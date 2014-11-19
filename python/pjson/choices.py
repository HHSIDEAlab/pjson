#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ai ts=4 sts=4 et sw=4
#Alan Viars



LICENSE_TYPE_CODES = ('AK-APN', 'AK-CNA', 'AK-CNM', 'AK-CNS', 'AK-DCH', 'AK-DEN',
                      'AK-DOS', 'AK-DPM',
'AK-DVM', 'AK-MDR', 'AK-MWF', 'AK-NPR', 'AK-ODR', 'AK-PAS', 'AK-RPH', 'AK-UNK',
'AL-APN', 'AL-CNA', 'AL-CNM', 'AL-CNS', 'AL-DCH', 'AL-DEN', 'AL-DOS', 'AL-DPM',
'AL-DVM', 'AL-MDR', 'AL-MWF', 'AL-NPR', 'AL-ODR', 'AL-PAS', 'AL-RPH', 'AL-UNK',
'AR-APN', 'AR-CNA', 'AR-CNM', 'AR-CNS', 'AR-DCH', 'AR-DEN', 'AR-DOS', 'AR-DPM',
'AR-DVM', 'AR-MDR', 'AR-MWF', 'AR-NPR', 'AR-ODR', 'AR-PAS', 'AR-RPH', 'AR-UNK',
'AS-UNK', 'AZ-APN', 'AZ-CNA', 'AZ-CNM', 'AZ-CNS', 'AZ-DCH', 'AZ-DEN', 'AZ-DOS',
'AZ-DPM', 'AZ-DVM', 'AZ-MDR', 'AZ-MWF', 'AZ-NPR', 'AZ-ODR', 'AZ-PAS', 'AZ-RPH',
'AZ-UNK', 'CA-APN', 'CA-CNA', 'CA-CNM', 'CA-CNS', 'CA-DCH', 'CA-DEN', 'CA-DOS',
'CA-DPM', 'CA-DVM', 'CA-MDR', 'CA-MWF', 'CA-NPR', 'CA-ODR', 'CA-PAS', 'CA-RPH',
'CA-UNK', 'CO-APN', 'CO-CNA', 'CO-CNM', 'CO-CNS', 'CO-DCH', 'CO-DEN', 'CO-DOS',
'CO-DPM', 'CO-DVM', 'CO-MDR', 'CO-MDU', 'CO-MWF', 'CO-NPR', 'CO-ODR', 'CO-PAS',
'CO-RPH', 'CO-UNK', 'CT-APN', 'CT-CNA', 'CT-CNM', 'CT-CNS', 'CT-DCH', 'CT-DEN',
'CT-DOS', 'CT-DPM', 'CT-DVM', 'CT-MDR', 'CT-MWF', 'CT-NPR', 'CT-ODR', 'CT-PAS',
'CT-RPH', 'CT-UNK', 'DC-APN', 'DC-CNA', 'DC-CNM', 'DC-CNS', 'DC-DCH', 'DC-DEN',
'DC-DOS', 'DC-DPM', 'DC-DVM', 'DC-MDR', 'DC-MWF', 'DC-NPR', 'DC-ODR', 'DC-PAS',
'DC-RPH', 'DC-UNK', 'DE-APN', 'DE-CNA', 'DE-CNM', 'DE-CNS', 'DE-DCH', 'DE-DEN',
'DE-DOS', 'DE-DPM', 'DE-DVM', 'DE-MDR', 'DE-MWF', 'DE-NPR', 'DE-ODR', 'DE-PAS',
'DE-RPH', 'DE-UNK', 'FL-APN', 'FL-CNA', 'FL-CNM', 'FL-CNS', 'FL-DCH', 'FL-DEN',
'FL-DOS', 'FL-DPM', 'FL-DVM', 'FL-MDR', 'FL-MWF', 'FL-NPR', 'FL-ODR', 'FL-PAS',
'FL-RPH', 'FL-UNK', 'FM-UNK', 'GA-APN', 'GA-CNA', 'GA-CNM', 'GA-CNS', 'GA-DCH',
'GA-DEN', 'GA-DOS', 'GA-DPM', 'GA-DVM', 'GA-MDR', 'GA-MWF', 'GA-NPR', 'GA-ODR',
'GA-PAS', 'GA-RPH', 'GA-UNK', 'GU-UNK', 'HI-APN', 'HI-CNA', 'HI-CNM', 'HI-CNS',
'HI-DCH', 'HI-DEN', 'HI-DOS', 'HI-DPM', 'HI-DVM', 'HI-MDR', 'HI-MWF', 'HI-NPR',
'HI-ODR', 'HI-PAS', 'HI-RPH', 'HI-UNK', 'IA-APN', 'IA-CNA', 'IA-CNM', 'IA-CNS',
'IA-DCH', 'IA-DEN', 'IA-DOS', 'IA-DPM', 'IA-DVM', 'IA-MDR', 'IA-MWF', 'IA-NPR',
'IA-ODR', 'IA-PAS', 'IA-RPH', 'IA-UNK', 'ID-APN', 'ID-CNA', 'ID-CNM', 'ID-CNS',
'ID-DCH', 'ID-DEN', 'ID-DOS', 'ID-DPM', 'ID-DVM', 'ID-MDR', 'ID-MWF', 'ID-NPR',
'ID-ODR', 'ID-PAS', 'ID-RPH', 'ID-UNK', 'IL-APN', 'IL-CNA', 'IL-CNM', 'IL-CNS',
'IL-DCH', 'IL-DEN', 'IL-DOS', 'IL-DPM', 'IL-DVM', 'IL-MDR', 'IL-MWF', 'IL-NPR',
'IL-ODR', 'IL-PAS', 'IL-RPH', 'IL-UNK', 'IN-APN', 'IN-CNA', 'IN-CNM', 'IN-CNS',
'IN-DCH', 'IN-DEN', 'IN-DOS', 'IN-DPM', 'IN-DVM', 'IN-MDR', 'IN-MWF', 'IN-NPR',
'IN-ODR', 'IN-PAS', 'IN-RPH', 'IN-UNK', 'KS-APN', 'KS-CNA', 'KS-CNM', 'KS-CNS',
'KS-DCH', 'KS-DEN', 'KS-DOS', 'KS-DPM', 'KS-DVM', 'KS-MDR', 'KS-MWF', 'KS-NPR',
'KS-ODR', 'KS-PAS', 'KS-RPH', 'KS-UNK', 'KY-APN', 'KY-CNA', 'KY-CNM', 'KY-CNS',
'KY-DCH', 'KY-DEN', 'KY-DOS', 'KY-DPM', 'KY-DVM', 'KY-MDR', 'KY-MWF', 'KY-NPR',
'KY-ODR', 'KY-PAS', 'KY-RPH', 'KY-UNK', 'LA-APN', 'LA-CNA', 'LA-CNM', 'LA-CNS',
'LA-DCH', 'LA-DEN', 'LA-DOS', 'LA-DPM', 'LA-DVM', 'LA-MDR', 'LA-MWF', 'LA-NPR',
'LA-ODR', 'LA-PAS', 'LA-RPH', 'LA-UNK', 'MA-APN', 'MA-CNA', 'MA-CNM', 'MA-CNS',
'MA-DCH', 'MA-DEN', 'MA-DOS', 'MA-DPM', 'MA-DVM', 'MA-MDR', 'MA-MWF', 'MA-NPR',
'MA-ODR', 'MA-PAS', 'MA-RPH', 'MA-UNK', 'MD-APN', 'MD-CNA', 'MD-CNM', 'MD-CNS',
'MD-DCH', 'MD-DEN', 'MD-DOS', 'MD-DPM', 'MD-DVM', 'MD-MDR', 'MD-MWF', 'MD-NPR',
'MD-ODR', 'MD-PAS', 'MD-RPH', 'MD-UNK', 'ME-APN', 'ME-CNA', 'ME-CNM', 'ME-CNS',
'ME-DCH', 'ME-DEN', 'ME-DOS', 'ME-DPM', 'ME-DVM', 'ME-MDR', 'ME-MWF', 'ME-NPR',
'ME-ODR', 'ME-PAS', 'ME-RPH', 'ME-UNK', 'MH-UNK', 'MI-APN', 'MI-CNA', 'MI-CNM',
'MI-NPR', 'MI-ODR', 'MI-PAS', 'MI-RPH', 'MI-UNK', 'MN-APN', 'MN-CNA', 'MN-CNM',
'MN-CNS', 'MN-DCH', 'MN-DEN', 'MN-DOS', 'MN-DPM', 'MN-DVM', 'MN-MDR', 'MN-MWF',
'MN-NPR', 'MN-ODR', 'MN-PAS', 'MN-RPH', 'MN-UNK', 'MO-APN', 'MO-CNA', 'MO-CNM',
'MO-CNS', 'MO-DCH', 'MO-DEN', 'MO-DOS', 'MO-DPM', 'MO-DVM', 'MO-MDR', 'MO-MWF',
'MO-NPR', 'MO-ODR', 'MO-PAS', 'MO-RPH', 'MO-UNK', 'MP-UNK', 'MS-APN', 'MS-CNA',
'MS-CNM', 'MS-CNS', 'MS-DCH', 'MS-DEN', 'MS-DOS', 'MS-DPM', 'MS-DVM', 'MS-MDR',
'MS-MWF', 'MS-NPR', 'MS-ODR', 'MS-PAS', 'MS-RPH', 'MS-UNK', 'MT-APN', 'MT-CNA',
'MT-CNM', 'MT-CNS', 'MT-DCH', 'MT-DEN', 'MT-DOS', 'MT-DPM', 'MT-DVM', 'MT-MDR',
'MT-MWF', 'MT-NPR', 'MT-ODR', 'MT-PAS', 'MT-RPH', 'MT-UNK', 'NC-APN', 'NC-CNA',
'NC-CNM', 'NC-CNS', 'NC-DCH', 'NC-DEN', 'NC-DOS', 'NC-DPM', 'NC-DVM', 'NC-MDR',
'NC-MWF', 'NC-NPR', 'NC-ODR', 'NC-PAS', 'NC-RPH', 'NC-UNK', 'ND-APN', 'ND-CNA',
'ND-CNM', 'ND-CNS', 'ND-DCH', 'ND-DEN', 'ND-DOS', 'ND-DPM', 'ND-DVM', 'ND-MDR',
'ND-MWF', 'ND-NPR', 'ND-ODR', 'ND-PAS', 'ND-RPH', 'ND-UNK', 'NE-APN', 'NE-CNA',
'NE-CNM', 'NE-CNS', 'NE-DCH', 'NE-DEN', 'NE-DOS', 'NE-DPM', 'NE-DVM', 'NE-MDR',
'NE-MWF', 'NE-NPR', 'NE-ODR', 'NE-PAS', 'NE-RPH', 'NE-UNK', 'NH-APN', 'NH-CNA',
'NH-CNM', 'NH-CNS', 'NH-DCH', 'NH-DEN', 'NH-DOS', 'NH-DPM', 'NH-DVM', 'NH-MDR',
'NH-MWF', 'NH-NPR', 'NH-ODR', 'NH-PAS', 'NH-RPH', 'NH-UNK', 'NJ-APN', 'NJ-CNA',
'NJ-CNM', 'NJ-CNS', 'NJ-DCH', 'NJ-DEN', 'NJ-DOS', 'NJ-DPM', 'NJ-DVM', 'NJ-MDR',
'NJ-MWF', 'NJ-NPR', 'NJ-ODR', 'NJ-PAS', 'NJ-RPH', 'NJ-UNK', 'NM-APN', 'NM-CNA',
'NM-CNM', 'NM-CNS', 'NM-DCH', 'NM-DEN', 'NM-DOS', 'NM-DPM', 'NM-DVM', 'NM-MDR',
'NM-MWF', 'NM-NPR', 'NM-ODR', 'NM-PAS', 'NM-RPH', 'NM-UNK', 'NV-APN', 'NV-CNA',
'NV-CNM', 'NV-CNS', 'NV-DCH', 'NV-DEN', 'NV-DOS', 'NV-DPM', 'NV-DVM', 'NV-MDR',
'NV-MWF', 'NV-NPR', 'NV-ODR', 'NV-PAS', 'NV-RPH', 'NV-UNK', 'NY-APN', 'NY-CNA',
'NY-CNM', 'NY-CNS', 'NY-DCH', 'NY-DEN', 'NY-DPM', 'NY-DVM', 'NY-MDU', 'NY-MWF',
'NY-NPR', 'NY-ODR', 'NY-PAS', 'NY-RPH', 'NY-UNK', 'OH-APN', 'OH-CNA', 'OH-CNM',
'OH-CNS', 'OH-DCH', 'OH-DEN', 'OH-DOS', 'OH-DPM', 'OH-DVM', 'OH-MDR', 'OH-MWF',
'OH-NPR', 'OH-ODR', 'OH-PAS', 'OH-RPH', 'OH-UNK', 'OK-APN', 'OK-CNA', 'OK-CNM',
'OK-CNS', 'OK-DCH', 'OK-DEN', 'OK-DOS', 'OK-DPM', 'OK-DVM', 'OK-MDR', 'OK-MWF',
'OK-NPR', 'OK-ODR', 'OK-PAS', 'OK-RPH', 'OK-UNK', 'OR-APN', 'OR-CNA', 'OR-CNM',
'OR-CNS', 'OR-DCH', 'OR-DEN', 'OR-DOS', 'OR-DPM', 'OR-DVM', 'OR-MDR', 'OR-MWF',
'OR-NPR', 'OR-ODR', 'OR-PAS', 'OR-RPH', 'OR-UNK', 'PA-APN', 'PA-CNA', 'PA-CNM',
'PA-CNS', 'PA-DCH', 'PA-DEN', 'PA-DOS', 'PA-DPM', 'PA-DVM', 'PA-MDR', 'PA-MWF',
'PA-NPR', 'PA-ODR', 'PA-PAS', 'PA-RPH', 'PA-UNK', 'PR-APN', 'PR-CNA', 'PR-CNM',
'PR-CNS', 'PR-DCH', 'PR-DEN', 'PR-DPM', 'PR-DVM', 'PR-MDU', 'PR-MWF', 'PR-NPR',
'PR-ODR', 'PR-PAS', 'PR-RPH', 'PR-UNK', 'PW-UNK', 'RI-APN', 'RI-CNA', 'RI-CNM',
'RI-CNS', 'RI-DCH', 'RI-DEN', 'RI-DOS', 'RI-DPM', 'RI-DVM', 'RI-MDR', 'RI-MWF',
'RI-NPR', 'RI-ODR', 'RI-PAS', 'RI-RPH', 'RI-UNK', 'SC-APN', 'SC-CNA', 'SC-CNM',
'SC-CNS', 'SC-DCH', 'SC-DEN', 'SC-DOS', 'SC-DPM', 'SC-DVM', 'SC-MDR', 'SC-MWF',
'SC-NPR', 'SC-ODR', 'SC-PAS', 'SC-RPH', 'SC-UNK', 'SD-APN', 'SD-CNA', 'SD-CNM',
'SD-CNS', 'SD-DCH', 'SD-DEN', 'SD-DOS', 'SD-DPM', 'SD-DVM', 'SD-MDR', 'SD-MWF',
'SD-NPR', 'SD-ODR', 'SD-PAS', 'SD-RPH', 'SD-UNK', 'TN-APN', 'TN-CNA', 'TN-CNM',
'TN-CNS', 'TN-DCH', 'TN-DEN', 'TN-DOS', 'TN-DPM', 'TN-DVM', 'TN-MDR', 'TN-MWF',
'TN-NPR', 'TN-ODR', 'TN-PAS', 'TN-RPH', 'TN-UNK', 'TX-APN', 'TX-CNA', 'TX-CNM',
'TX-CNS', 'TX-DCH', 'TX-DEN', 'TX-DOS', 'TX-DPM', 'TX-DVM', 'TX-MDR', 'TX-MWF',
'TX-NPR', 'TX-ODR', 'TX-PAS', 'TX-RPH', 'TX-UNK', 'UT-APN', 'UT-CNA', 'UT-CNM',
'UT-CNS', 'UT-DCH', 'UT-DEN', 'UT-DOS', 'UT-DPM', 'UT-DVM', 'UT-MDR', 'UT-MWF',
'UT-NPR', 'UT-ODR', 'UT-PAS', 'UT-RPH', 'UT-UNK', 'VA-APN', 'VA-CNA', 'VA-CNM',
'VA-CNS', 'VA-DCH', 'VA-DEN', 'VA-DOS', 'VA-DPM', 'VA-DVM', 'VA-MDR', 'VA-MWF',
'VA-NPR', 'VA-ODR', 'VA-PAS', 'VA-RPH', 'VA-UNK', 'VI-APN', 'VI-CNA', 'VI-CNM',
'VI-CNS', 'VI-DCH', 'VI-DEN', 'VI-DOS', 'VI-DPM', 'VI-DVM', 'VI-MDR', 'VI-MWF',
'VI-NPR', 'VI-ODR', 'VI-PAS', 'VI-RPH', 'VI-UNK', 'VT-APN', 'VT-CNA', 'VT-CNM',
'VT-CNS', 'VT-DCH', 'VT-DEN', 'VT-DOS', 'VT-DPM', 'VT-DVM', 'VT-MDR', 'VT-MWF',
'VT-NPR', 'VT-ODR', 'VT-PAS', 'VT-RPH', 'VT-UNK', 'WA-APN', 'WA-CNA', 'WA-CNM',
'WA-CNS', 'WA-DCH', 'WA-DEN', 'WA-DOS', 'WA-DPM', 'WA-DVM', 'WA-MDR', 'WA-MWF',
'WA-NPR', 'WA-ODR', 'WA-PAS', 'WA-RPH', 'WA-UNK', 'WI-APN', 'WI-CNA', 'WI-CNM',
'WI-CNS', 'WI-DCH', 'WI-DEN', 'WI-DOS', 'WI-DPM', 'WI-DVM', 'WI-MDR', 'WI-MWF',
'WI-NPR', 'WI-ODR', 'WI-PAS', 'WI-RPH', 'WI-UNK', 'WV-APN', 'WV-CNA', 'WV-CNM',
'WV-CNS', 'WV-DCH', 'WV-DEN', 'WV-DOS', 'WV-DPM', 'WV-DVM', 'WV-MDR', 'WV-MWF',
'WV-NPR', 'WV-ODR', 'WV-PAS', 'WV-RPH', 'WV-UNK', 'WY-APN', 'WY-CNA', 'WY-CNM',
'WY-CNS', 'WY-DCH', 'WY-DEN')

