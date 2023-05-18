init python:
    import shutil
    import os
    import sys

    try:
        import _renpytfd
    except Exception:
        _renpytfd = None

    global file_uploader

    class FileUploader:
        def __init__(self):
            self.destination = renpy.config.savedir
        
        def choose_file(self):
            """
            Pops up a directory chooser.
            `path`
                The directory that is selected by default. If None, config.renpy_base
                is selected.
            Returns a (path, is_default) tuple, where path is the chosen directory,
            and is_default is true if and only if it was chosen by default mechanism
            rather than user choice.
            """
            
            if _renpytfd:
                file_path = _renpytfd.openFileDialog(__("Select File"), None, ["*.pdf"], None)
            
            return file_path
        
        def check_if_encrypted(self, file_path):
            try:
                PdfReader(file_path)
                return False
            except Exception as e:
                renpy.log(f"Error checking encryption: {e}")
                return True
        
        def get_ellipsized_file_name_for_path(self, path):
            head, tail = os.path.split(path)
            if len(tail) > 16:
                tail = f'{tail[0:16]}...'
            return tail
        
        def set_slotted_file(self, file_path):
            global file_slotted_for_upload
            file_slotted_for_upload = file_path
            renpy.restart_interaction()
        
        def upload_and_save_pdf(self,  location_value_name, replace=False, replacement_index=None, post_function=None, pdf_type=None, **kwargs):
            chosen_file = self.upload_pdf(location_value_name)
            if chosen_file is not None:
                self.save_pdf(chosen_file, location_value_name, replace, replacement_index, pdf_type=pdf_type)
            
            if post_function is not None:
                post_function(**kwargs)
            renpy.restart_interaction()
        
        def upload_pdf(self, location_value_name, should_return=True, post_function=None):
            global should_close_modal
            chosen_file = self.choose_file()
            
            if chosen_file is None:
                should_close_modal = True
            
            if post_function is not None:
                post_function(chosen_file)
            
            renpy.restart_interaction()
            
            if should_return:
                return chosen_file
        
        def save_pdf(self, chosen_file, location_value_name, replace=False, replacement_index=None,  notification_message=None, post_function=None, pdf_type=None, **kwargs):
            global should_close_modal
            try:
                chosen_filepath = os.fsdecode(chosen_file)
                is_encrypted = self.check_if_encrypted(chosen_filepath)
                renpy.log(is_encrypted)
                if is_encrypted:
                    if not in_diary:
                        add_error(location_value_name, FILE_IS_ENCRYPTED_ERROR_MESSAGE)
                    else:
                        renpy.notify(FILE_IS_ENCRYPTED_ERROR_MESSAGE)
                        should_close_modal = True
                    renpy.restart_interaction()
                    return
                
                new_path = copy_file(chosen_filepath, self.destination)
                value_name_type = type(globals()[location_value_name])
                if pdf_type == None:
                    pdf = PDF(new_path)
                else:
                    pdf = pdf_type(new_path)
                pdf.generate_preview_images()
                if value_name_type == renpy.revertable.RevertableList:
                    if replace:
                        globals()[location_value_name][replacement_index].delete_file_and_previews()
                        globals()[location_value_name][replacement_index] = pdf
                    else:
                        globals()[location_value_name].append(pdf)
                else:
                    
                    
                    prev_location = globals()[location_value_name]
                    globals()[location_value_name] = pdf
                    if replace:
                        prev_location.delete_file_and_previews()
                
                
                if notification_message is not None:
                    renpy.notify(notification_message)
                
                should_close_modal = True
                
                if post_function is not None:
                    post_function(**kwargs)
                
                clear_error_by_id(location_value_name)
                renpy.restart_interaction()
            except Exception as e:
                renpy.log(e)
                if not in_diary:
                    add_error(location_value_name, "Something went wrong, please try again")
                else:
                    renpy.notify(DEFAULT_FILE_ERROR_MESSAGE)
                    should_close_modal = True
        
        def delete_pdf(self, index, location_value_name, notification_message=None, post_function=None, **kwargs):
            global should_close_modal
            value_name_type = type(globals()[location_value_name])
            if value_name_type == renpy.revertable.RevertableList:
                globals()[location_value_name][index].delete_file_and_previews()
                globals()[location_value_name].pop(index)
            else:
                globals()[location_value_name].delete_file_and_previews()
                globals()[location_value_name] = None
            
            if notification_message is not None:
                renpy.notify(notification_message)
            
            should_close_modal = True
            
            if post_function is not None:
                post_function(**kwargs)
            
            if not in_diary:
                renpy.restart_interaction()

    file_uploader = FileUploader()

    def choose_save_filepath():
        if _renpytfd:
            file_path = _renpytfd.saveFileDialog(__("Save File"), "2022 Tax Return", ["*.pdf"], None)
            name = os.path.basename(file_path)
            path = os.path.dirname(file_path)
            return path, name

    def download_file(file_to_download_path, error_value_name):
        global downloaded_return, ctc_disabled
        try:
            clear_error_by_id(error_value_name)
            (download_dir, name) = choose_save_filepath()
            copy_file(file_to_download_path, dest=download_dir, dest_name=f"{name}.pdf")
            downloaded_return = True
            ctc_disabled = False
            renpy.restart_interaction()
        except Exception as e:
            downloaded_return = False
            renpy.log(e)
            if not in_diary:
                add_error(error_value_name, "Something went wrong, please try again")
            else:
                renpy.notify(DEFAULT_FILE_ERROR_MESSAGE)

    def copy_file(src, dest, dest_name=None):
        """Safely copy a file to the specified directory. If a file with the same name already 
        exists, the copied file name is altered to preserve both.

        :param str src: Path to the file to copy.
        :param str dest: Directory to copy the file into.
            file.
        """
        name = dest_name or os.path.basename(src)
        if not os.path.exists(os.path.join(dest, name)):
            return shutil.copy(src, os.path.join(dest, name))
        else:
            base, extension = os.path.splitext(name)
            i = 1
            while os.path.exists(os.path.join(dest, '{}_{}{}'.format(base, i, extension))):
                i += 1
            return shutil.copy(src, os.path.join(dest, '{}_{}{}'.format(base, i, extension)))

    def delete_pdfs_in_save_dir():
        
        for parent, dirnames, filenames in os.walk(renpy.config.savedir):
            for fn in filenames:
                if fn.lower().endswith('.pdf'):
                    try:
                        renpy.log(f'{parent} {fn}')
                        os.remove(os.path.join(parent, fn))
                    except Exception as e:
                        pass
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
