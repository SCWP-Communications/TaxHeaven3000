init python:
    global ADDRESSES_NO_PAYMENT, ADDRESS_PAYMENT, RETURN_ADDRESS_STATE_MAPPING, SENDING_PAYMENT_ADDRESS_STATE_MAPPING
    ADDRESSES_NO_PAYMENT = [
        Address(
            name="Department of the Treasury",
            line_1="Internal Revenue Service",
            city="Kansas City",
            state="MO",
            zip="64999-0002"
        ),
        Address(
            name="Department of the Treasury",
            line_1="Internal Revenue Service",
            city="Austin",
            state="TX",
            zip="73301-0002"
        ),
        Address(
            name="Department of the Treasury",
            line_1="Internal Revenue Service",
            city="Ogden",
            state="UT",
            zip="84201-0002"
        )
    ]

    ADDRESS_PAYMENT = [
        Address(
            line_1="Internal Revenue Service",
            line_2="P.O. Box 931000",
            city="Louisville",
            state="KY",
            zip="40293-1000"
        ),
        Address(
            line_1="Internal Revenue Service",
            line_2="P.O. Box 1214",
            city="Charlotte",
            state="NC",
            zip="28201-1214"
        ),
        Address(
            line_1="Internal Revenue Service",
            line_2="P. O. Box 802501",
            city="Cincinnati",
            state="OH",
            zip="45280-2501"
        ),
    ]

    RETURN_ADDRESS_STATE_MAPPING = {
        'AK': 0, 
        'AL': 0, 
        'AR': 0, 
        'AZ': 1, 
        'CA': 2, 
        'CO': 2, 
        'CT': 0, 
        'DC': 0, 
        'DE': 0, 
        'FL': 1, 
        'GA': 0,
        'HI': 2, 
        'IA': 0, 
        'ID': 2, 
        'IL': 0, 
        'IN': 0, 
        'KS': 2, 
        'KY': 0, 
        'LA': 1, 
        'MA': 0, 
        'MD': 0, 
        'ME': 0,
        'MI': 2, 
        'MN': 2, 
        'MO': 1, 
        'MS': 0, 
        'MT': 0, 
        'NC': 0, 
        'ND': 2, 
        'NE': 2, 
        'NH': 0, 
        'NJ': 0, 
        'NM': 1,
        'NV': 2, 
        'NY': 0, 
        'OH': 2, 
        'OK': 0, 
        'OR': 2, 
        'PA': 0, 
        'RI': 0, 
        'SC': 0, 
        'SD': 2, 
        'TN': 0, 
        'TX': 1,
        'UT': 2, 
        'VA': 0, 
        'VT': 0, 
        'WA': 2, 
        'WI': 0, 
        'WV': 0, 
        'WY': 2
    }

    SENDING_PAYMENT_ADDRESS_STATE_MAPPING = {
        'AK': 0, 
        'AL': 1, 
        'AR': 0, 
        'AZ': 2, 
        'CA': 2, 
        'CO': 2, 
        'CT': 0, 
        'DC': 0, 
        'DE': 0, 
        'FL': 1, 
        'GA': 1,
        'HI': 2, 
        'IA': 0, 
        'ID': 2, 
        'IL': 0, 
        'IN': 0, 
        'KS': 2, 
        'KY': 0, 
        'LA': 1, 
        'MA': 0, 
        'MD': 0, 
        'ME': 0,
        'MI': 2, 
        'MN': 2, 
        'MO': 1, 
        'MS': 0, 
        'MT': 0, 
        'NC': 1, 
        'ND': 2, 
        'NE': 2, 
        'NH': 0, 
        'NJ': 0, 
        'NM': 2,
        'NV': 2, 
        'NY': 0, 
        'OH': 2, 
        'OK': 0, 
        'OR': 2, 
        'PA': 2, 
        'RI': 0, 
        'SC': 1, 
        'SD': 2, 
        'TN': 1, 
        'TX': 1,
        'UT': 2, 
        'VA': 0, 
        'VT': 0, 
        'WA': 2, 
        'WI': 0, 
        'WV': 0, 
        'WY': 2
    }

    def generate_address_to_send_returns_to():
        global is_sending_payment, residential_address, address_to_send_returns_to
        
        if is_sending_payment:
            address_to_send_returns_to = ADDRESS_PAYMENT[SENDING_PAYMENT_ADDRESS_STATE_MAPPING[residential_address.state]]
        else:
            address_to_send_returns_to = ADDRESSES_NO_PAYMENT[RETURN_ADDRESS_STATE_MAPPING[residential_address.state]]
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