ADDRESS_PURPOSE = ("LOCATION", "MAILING", "MEDREC-STORAGE",     
                "1099","REVALIDATION", "ADDITIONAL-LOCATION",
                "REMITTANCE", "TELEMEDICINE")

ADDRESS_TYPE = ('DOM', 'MIL', 'FGN')

STATES = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC', 'FL',
                    'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME',
                    'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH',
                    'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI',
                    'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI',
                    'WY', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI', 'ZZ')

COUNTRIES = ('AF', 'AX', 'AL', 'DZ', 'AS',
                    'AD', 'AO', 'AI', 'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT',
                    'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE', 'BZ', 'BJ', 'BM',
                    'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG',
                    'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL',
                    'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI',
                    'HR', 'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC',
                    'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 
                    'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI',
                    'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY',
                    'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID', 'IR',
                    'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ',
                    'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS',
                    'LR', 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY',
                    'MV', 'ML', 'MT', 'MH', 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM',
                    'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ', 'MM', 'NA', 'NR',
                    'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP',
                    'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH',
                    'PN', 'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL',
                    'SH', 'KN', 'LC', 'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA',
                    'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB', 'SO',
                    'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE',
                    'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO',
                    'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB',
                    'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF',
                    'EH', 'YE', 'ZM', 'ZW')

