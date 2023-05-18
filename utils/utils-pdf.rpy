init python:
    from pypdf import PdfReader, PdfWriter, PdfMerger
    from pypdf.generic import BooleanObject, NameObject, IndirectObject, TextStringObject, NumberObject
    import time
    import io

    if renpy.macintosh:
        from fitz.__main__ import open_file as fitz_open

    def openpdf(fn):
        
        import os.path
        import subprocess
        
        fn = renpy.fsencode(fn)
        
        try:
            if renpy.windows:
                os.startfile(fn)
            elif renpy.macintosh:
                subprocess.Popen([ "open", fn ])
            else:
                subprocess.Popen([ "xdg-open", fn])
        except:
            if config.developer:
                raise

    class PDF:
        def __init__(self, file_path):
            self.file_path = file_path
            self.destination = renpy.config.savedir
            self.preview_images = []
            self.set_file_name_without_path()
        
        def get_thumbnail(self):
            try:
                return self.preview_images[0]
            except Exception as e:
                renpy.log(e)
                return None
        
        def get_preview_images(self):
            try:
                return self.preview_images
            except Exception:
                return []
        
        def get_file_path(self):
            return self.file_path
        
        def get_file_name(self):
            return self.file_name
        
        def delete_file(self, src):
            if os.path.exists(src):
                os.remove(src)
        
        def delete_file_and_previews(self):
            self.delete_file(self.file_path)
        
        def set_file_name_without_path(self):
            head, tail = os.path.split(self.file_path)
            self.file_name = tail
        
        def get_ellipsized_filename(self):
            if len(self.file_name) > 15:
                return f'{self.file_name[0:15]}...'
            else:
                return self.file_name
        
        def generate_preview_images(self):
            if renpy.macintosh:
                try:
                    doc = fitz_open(self.file_path, password=None)
                    for idx, page in enumerate(doc):
                        pix = page.get_pixmap(dpi=100)
                        with io.BytesIO() as output:
                            preview_image_bytes = pix.pil_save(output, format="PNG")
                            self.preview_images.append(output.getvalue())
                except Exception:
                    self.preview_images = []
            else:
                pass

    class W2(PDF):
        def __init__(self, file_path):
            super().__init__(file_path)
            self.box_1 = None 
            self.box_2 = None 
            self.box_4 = None 
        
        def set_box_1(self, val):
            self.box_1 = val
        
        def set_box_2(self, val):
            self.box_2 = val
        
        def set_box_4(self, val):
            self.box_4 = val
        
        def get_box_1(self):
            return self.box_1 or 0
        
        def get_box_2(self):
            return self.box_2 or 0
        
        def get_box_4(self):
            return self.box_4 or 0

    def get_total_w2_box_1():
        global w2_objects
        sum = 0
        for object in w2_objects:
            sum += object.get_box_1()
        return sum

    def get_total_w2_box_2():
        global w2_objects
        sum = 0
        for object in w2_objects:
            sum += object.get_box_2()
        return sum

    def get_total_w2_box_4():
        global w2_objects
        sum = 0
        for object in w2_objects:
            sum += object.get_box_4()
        return sum

    class FillablePdf:
        def __init__(self, template_location):
            self.reader = PdfReader(template_location)
            self._template_location = template_location
            if "/AcroForm" in self.reader.trailer["/Root"]:
                self.reader.trailer["/Root"]["/AcroForm"].update({NameObject("/NeedAppearances"): BooleanObject(True)})
            
            self.writer = PdfWriter()
            self.writer._info = self.reader.trailer["/Info"]
            reader_trailer = self.reader.trailer["/Root"]
            self.writer._root_object.update(
                {
                    key: reader_trailer[key]
                    for key in reader_trailer
                    if key in ("/AcroForm", "/Lang", "/MarkInfo")
                }
            )
            
            self.set_need_appearances_writer()
            time.sleep(1)
            if "/AcroForm" in self.writer._root_object:
                self.writer._root_object["/AcroForm"].update({NameObject("/NeedAppearances"): BooleanObject(True)})
        
        def set_need_appearances_writer(self):
            
            try:
                catalog = self.writer._root_object
                time.sleep(1)
                
                if "/AcroForm" not in catalog:
                    self.writer._root_object.update({
                        NameObject("/AcroForm"): IndirectObject(len(writer._objects), 0, writer)})
                
                need_appearances = NameObject("/NeedAppearances")
                self.writer._root_object["/AcroForm"][need_appearances] = BooleanObject(True)
            
            except Exception as e:
                renpy.log('set_need_appearances_writer() catch : ', repr(e))
        
        def updatePageFormFieldValues(self, page, fields):
            '''
                Update the form field values for a given page from a fields dictionary.

            This was copied from the PyPDF2 library and adapted for my use case.


                Copy field texts and values from fields to page.
                :param page: Page reference from PDF writer where the annotations
                    and field data will be updated.
                :param fields: a Python dictionary of field names (/T) and text
                    values (/V)
                '''
            
            if page.get('/Annots', None) is not None:
                for j in range(0, len(page['/Annots'])):
                    writer_annot = page['/Annots'][j].get_object()
                    field = writer_annot.get('/T') 
                    if writer_annot.get("/FT") == "/Btn":
                        value = fields.get(field, False)
                        if value and value == '/On':
                            writer_annot.update(
                                    {
                                        NameObject("/AS"): NameObject("/On"),
                                        NameObject("/V"): NameObject("/On"),
                                    }
                                )
                    elif writer_annot.get("/FT") == "/Tx":
                        value = fields.get(field, False)
                        if value:
                            writer_annot.update(
                                    {
                                        NameObject("/V"): TextStringObject(value)
                                    }
                                )
                            writer_annot.pop('/AP', None)
        
        
        def fill_document(self, field_map, omit_zeros=False):
            for idx, page in enumerate(self.reader.pages):
                fields_to_update_on_page = {}
                self.writer.add_page(page)
                
                for key, key_name in field_map[idx].items():
                    if type(key_name) is tuple:
                        
                        
                        value = globals()[key_name[0]] == key_name[1]
                    else:
                        value = globals()[key_name]
                    
                    if type(value) is bool:
                        value = '/On' if value else '/Off'
                    
                    if type(value) is float or type(value) is int:
                        
                        if omit_zeros and value == 0:
                            continue
                        
                        value = '{0:.2f}'.format(value)
                    
                    if type(value) is NoneType:
                        if omit_zeros:
                            continue
                        else:
                            value = '{0:.2f}'.format(0)
                    
                    
                    fields_to_update_on_page.update({key: str(value)})
                
                self.updatePageFormFieldValues(self.writer.pages[idx], fields=fields_to_update_on_page)











    class Form1040(FillablePdf):
        FIELD_MAP = [
            {
                'status_single': 'is_single_filer',
                'last_name': 'last_name',
                'someone_can_claim_as_dependent': 'someone_can_claim_as_dependent',
                'were_born_before_january_2_1958': 'was_born_before_jan_2_1958',
                'is_blind': 'is_blind',
                '1a': 'form_1040_line_1a',
                '1b': 'household_empoloyee_wages_not_reported_on_w2',
                '1i': 'nontaxable_combat_pay_election',
                '1z': 'form_1040_line_1z',
                '2a': 'form_1040_line_2a',
                '2b': 'form_1040_line_2b',
                '6a': 'social_security_taxable_amount',
                '6b': 'form_1040_line_6b',
                '8': 'form_1040_line_8',
                '9': 'form_1040_line_9',
                '10': 'form_1040_line_10',
                '11': 'form_1040_line_11',
                '12': 'form_1040_line_12',
                '14': 'form_1040_line_14',
                '15': 'form_1040_line_15',
            },
            { 
                '16': 'form_1040_line_16',
                '18': 'form_1040_line_18',
                '20': 'form_1040_line_20',
                '21': 'form_1040_line_21',
                '22': 'form_1040_line_22',
                '24': 'form_1040_line_24',
                '25a': 'federal_income_tax_witheld_from_w2',
                '25b': 'form_1040_line_25b',
                '25d': 'form_1040_line_25d',
                '26': 'estimated_tax_payments_and_amount_applied_from_prev_year',
                '27': 'form_1040_line_27',
                '29': 'form_1040_line_29',
                '31': 'form_schedule3_line_15',
                '32': 'form_1040_line_32',
                '33': 'form_1040_line_33',
                'phone_number': 'phone_number',
                'email': 'email',
                'occupation': 'occupation',
                'preparers_signature': 'form_1040_preparers_signature'
            }

        ]
        TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/1040.pdf"
        def __init__(self):
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/1040.pdf"
        
        def fill_document(self, has_schedule1=False):
            super().fill_document(field_map=self.FIELD_MAP, omit_zeros=True)
            
            global residential_address, first_name, middle_name, social_security_number, form_schedule1_line_10, form_1040_line_34, amount_to_be_refunded, routing_number, bank_account_number, is_checking_account, is_savings_account
            fields_to_update_page_1 = {}
            fields_to_update_page_1.update({'first_name_middle_initial': format_first_name_middle_initial(first_name, middle_name)})
            fields_to_update_page_1.update({'ssn': format_ssn(social_security_number)})
            fields_to_update_page_1.update({'not_received_or_sold_digital_asset': '/On'})
            fields_to_update_page_1.update({
                'address_line_1': residential_address.line_1,
                'address_line_2': residential_address.line_2,
                'address_city': residential_address.city,
                'address_state': residential_address.state,
                'address_zip': residential_address.zip,
            })
            
            if has_schedule1:
                fields_to_update_page_1.update({'8': '{0:.2f}'.format(form_schedule1_line_10)})
            
            
            super().updatePageFormFieldValues(self.writer.pages[0], fields=fields_to_update_page_1)
            
            fields_to_update_page_2 = {}
            if form_1040_line_34 > 0:
                fields_to_update_page_2.update(
                    {
                        '34': '{0:.2f}'.format(form_1040_line_34),
                        '35a': '{0:.2f}'.format(amount_to_be_refunded),
                        'routing_number': routing_number,
                        'account_number': bank_account_number,
                        'account_type_checking': '/On' if is_checking_account else '/Off',
                        'account_type_savings': '/On' if not is_checking_account else '/Off',
                        '36': '{0:.2f}'.format(form_1040_line_34 - amount_to_be_refunded)
                    }
                )
            else:
                fields_to_update_page_2.update(
                    {
                        '37': '{0:.2f}'.format(form_1040_line_37)
                    }
                )
            
            
            super().updatePageFormFieldValues(self.writer.pages[1], fields=fields_to_update_page_2)
            
            
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)

    class Form8863(FillablePdf):
        FIELD_MAP = [
            {
                '1': 'form_8863_line_30',
                '2': 'form_8863_line_2',
                '3': 'form_8863_line_3',
                '4': 'form_8863_line_4'
            },
            {}
        ]
        
        TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/8863.pdf"
        
        def __init__(self):
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/8863.pdf"
        
        def fill_document(self):
            global social_security_number, ineligible_for_edu_credits, first_name, middle_name, last_name, aoc_claimed_last_four_years, student_status, HALF_TIME_CHOICE, FULL_TIME_CHOICE, aoc_first_four_years_completed_before_this_year, aoc_has_been_convicted, claiming_aoc, claiming_lllc, aoc_qualified_educational_expenses, form_8863_line_28, form_8863_line_29, form_8863_line_30, form_8863_line_31, form_8863_line_7_box, form_8863_line_15
            super().fill_document(field_map=self.FIELD_MAP)
            fields_to_update_page_1 = {}
            
            
            if not ineligible_for_edu_credits:
                for idx in range(5, 11):
                    value = globals()[f'form_8863_line_{idx}']
                    
                    if type(value) is bool:
                        value = '/On' if value else '/Off'
                    
                    if type(value) is float:
                        if idx is not 6:
                            value = '{0:.2f}'.format(value)
                        else:
                            value = '{0:.3f}'.format(value)
                    
                    fields_to_update_page_1.update({str(idx): str(value or 0)})
                
                
                if claiming_lllc:
                    for idx in range(11, 16):
                        value = globals()[f'form_8863_line_{idx}']
                        value = '{0:.2f}'.format(value)
                        
                        fields_to_update_page_1.update({
                            str(idx): value
                        })
                    
                    
                    if form_8863_line_15 > 0:
                        fields_to_update_page_1.update(
                            {
                                '16': '{0:.2f}'.format(form_8863_line_16),
                                '17': '{0:.3f}'.format(form_8863_line_17)
                            }
                        )
                
                fields_to_update_page_1.update(
                    {
                        '7_box': '/On' if form_8863_line_7_box else '/Off',
                        '18': '{0:.2f}'.format(form_8863_line_18),
                        '19': '{0:.2f}'.format(form_8863_line_19)
                    }
                )
            
            full_name = format_full_name(first_name, middle_name, last_name)
            fields_to_update_page_1.update({'name_1': full_name})
            
            formatted_ssn = format_ssn(social_security_number)
            fields_to_update_page_1.update({'ssn_1': formatted_ssn})
            
            super().updatePageFormFieldValues(self.writer.pages[0], fields=fields_to_update_page_1)
            
            fields_to_update_page_2 = {}
            fields_to_update_page_2.update({'name_2': full_name})
            fields_to_update_page_2.update({'ssn_2': formatted_ssn})
            fields_to_update_page_2.update({'student_ssn': formatted_ssn})
            fields_to_update_page_2.update({'student_name': full_name})
            
            
            school_1 = aoc_schools[0]
            fields_to_update_page_2.update({'school_name_1': school_1.name})
            fields_to_update_page_2.update({'school_1_address_line_1': format_address_into_one_line(school_1.line_1, school_1.line_2, school_1.city, school_1.state, school_1.zip)})
            fields_to_update_page_2.update({'did_receive_1098t_1': '/On' if school_1.did_receive_1098t_this_year else '/Off'})
            fields_to_update_page_2.update({'did_not_receive_1098t_1': '/On' if not school_1.did_receive_1098t_this_year else '/Off'})
            fields_to_update_page_2.update({'did_receive_1098t_previous_year_box_7_1': '/On' if school_1.did_receive_1098t_previous_year_box_7 else '/Off'})
            fields_to_update_page_2.update({'did_not_receive_1098t_previous_year_box_7_1': '/On' if not school_1.did_receive_1098t_previous_year_box_7 else '/Off'})
            
            
            if claiming_aoc:
                ein = school_1.ein
                (ein_1, ein_2) = format_ein(ein)
                fields_to_update_page_2.update({'ein_1_1': ein_1})
                fields_to_update_page_2.update({'ein_1_2': ein_2})
            
            
            
            if len(aoc_schools) > 1:
                school_2 = aoc_schools[1]
                fields_to_update_page_2.update({'school_name_2': school_2.name})
                fields_to_update_page_2.update({'school_2_address_line_2': format_address_into_one_line(school_2.line_1, school_2.line_2, school_2.city, school_2.state, school_2.zip)})
                fields_to_update_page_2.update({'did_receive_1098t_2': '/On' if school_2.did_receive_1098t_this_year else '/Off'})
                fields_to_update_page_2.update({'did_not_receive_1098t_2': '/On' if not school_2.did_receive_1098t_this_year else '/Off'})
                fields_to_update_page_2.update({'did_receive_1098t_previous_year_box_7_2': '/On' if school_2.did_receive_1098t_previous_year_box_7 else '/Off'})
                fields_to_update_page_2.update({'did_not_receive_1098t_previous_year_box_7_2': '/On' if not school_2.did_receive_1098t_previous_year_box_7 else '/Off'})
                
                if claiming_aoc:
                    (ein_1, ein_2) = format_ein(school_2.ein)
                    fields_to_update_page_2.update({'ein_2_1': ein_1})
                    fields_to_update_page_2.update({'ein_2_2': ein_2})
            
            fields_to_update_page_2.update({
                'claimed_last_four_years': '/On' if aoc_claimed_last_four_years else '/Off',
                'not_claimed_last_four_years': '/On' if not aoc_claimed_last_four_years else '/Off'
            })
            
            if not aoc_claimed_last_four_years:
                fields_to_update_page_2.update({'in_school_at_least_half_of_time': '/On' if student_status in [HALF_TIME_CHOICE, FULL_TIME_CHOICE] else '/Off'})
                fields_to_update_page_2.update({'not_in_school_at_least_half_of_time': '/On' if not student_status in [HALF_TIME_CHOICE, FULL_TIME_CHOICE] else '/Off'})
                
                if student_status in [HALF_TIME_CHOICE, FULL_TIME_CHOICE]:
                    fields_to_update_page_2.update({'completed_first_four_years': '/On' if aoc_first_four_years_completed_before_this_year else '/Off'})
                    fields_to_update_page_2.update({'not_completed_first_four_years': '/On' if not aoc_first_four_years_completed_before_this_year else '/Off'})
                    
                    if not aoc_first_four_years_completed_before_this_year:
                        fields_to_update_page_2.update({'has_been_convicted': '/On' if aoc_has_been_convicted else '/Off'})
                        fields_to_update_page_2.update({'has_not_been_convicted': '/On' if not aoc_has_been_convicted else '/Off'})
            
            
            if claiming_aoc:
                fields_to_update_page_2.update({'27': '{0:.2f}'.format(aoc_qualified_educational_expenses)})
                fields_to_update_page_2.update({'28': '{0:.2f}'.format(form_8863_line_28)})
                fields_to_update_page_2.update({'29': '{0:.2f}'.format(form_8863_line_29)})                
                fields_to_update_page_2.update({'30': '{0:.2f}'.format(form_8863_line_30)})                
            elif claiming_lllc:                       
                fields_to_update_page_2.update({'31': '{0:.2f}'.format(form_8863_line_31)})                
            
            super().updatePageFormFieldValues(self.writer.pages[1], fields=fields_to_update_page_2)
            
            
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)       

    class FormSchedule3(FillablePdf):
        FIELD_MAP = [
            {   
                '3': 'form_8863_line_19',
                '8': 'form_8863_line_19'
            },
            {
                '11': 'form_schedule3_line_11',
                '15': 'form_schedule3_line_15'
            }
        ]
        
        TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/schedule3.pdf"
        
        def __init__(self):
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/schedule3.pdf"
        
        def fill_document(self):
            global social_security_number, first_name, middle_name, last_name
            super().fill_document(field_map=self.FIELD_MAP, omit_zeros=True)
            full_name = format_full_name(first_name, middle_name, last_name)
            super().updatePageFormFieldValues(self.writer.pages[0], fields={'name_1': full_name, 'ssn_1': format_ssn(social_security_number)})           
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)

    class FormSchedule1(FillablePdf):
        FIELD_MAP = [
            {
                '7': 'unemployment_compensation',
                '10': 'form_schedule1_line_10'
            },
            {
                '11': 'form_schedule1_line_11',
                '20': 'form_schedule1_line_20',
                '21': 'form_schedule1_line_21',
                '26': 'form_schedule1_line_26'
            }
        ]
        
        TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/schedule1.pdf"
        
        def __init__(self):
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/schedule1.pdf"
        
        def fill_document(self):
            global social_security_number, first_name, middle_name, last_name
            super().fill_document(field_map=self.FIELD_MAP, omit_zeros=True)
            full_name = format_full_name(first_name, middle_name, last_name)
            super().updatePageFormFieldValues(self.writer.pages[0], fields={'name': full_name, 'ssn': format_ssn(social_security_number)})           
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)

    class FormScheduleB(FillablePdf):
        FIELD_MAP = [
            {
                '2': 'form_scheduleb_line_2',
                '4': 'form_scheduleb_line_2',
            }
        ]
        
        TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/scheduleb.pdf"
        
        def __init__(self):
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/scheduleb.pdf"
        
        def fill_document(self):
            global social_security_number, first_name, middle_name, last_name, int_1099_objects
            super().fill_document(field_map=self.FIELD_MAP)
            full_name = format_full_name(first_name, middle_name, last_name)
            fields_to_update = {'first_middle_last_name': full_name, 'ssn': format_ssn(social_security_number)}
            
            for idx, obj in enumerate(int_1099_objects):
                amount = obj.get_taxable_interest()
                fields_to_update.update({
                    f'payer_name_{idx}': obj.payer_name,
                    f'amount_{idx}': '{0:.2f}'.format(convert_to_dollar_amount(amount))
                })
            
            
            if form_scheduleb_line_2 > 1500:
                fields_to_update.update({
                    '7a_no': '/On',
                    '7ai_no': '/On',
                    '8_no': '/On'
                })
            else:
                fields_to_update.update({
                    '7a_no': '/Off',
                    '7ai_no': '/Off',
                    '8_no': '/Off'
                })
            
            super().updatePageFormFieldValues(self.writer.pages[0], fields=fields_to_update)           
            
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)

    class Form1040V(FillablePdf):
        FIELD_MAP = [
            {
                'ssn': 'social_security_number',
                'last_name': 'last_name',
                'amount_paying': 'form_1040_line_37'
            },
            {}
        ]
        
        TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/1040v.pdf"
        
        def __init__(self):
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/1040v.pdf"
        
        def fill_document(self):
            super().fill_document(field_map=self.FIELD_MAP)
            
            fields_to_update = {}
            
            first_middle_initial = format_first_name_middle_initial(first_name, middle_name)
            
            fields_to_update.update({
                'first_middle_initial': first_middle_initial,
                'address_line_1': residential_address.line_1,
                'address_line_2': residential_address.line_2,
                'address_city': residential_address.city,
                'address_state': residential_address.state,
                'address_zip': residential_address.zip,
            })
            
            super().updatePageFormFieldValues(self.writer.pages[0], fields=fields_to_update)           
            
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)

    class CoverSheet(FillablePdf):
        FIELD_MAP = [
            {
            }
        ]
        
        def __init__(self, template_name):
            self.TEMPLATE_LOCATION = f"{renpy.config.gamedir}/file_templates/cover_sheets/{template_name}"
            super().__init__(self.TEMPLATE_LOCATION)
            self.location = f"{renpy.config.savedir}/cover_sheet.pdf"
        
        def fill_document(self):
            super().fill_document(field_map=self.FIELD_MAP)
            super().updatePageFormFieldValues(
                self.writer.pages[0], 
                fields={
                    'state': residential_address.state
                }
            )           
            
            with open(self.location, "wb") as output_stream:
                self.writer.write(output_stream)

    def generate_return():
        global qualifies_for_eitc, claiming_aoc, claiming_lllc, has_educator_expenses, has_tax_deferred_ira_contributions, has_student_loan_interest, has_unemployment_compensation, return_file_location, w2_objects
        
        calculate_return()
        files_to_combine = []
        
        schedule1_file_location = None
        form_8863_file_location = None
        schedule3_file_location = None
        scheduleb_file_location = None
        if has_educator_expenses or (tax_deferred_ira_contributions != None and tax_deferred_ira_contributions > 0) or has_student_loan_interest or has_unemployment_compensation:
            file_schedule1 = FormSchedule1()
            file_schedule1.fill_document()
            schedule1_file_location = file_schedule1.location
        
        
        if claiming_aoc or claiming_lllc:
            file_8863 = Form8863()
            file_8863.fill_document()
            form_8863_file_location = file_8863.location
        
        if claiming_aoc or claiming_lllc or has_excess_social_security_to_claim:
            file_schedule3 = FormSchedule3()
            file_schedule3.fill_document()
            schedule3_file_location = file_schedule3.location
        
        
        if has_income_interest:
            file_scheduleb = FormScheduleB()
            file_scheduleb.fill_document()
            scheduleb_file_location = file_scheduleb.location
        
        
        generate_address_to_send_returns_to()
        if is_sending_payment:
            cover_sheet_index = SENDING_PAYMENT_ADDRESS_STATE_MAPPING[residential_address.state]
            cover_sheet_name = f"cover_payment_0{cover_sheet_index}.pdf"
        else:
            cover_sheet_index = RETURN_ADDRESS_STATE_MAPPING[residential_address.state]
            cover_sheet_name = f"cover_wo_payment_0{cover_sheet_index}.pdf"
        
        cover_sheet = CoverSheet(cover_sheet_name)
        cover_sheet.fill_document()
        files_to_combine.append(cover_sheet.location)
        files_to_combine.append(f"{renpy.config.gamedir}/file_templates/cover_sheets/glossary.pdf")
        
        
        file_1040 = Form1040()
        file_1040.fill_document(has_schedule1=True if schedule1_file_location is not None else False)
        files_to_combine.append(file_1040.location)
        
        if form_1040_line_37 > 0:
            
            file_1040v = Form1040V()
            file_1040v.fill_document()
            files_to_combine.append(file_1040v.location)
        
        
        
        
        
        
        
        if schedule1_file_location is not None:
            files_to_combine.append(schedule1_file_location)
        if scheduleb_file_location is not None:
            files_to_combine.append(scheduleb_file_location)
        if schedule3_file_location is not None:
            files_to_combine.append(schedule3_file_location)
        if form_8863_file_location is not None:
            files_to_combine.append(form_8863_file_location)
        
        
        for file in w2_objects:
            files_to_combine.append(file.get_file_path())
        
        
        if has_unemployment_compensation:
            files_to_combine.append(unemployment_1099g_file_location.get_file_path())
        
        
        merger = PdfMerger()
        for file in files_to_combine:
            if not os.path.isfile(file):
                
                renpy.log("No file found")
                pass
            else:
                try:
                    if PdfReader(file).is_encrypted:
                        
                        pass
                    else:
                        merger.append(file)
                except Exception:
                    pass
        
        return_file_location = f'{renpy.config.savedir}/return.pdf'
        merger.write(return_file_location)

    PDF_TYPE_MAPPINGS = { 'W2': W2, 'PDF': PDF }
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