TAXONOMY_CODES =('347E00000X','347D00000X','344600000X','343800000X','347C00000X','343900000X',
                 '3418M1130X','3418M1110X','3418M1120X','341800000X','347B00000X','3416S0300X',
                 '3416L0300X','3416A0800X','341600000X','344800000X','335E00000X','335V00000X',
                 '3336S0011X','3336N0007X','3336M0003X','3336M0002X','3336L0003X','3336I0012X',
                 '3336H0001X','3336C0004X','3336C0003X','3336C0002X','333600000X','335U00000X',
                 '332900000X','332000000X','332800000X','332U00000X','332S00000X','332H00000X',
                 '332G00000X','333300000X','332BP3500X','332BX2000X','332BN1400X','332BD1200X',
                 '332BC3200X','332B00000X','332100000X','331L00000X','Suppliers','385HR2065X',
                 '385HR2060X','385HR2055X','385HR2050X','385H00000X','3245S0500X','324500000X',
                 '320700000X','320600000X','322D00000X','323P00000X','320900000X','320800000X',
                 '177F00000X','3140N1450X','314000000X','313M00000X','315P00000X','310500000X',
                 '315D00000X','311ZA0620X','311Z00000X','317400000X','3104A0625X','3104A0630X',
                 '310400000X','311500000X','305R00000X','305S00000X','302R00000X','302F00000X',
                 '293D00000X','291900000X','292200000X','291U00000X','284300000X','282J00000X',
                 '283XC2000X','283X00000X','283Q00000X','2865X1600X','2865M2000X','2865C1500X',
                 '286500000X','282E00000X','282NW0100X','282NR1301X','282NC0060X','282NC2000X',
                 '282N00000X','281PC2000X','281P00000X','287300000X','276400000X','273Y00000X',
                 '273R00000X','275N00000X','273100000X','261QV0200X','261QU0200X','261QS1000X',
                 '261QS1200X','261QR1300X','261QR1100X','261QR0405X','261QR0401X','261QR0404X',
                 '261QR0400X','261QR0800X','261QR0207X','261QR0208X','261QR0206X','261QR0200X',
                 '261QP0905X','261QP0904X','261QP2400X','261QP2300X','261QP1100X','261QP2000X',
                 '261QP3300X','261QS0112X','261QS0132X','261QX0203X','261QX0200X','261QX0100X',
                 '261QM1300X','261QM1100X','261QM1102X','261QM1101X','261QM1103X','261QM1000X',
                 '261QM2800X','261QM0801X','261QM3000X','261QM2500X','261QM1200X','261QL0400X',
                 '261QI0500X','261QH0700X','261QH0100X','261QG0250X','261QF0400X','261QF0050X',
                 '261QE0700X','261QE0800X','261QE0002X','261QD1600X','261QD0000X','261QC0050X',
                 '261QC1800X','261QC1500X','261QB0400X','261QA3000X','261QA0900X','261QA1903X',
                 '261QA0006X','261QA0005X','261QM0850X','261QA0600X','261QM0855X','261Q00000X',
                 '251V00000X','251X00000X','251K00000X','251T00000X','251J00000X','253Z00000X',
                 '251G00000X','251F00000X','251E00000X','253J00000X','252Y00000X','251C00000X',
                 '251S00000X','251B00000X','251300000X','246RP1900X','246RM2200X','246RH0600X',
                 '247ZC0005X','246R00000X','2472V0600X','2472R0900X','2472E0500X','2472D0500X',
                 '2472B0301X','247200000X','2470A2800X','247000000X','246W00000X','246QM0900X',
                 '246QM0706X','246QL0901X','246QL0900X','246QI0000X','246QH0600X','246QH0000X',
                 '246QH0401X','246QC2700X','246QC1000X','246QB0000X','246Q00000X','246ZS0400X',
                 '246ZN0300X','246ZI1000X','246ZG0701X','246ZG1000X','246ZE0600X','246ZE0500X',
                 '246ZC0007X','246ZB0600X','246ZB0302X','246ZB0301X','246ZB0500X','246ZA2600X',
                 '246Z00000X','246YR1600X','246YC3302X','246YC3301X','246Y00000X','246XC2903X',
                 '246XS1301X','246XC2901X','246X00000X','243U00000X','2471V0106X','2471V0105X',
                 '2471S1302X','2471C3402X','2471R0002X','2471Q0001X','2471N0900X','2471M2300X',
                 '2471M1202X','2471C3401X','2471C1101X','2471C1106X','2471B0102X','247100000X',
                 '242T00000X','390200000X','235Z00000X','2355S0801X','2355A2700X','235500000X',
                 '237700000X','237600000X','231HA2500X','231HA2400X','231H00000X','2255R0406X',
                 '2255A2300X','225500000X','2279S1500X','2279P1005X','2279P1006X','2279P1004X',
                 '2279P4000X','2279P3800X','2279P3900X','2279H0200X','2279G0305X','2279G1100X',
                 '2279E0002X','2279E1000X','2279C0205X','227900000X','2278S1500X','2278P1005X',
                 '2278P1006X','2278P1004X','2278P4000X','2278P3800X','2278P3900X','2278H0200X',
                 '2278G0305X','2278G1100X','2278E0002X','2278E1000X','2278C0205X','227800000X',
                 '225400000X','225CX0006X','225CA2500X','225CA2400X','225C00000X','225800000X',
                 '225B00000X','224P00000X','225200000X','2251S0007X','2251P0200X','2251X0800X',
                 '2251N0400X','2251H1300X','2251H1200X','2251G0304X','2251E1200X','2251E1300X',
                 '2251C2600X','225100000X','222Z00000X','225000000X','224ZL0004X','224ZF0002X',
                 '224ZE0001X','224ZR0403X','224Z00000X','225XP0019X','225XP0200X','225XN1300X',
                 '225XM0800X','225XL0004X','225XH1300X','225XH1200X','225XG0600X','225XF0002X',
                 '225XE1200X','225XE0001X','225XR0403X','225X00000X','225A00000X','225700000X',
                 '226300000X','222Q00000X','225600000X','221700000X','229N00000X','213ES0000X',
                 '213ER0200X','213EP0504X','213EP1101X','213EG0000X','213ES0131X','213ES0103X',
                 '213E00000X','211D00000X','363AS0400X','363AM0700X','363A00000X','363LW0102X',
                 '363LS0200X','363LP0808X','363LP2300X','363LP1700X','363LP0222X','363LP0200X',
                 '363LX0106X','363LX0001X','363LN0005X','363LN0000X','363LG0600X','363LF0000X',
                 '363LC0200X','363LC1500X','363LA2200X','363LA2100X','363L00000X','367500000X',
                 '364SW0102X','364ST0500X','364SS0200X','364SR0400X','364SP0813X','364SP0812X',
                 '364SP0811X','364SP0810X','364SP0807X','364SP0809X','364SP0808X','364SP2800X',
                 '364SP1700X','364SP0200X','364SX0204X','364SX0200X','364SX0106X','364SN0800X',
                 '364SN0000X','364SM0705X','364SL0600X','364SI0800X','364SH0200X','364SH1100X',
                 '364SG0600X','364SF0001X','364SE1400X','364SE0003X','364SC0200X','364SC1501X',
                 '364SC2300X','364SA2200X','364SA2100X','364S00000X','367H00000X','367A00000X',
                 '183700000X','1835P1300X','1835P1200X','1835P0018X','1835X0200X','1835N1003X',
                 '1835N0905X','1835G0303X','1835G0000X','183500000X','174MM1900X','174M00000X',
                 '1744R1102X','1744R1103X','1744P3200X','1744G0900X','174400000X','173F00000X',
                 '173C00000X','175F00000X','172P00000X','1710I1003X','1710I1002X','171000000X',
                 '175M00000X','176B00000X','170100000X','172M00000X','173000000X','171R00000X',
                 '175L00000X','174H00000X','170300000X','176P00000X','172A00000X','171WV0202X',
                 '171WH0202X','171W00000X','172V00000X','171M00000X','171100000X','3747P1801X',
                 '3747A0650X','374700000X','374K00000X','374T00000X','376G00000X','376K00000X',
                 '376J00000X','374U00000X','374J00000X','373H00000X','372500000X','372600000X',
                 '163WW0000X','163WW0101X','163WU0100X','163WS0200X','163WR1000X','163WR0400X',
                 '163WR0006X','163WP0807X','163WP0809X','163WP0808X','163WS0121X','163WP1700X',
                 '163WP0200X','163WP0218X','163WP0000X','163WX0601X','163WX1500X','163WX0800X',
                 '163WX1100X','163WX0200X','163WX0106X','163WX0003X','163WX0002X','163WN1003X',
                 '163WM1400X','163WN0800X','163WN0300X','163WN0003X','163WN0002X','163WM0705X',
                 '163WM0102X','163WL0100X','163WI0500X','163WI0600X','163WH1000X','163WH0200X',
                 '163WH0500X','163WG0600X','163WG0000X','163WG0100X','163WF0300X','163WE0900X',
                 '163WE0003X','163WD1100X','163WD0400X','163WC0200X','163WC1600X','163WC2100X',
                 '163WC1500X','163WC1400X','163WC0400X','163WC3500X','163WP2201X','163WA2000X',
                 '163WA0400X','163W00000X','164X00000X','167G00000X','164W00000X','156FX1900X',
                 '156FX1202X','156FX1201X','156FX1800X','156FX1101X','156FX1100X','156FX1700X',
                 '156FC0801X','156FC0800X','156F00000X','152WV0400X','152WS0006X','152WP0200X',
                 '152WX0102X','152WL0500X','152WC0802X','152W00000X','146D00000X','146L00000X',
                 '146M00000X','146N00000X','133NN1002X','133N00000X','133VN1005X','133VN1004X',
                 '133VN1006X','133V00000X','136A00000X','132700000X','122400000X','1223P0700X',
                 '1223P0300X','1223P0221X','1223X0400X','1223S0112X','1223X0008X','1223P0106X',
                 '1223G0001X','1223E0200X','1223D0001X','122300000X','126900000X','124Q00000X',
                 '126800000X','111NT0100X','111NS0005X','111NR0400X','111NR0200X','111NP0017X',
                 '111NX0800X','111NX0100X','111NN1001X','111NN0400X','111NI0900X','111NI0013X',
                 '111N00000X','1041S0200X','1041C0700X','104100000X','103TW0100X','103TS0200X',
                 '103TR0400X','103TP2700X','103TP0814X','103TP0016X','103TM1800X','103TM1700X',
                 '103TH0100X','103TH0004X','103TP2701X','103TF0200X','103TF0000X','103TE1100X',
                 '103TE1000X','103TC1900X','103TB0200X','103TC2200X','103TC0700X','103TA0700X',
                 '103TA0400X','103T00000X','102L00000X','102X00000X','106H00000X','101YS0200X',
                 '101YP2500X','101YP1600X','101YM0800X','101YA0400X','101Y00000X','103GC0700X',
                 '103G00000X','103K00000X','2088P0231X','208800000X','204F00000X','208G00000X',
                 '2086S0129X','2086S0127X','2086X0206X','2086S0102X','2086S0105X','2086S0122X',
                 '2086S0120X','2086H0002X','208600000X','2085R0204X','2085R0203X','2085R0205X',
                 '2085R0001X','2085P0229X','2085N0904X','2085N0700X','2085H0002X','2085U0001X',
                 '2085R0202X','2085D0003X','2085B0100X','208VP0000X','208VP0014X','2084V0102X',
                 '2084S0010X','2084S0012X','2084P0015X','2084P0800X','2084P2900X','2084N0008X',
                 '2084N0402X','2084N0400X','2084P0005X','2084H0002X','2084P0805X','2084F0202X',
                 '2084D0003X','2084N0600X','2084P0804X','2084B0002X','2084P0802X','2084A0401X',
                 '2083P0011X','2083S0010X','2083P0901X','2083P0500X','2083X0100X','2083T0002X',
                 '2083A0100X','2082S0105X','2082S0099X','208200000X','2081S0010X','2081P0004X',
                 '2081P0010X','2081P2900X','2081N0008X','2081H0002X','208100000X','202K00000X',
                 '2080S0010X','2080S0012X','2080T0004X','2080P0216X','2080P0214X','2080P0210X',
                 '2080P0208X','2080P0207X','2080P0206X','2080P0205X','2080P0204X','2080P0203X',
                 '2080P0202X','2080P0201X','2080P0008X','2080N0001X','2080T0002X','2080H0002X',
                 '2080P0006X','2080I0007X','2080C0008X','2080A0000X','208000000X','207ZP0213X',
                 '207ZN0500X','207ZP0007X','207ZM0300X','207ZI0100X','207ZH0000X','207ZF0201X',
                 '207ZD0900X','207ZC0500X','207ZP0105X','207ZC0006X','207ZP0104X','207ZB0001X',
                 '207ZP0102X','207ZP0101X','207YS0012X','207YX0007X','207YP0228X',
                 '207YX0901X','207YX0905X','207YX0602X','207YS0123X','207Y00000X','207XX0005X',
                 '207XP3100X','207XX0801X','207XS0117X','207XS0106X','207XX0004X','207XS0114X',
                 '207X00000X','204E00000X','207W00000X','207VE0102X','207VX0000X','207VM0101X',
                 '207VH0002X','207VG0400X','207VX0201X','207VC0200X','207VB0002X','207V00000X',
                 '204C00000X','204D00000X','207UN0902X','207UN0901X','207UN0903X','207U00000X',
                 '207T00000X','207SG0205X','207SM0001X','207SG0203X','207SG0201X','207SC0300X',
                 '207SG0202X','209800000X','207RT0003X','207RS0010X','207RS0012X','207RR0500X',
                 '207RP1001X','207RN0300X','207RX0202X','207RM1200X','207RI0011X','207RI0200X',
                 '207RH0002X','207RI0008X','207RH0003X','207RH0000X','207RG0300X','207RG0100X',
                 '207RE0101X','207RC0200X','207RC0001X','207RI0001X','207RC0000X','207RB0002X',
                 '207RA0201X','207RA0000X','207RA0401X','207R00000X','202C00000X','208M00000X',
                 '208D00000X','207QS0010X','207QS1201X','207QH0002X','207QG0300X','207QB0002X',
                 '207QA0505X','207QA0000X','207QA0401X','207Q00000X','207PE0005X','207PS0010X',
                 '207PP0204X','207PT0002X','207PH0002X','207PE0004X','207P00000X','207NS0135X',
                 '207NP0225X','207ND0101X','207ND0900X','207NI0002X','207N00000X','208C00000X',
                 '208U00000X','207LP3000X','207LP2900X','207LH0002X','207LC0200X','207LA0401X',
                 '207L00000X','207KI0005X','207KA0200X','207K00000X','193400000X','193200000X')