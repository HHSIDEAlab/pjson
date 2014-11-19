ProviderJSON
============

0.0.22


Quick Installation of Reference Implementation
==============================================

A validation library(Python) and command line tool for validating ProviderJSON
is contained in this repository.  The easiest way to install it is using `pip`.
Open a terminal window and type:


    sudo pip install providerjson


Test it using the command line tool on Unixlike systems:


    validate-pjson sample.json
    
    
On Windows it will be something like:


    python c:\Python27\Scrips\validate-pjson sample.json


This will return a JSON object with arrays of errors and warnings. A clean record would
look like this.

    {
        "errors": [], 
        "warnings": []
    }



You can also use it in you own code like so:


    python
    >>> from pjson.validate_pjson import validate_pjson
    >>> validate_pjson('{"number": "12345"}')
    >>> {'errors': ['The JSON object does not contain an enumeration_type.'], 'warnings': []}
    >>>



ProviderJSON Format Definition
==============================

ProviderJSON is a JSON object format for US health care providers. 
It is based on fields currently collected to receive or maintain 
a National Provider Identifier (or NPI). ProviderJSON is the basis for 
the NPPES National Plan and Provider Enumeration System (NPPES) write API.
Here is a high-level pseudo-code example:


    {
        "enumeration_type"           : "NPI-1",
        "number"                     : 114283205,
        "last_updated_epoch"         : 1409675065,
        "created_epoch"              : 1409663451,
        "basic"                      : {...},
        "other_names"                : [...],
        "addresses"                  : [...],
        "taxonomies"                 : [... ],
        "licenses"                   : [...],
        "identifiers"                : [...],
        "specialties"                : [...],
        "direct_addresses"           : [...],
        .
        .
        .
    }

The ProviderJSON object contains several top-level items.
The `enumeration_type` acts a switch determining what is required and what is
not. The `number` component contains a string of the enumeration number.
`classification` is used when submitting this informartion via API to indicate
whether the request is for a new enumeration or a change request.
`basic` is an object that contains basic demographic information (e.g. name,
contact person, etc.). `addresses` contains an array of provider address objects.
`taxonomies` is an array of taxonomy classification objects,`licenses` contains
an array of license information. `identifiers` contains an array of other
identifier objects. `specialities` contains an array of provider specalitt
objects. `direct-addresses` contain an array of Direct email address objects.
Each of these main components are described in detail in the sections below.
Much of the information is optional or is only required in specific
circumstances. It is possibile to add additional infformation to this document
so long as the additional items do not confilict with the fields defined here.
It is the hope that other componets can be defined over time so that all provider
information can be represented here.

Enumeration Type
----------------

The `enumeration_type` is required and shall be one of these four values.


* NPI-1 - An individual (human) provider.
* NPI-2 - An provider (legal entity) organization.
* OEID  - An individual "other entitiy" provider (a human being).
* HPID  - A health plan identifier.



Number
------

The `number` is the assigned enumeration number (e.g. an NPI). This integer
field should be left blank when submitting a new enumeration request, but
must be provided on change requests. Number is always length 9 where 
the  last number is a checkdigit according to the Luhn algorithm. 
Please refer to the NPI final rule for more infromation.


Last Updated Epoch
-------------------

The `last_updated_epoch` is an integer of  the Unix epoch for the last update 
to the enumeration. 
A Unix epoch (or Unix time or POSIX time or Unix timestamp) is the number 
of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), 
not counting leap seconds (in ISO8601: 1970-01-01T00:00:00Z).


Created Epoch
-------------

The `created_epoch` is an integer of  the Unix epoch for the creation of the enumeration.
A Unx epoch (or Unix time or POSIX time or Unix timestamp) is the number 
of seconds that have elapsed since January 1, 1970 (midnight UTC/GMT), 
not counting leap seconds (in ISO8601: 1970-01-01T00:00:00Z).



Requirements for National Plan Identifer Type I Individual (NPI-1)
------------------------------------------------------------------

* basic - name, contact person etc.
* licenses - at least 1 license or certification
* taxonomies - at least one and one should be marked as primary.
* addresses - Exactly one mailing addrress.  Exactly one primary practice location.

Requirements for National Plan Identifer Type II Entity (NPI-2)
---------------------------------------------------------------


* basic - name, contact person etc.
* taxonomies - at least one and one should be marked as primary.
* addresses - Exactly one mailing addrress.  Exactly one primary practice location.

Requirements for Other Entitiy Identifier (OEID)
------------------------------------------------

* basic - name, contact person etc.
* taxonomies - at least one and one should be marked as primary.

Requirements for a Health Plan Identifier (HPID)
------------------------------------------------

* basic - name, contact person etc.
* taxonomies - at least one and one should be marked as primary.


Basic (basic object)
--------------------

`basic` contains an object (`{}`) of basic demographic inforation that is not
repeated.  The information is based on the NPI final rule, but includes some
optional information.

These are as follows:
<table>
 <tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

  <tr>
   <td>name_prefix</td>
   <td>5</td>
   <td>N</td>
   <td>Choices must be in ['Ms.', 'Mr.', 'Miss', 'Mrs.', 'Dr.', 'Prof.'].
   Required for NPI-1
   </td>
 </tr>

 <tr>
   <td>first_name</td>
   <td>150</td>
   <td>N</td>
   <td>Required for NPI-1</td>
 </tr>


 <tr>
   <td>last_name</td>
   <td>150</td>
   <td>S</td>
   <td>Required for NPI-1</td>
 </tr>


 <tr>
   <td>middle_name</td>
   <td>150</td>
   <td>N</td>
   <td>Applies only to NPI-1.</td>
 </tr>


 <tr>
   <td>name_suffix</td>
   <td>4</td>
   <td>N</td>
   <td>Choices must be in ['Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII',
       'VIII', 'IX', 'X']. Applies only to NPI-1.</td>
 </tr>


 <tr>
   <td>credential</td>
   <td>50</td>
   <td>N</td>
   <td>Applies only to NPI-1.</td>
 </tr>


 <tr>
   <td>sole_proprietor</td>
   <td>3</td>
   <td>N</td>
   <td>Applies only to NPI-1. Choices must be in ['YES', 'NO']. .</td>
 </tr>



 <tr>
   <td>organizational_subpart</td>
   <td>Boolean</td>
   <td>S</td>
   <td>Applies only to NPI-2. true or false.</td>
 </tr>


 <tr>
   <td>ssn</td>
   <td>9</td>
   <td>S</td>
   <td>Required for NPI-1 if no itin is provided.</td>
 </tr>


 <tr>
   <td>ein</td>
   <td>9</td>
   <td>S</td>
   <td>Required for NPI-2.</td>
 </tr>


 <tr>
   <td>itin</td>
   <td>9</td>
   <td>S</td>
   <td>Required for NPI-1 if no ssn is provided.</td>
 </tr>


 <tr>
   <td>gender</td>
   <td>1</td>
   <td>S</td>
   <td>Required for NPI-1. Choices must be in ['F', 'M'].</td>
 </tr>


 <tr>
   <td>date_of_birth</td>
   <td>10</td>
   <td>S</td>
   <td>Required for NPI-1. Format must be YYYY-MM-DD.</td>
 </tr>

 <tr>
   <td>state_of_birth</td>
   <td>2</td>
   <td>S</td>
   <td>Required for NPI-1. Choices must be in ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'DC',
   'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA',
   'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND',
   'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA',
   'WV', 'WI', 'WY', 'AS', 'FM', 'GU', 'MH', 'MP', 'PR', 'PW', 'VI', 'ZZ'].</td>
 </tr>


 <tr>
   <td>country_of_birth</td>
   <td>2</td>
   <td>S</td>
   <td>Applies to NPI-1.Choices must be in ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI', 'AQ',
   'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB', 'BY', 'BE',
   'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR', 'IO', 'BN', 'BG',
   'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD', 'CL', 'CN', 'CX', 'CC',
   'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR', 'CU', 'CW', 'CY', 'CZ', 'DK',
   'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ', 'ER', 'EE', 'ET', 'FK', 'FO', 'FJ',
   'FI', 'FR', 'GF', 'PF', 'TF', 'GA', 'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL',
   'GD', 'GP', 'GU', 'GT', 'GG', 'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK',
   'HU', 'IS', 'IN', 'ID', 'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE',
 'JO', 'KZ', 'KE', 'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR',
 'LY', 'LI', 'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH',
 'MQ', 'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ',
 'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF', 'MP',
 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN', 'PL', 'PT',
 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC', 'MF', 'PM', 'VC',
 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG', 'SX', 'SK', 'SI', 'SB',
 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR', 'SJ', 'SZ', 'SE', 'CH', 'SY',
 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK', 'TO', 'TT', 'TN', 'TR', 'TM', 'TC',
 'TV', 'UG', 'UA', 'AE', 'GB', 'US', 'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG',
 'VI', 'WF', 'EH', 'YE', 'ZM', 'ZW'].</td>
 </tr>



 <tr>
   <td>initial_enumeration_date</td>
   <td>10</td>
   <td>N</td>
   <td>Must be in YYYY-MM-DD format. This value is system generated. Value is
   same as enumeration_date unless record has been deactivated and reactivated.</td>
 </tr>


 <tr>
   <td>enumeration_date</td>
   <td>10</td>
   <td>N</td>
   <td>Must be in YYYY-MM-DD format. This value is system generated.</td>
 </tr>


 <tr>
   <td>last_updated</td>
   <td>10</td>
   <td>N</td>
   <td>Must be in YYYY-MM-DD format. This value is system generated.</td>
 </tr>


 <tr>
   <td>date_of_death</td>
   <td>10</td>
   <td>N</td>
   <td>Date of death. System generated from SSA. Must be in YYYY-MM-DD format.</td>
 </tr>


<tr>
   <td>reactivation_date</td>
   <td>10</td>
   <td>N</td>
   <td>Date of reactivation. Must be in YYYY-MM-DD format.</td>
 </tr>


 <tr>
   <td>mode</td>
   <td>1</td>
   <td>N</td>
   <td> System generated. Choices must be in ['(W)eb', '(P)aper', '(E)FI',  '(A)PI']. Should always be 'A' when using the API and 'W' when using the web interface.
   </td>
 </tr>


 <tr>
   <td>status</td>
   <td>1</td>
   <td>N</td>
   <td>Choices must be in ['E(diting)', 'P(ending)', '(A)ctive', '(D)eactive', '(R)evoked']. System generated.</td>
 </tr>


 <tr>
   <td>contact_method</td>
   <td>1</td>
   <td>N</td>
   <td>Defaults to email. Choices must be in ['(E)mail', '(M)ail'].</td>
 </tr>


 <tr>
   <td>deactivated_details</td>
   <td>1000</td>
   <td>N</td>
   <td>Optional details concering deactivation. Deacesed etc. This information is for the Enuemrator only.</td>
 </tr>


 <tr>
   <td>deactivation_date</td>
   <td>10</td>
   <td>N</td>
   <td>Deactivation Date. System generated. Format must be YYYY-MM-DD.</td>
 </tr>


 <tr>
   <td>deactivation_reason_code</td>
   <td>2</td>
   <td>N</td>
   <td>Choices must be in ['', 'DT', 'DB', 'FR', 'OT']. System generated.</td>
 </tr>


 <tr>
   <td>deactivation_note</td>
   <td>1024</td>
   <td>N</td>
   <td>Optional deactivation note.  This information is for the Enuemrator only.</td>
 </tr>


 <tr>
   <td>deceased_notes</td>
   <td>1000</td>
   <td>N</td>
   <td>Optional deceased notes. This information is for the Enuemrator only</td>
 </tr>



 <tr>
   <td>parent_organization_ein</td>
   <td>Boolean</td>
   <td>N</td>
   <td>'true or 'false'.Applies only to NPI-2. A parent organization tax id.</td>
 </tr>

 <tr>
   <td>parent_organization_ein</td>
   <td>9</td>
   <td>S</td>
   <td>A parent organization tax id. Applies only to NPI-2. Required when subpart is true.</td>
 </tr>


 <tr>
   <td>parent_organization_legal_business_name</td>
   <td>300</td>
   <td>S</td>
   <td>Applies only to NPI-2. A parent organization's legal business name. Required when subpart is true.</td>
 </tr>


 <tr>
   <td>reactivation_note</td>
   <td>1024</td>
   <td>N</td>
   <td>Note on reactivation</td>
 </tr>


 <tr>
   <td>comments</td>
   <td>1024</td>
   <td>N</td>
   <td>Used only by the enuemerator and cannot be submitted or returned in API results./td>
 </tr>


 <tr>
   <td>authorized_official_credential</td>
   <td>20</td>
   <td>N</td>
   <td>Applies only to NPI-2.</td>
 </tr>


 <tr>
   <td>authorized_official_email</td>
   <td>75</td>
   <td>N</td>
   <td>Applies only to NPI-2.</td>
 </tr>


 <tr>
   <td>authorized_official_first_name</td>
   <td>150</td>
   <td>S</td>
   <td>Required for NPI-2.</td>
 </tr>


 <tr>
   <td>authorized_official_last_name</td>
   <td>150</td>
   <td>S</td>
   <td>Required for NPI-2.</td>
 </tr>


 <tr>
   <td>authorized_official_middle_name</td>
   <td>150</td>
   <td>N</td>
   <td>Applies only to NPI-2.</td>
 </tr>


 <tr>
   <td>authorized_official_prefix</td>
   <td>10</td>
   <td>N</td>
   <td>Choices must be in ['Ms.', 'Mr.', 'Miss', 'Mrs.', 'Dr.', 'Prof.'].
   Applies only to NPI-2.</td>
 </tr>


 <tr>
   <td>authorized_official_suffix</td>
   <td>4</td>
   <td>N</td>
   <td>Choices must be in ['Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'VI',
   'VII', 'VIII', 'IX', 'X']. Applies only to NPI-2.</td>
 </tr>

 <tr>
   <td>authorized_official_telephone_number</td>
   <td>10</td>
   <td>S</td>
   <td>Required for NPI-2 only.</td>
 </tr>


 <tr>
   <td>authorized_official_telephone_extension</td>
   <td>10</td>
   <td>N</td>
   <td>Applies for NPI-2 only.</td>
 </tr>


 <tr>
   <td>authorized_official_title_or_position</td>
   <td>150</td>
   <td>S</td>
   <td>Required for NPI-2.</td>
 </tr>


 <tr>
   <td>contact_person_credential</td>
   <td>20</td>
   <td>N</td>
   <td>Optional</td>
 </tr>


 <tr>
   <td>contact_person_email</td>
   <td>75</td>
   <td>Y</td>
   <td>Required if the person has an email.</td>
 </tr>

 <tr>
   <td>contact_person_prefix</td>
   <td>5</td>
   <td>N</td>
   <td>Choices must be in ['Ms.', 'Mr.', 'Miss', 'Mrs.', 'Dr.', 'Prof.'].
   Applies only to NPI-1.</td>
 </tr>

 <tr>
   <td>contact_person_first_name</td>
   <td>150</td>
   <td>Y</td>
   <td>Required for NPI-1.</td>
 </tr>

 <tr>
   <td>contact_person_last_name</td>
   <td>150</td>
   <td>Y</td>
   <td>Required.</td>
 </tr>


 <tr>
   <td>contact_person_middle_name</td>
   <td>150</td>
   <td>Y</td>
   <td>Applies only to NPI-1.</td>
 </tr>


 <tr>
   <td>contact_person_suffix</td>
   <td>4</td>
   <td>N</td>
   <td>Choices must be in ['Jr.', 'Sr.', 'I', 'II', 'III', 'IV', 'V', 'VI',
   'VII', 'VIII', 'IX', 'X'].
   Applies only to NPI-1.</td>
 </tr>


 <tr>
   <td>contact_person_telephone_number</td>
   <td>20</td>
   <td>Y</td>
   <td>Required for NPI-1 and NPI-2 if the contact person has a telephone number.
   </td>
 </tr>

 
 <tr>
   <td>contact_person_telephone_extension</td>
   <td>10</td>
   <td>N</td>
   <td></td>
 </tr>


 <tr>
   <td>contact_person_title_or_position</td>
   <td>150</td>
   <td>Y</td>
   <td></td>
 </tr>


 <tr>
   <td>website</td>
   <td>200</td>
   <td>N</td>
   <td>A website url.</td>
 </tr>


 <tr>
   <td>facebook_handle</td>
   <td>100</td>
   <td>N</td>
   <td>A facebook handle.</td>
 </tr>


 <tr>
   <td>twitter_handle</td>
   <td>100</td>
   <td>A twitter handle</td>
   <td>A twitter handle</td>
 </tr>


 <tr>
   <td>public_email</td>
   <td>75</td>
   <td>N</td>
   <td></td>
 </tr>


 <tr>
   <td>gravatar_email</td>
   <td>200</td>
   <td>N</td>
   <td>a gravatar email for displaying an avatar with a profile.</td>
 </tr>


 <tr>
   <td>driving_directions</td>
   <td>256</td>
   <td>N</td>
   <td></td>
 </tr>


 <tr>
   <td>bio_headline</td>
   <td>255</td>
   <td>N</td>
   <td></td>
 </tr>
</table>


Other Names (other_names)
-------------------------
<table>
 <tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>Type</td>
  <td>35</td>
  <td>N</td>
  <td>System generated from "code" for readability.</td>
</tr>

<tr>
  <td>code</td>
  <td>1</td>
  <td>Y</td>
  <td> Determines the type of other_name. Values must be in
  	("","Blank"),
    ("1","Former Name"),
    ("2","Professional Name"),
    ("3","Doing Business As"),
    ("4","Former Legal Business Name"),
    ("5","Other Name").<br>
    Codes "1" and "2"refer only to NPI-1. <br>
    4 refers only to NPI-2.<br>
    5 refers to NPI-1 where sole_proprietor=true and NPI-2.<br>
    Blank ("") is not accepted in the API, but may be
    encountered in legacy data.
                        </td>
</tr>

<tr>
  <td>prefix</td>
  <td>5</td>
  <td>N</td>
  <td>Applies only to NPI-1. Must be in ['Ms.'Mr.','Miss','Mrs.','Dr.','Prof.']</td>
</tr>

<tr>
  <td>suffix</td>
  <td>4</td>
  <td>N</td>
  <td>Applies only to NPI-1. Must be in ['Jr.','Sr.','I','II',                              'III','IV','V','VI','VII','VIII','IX','X']</td>
</tr>

<tr>
  <td>credential</td>
  <td>50</td>
  <td>N</td>
  <td>Refersonly to NPI-1.</td>
</tr>

<tr>
  <td>othertype</td>
  <td>50</td>
  <td>S</td>
  <td>Required when code=5.</td>
</tr>

<tr>
  <td>organization_name</td>
  <td>150</td>
  <td>S</td>
  <td>Required for NPI-2.</td>
</tr>

<tr>
  <td>first_name</td>
  <td>150</td>
  <td>S</td>
  <td>Required for NPI-1 when code is 1 or 2.</td>
</tr>

<tr>
  <td>last_name</td>
  <td>150</td>
  <td>S</td>
  <td>Required for NPI-1 when code is 1 or 2.</td>
</tr>

<tr>
  <td>middle_name</td>
  <td>150</td>
  <td>N</td>
  <td>Applies only to NPI-1 and when code is 1 or 2.</td>
</tr>


</table>


Addresses (addresses)
---------------------

<table>
 <tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>


<tr>
          <td>address_purpose</td>
          <td>20</td>
          <td>Y</td>
          <td>Choices must be in ['LOCATION', 'MAILING', 'MEDREC-STORAGE', '1099',
          'REVALIDATION', 'ADDITIONAL-LOCATION', 'REMITTANCE']</td>
</tr>
            

        <tr>
          <td>address_type</td>
          <td>12</td>
          <td>Y</td>
          <td>Choices must be in ['DOM', 'FGN', 'MIL']</td>
        </tr>
            

        <tr>
          <td>address_1</td>
          <td>200</td>
          <td>Y</td>
          <td></td>
        </tr>
            

        <tr>
          <td>address_2</td>
          <td>200</td>
          <td>N</td>
          <td></td>
        </tr>




        <tr>
          <td>city</td>
          <td>200</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>zip</td>
          <td>10</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>country_code</td>
          <td>2</td>
          <td>N</td>
          <td>Choices must be in ['AF', 'AX', 'AL', 'DZ', 'AS', 'AD', 'AO', 'AI',
          'AQ', 'AG', 'AR', 'AM', 'AW', 'AU', 'AT', 'AZ', 'BS', 'BH', 'BD', 'BB',
          'BY', 'BE', 'BZ', 'BJ', 'BM', 'BT', 'BO', 'BQ', 'BA', 'BW', 'BV', 'BR',
          'IO', 'BN', 'BG', 'BF', 'BI', 'KH', 'CM', 'CA', 'CV', 'KY', 'CF', 'TD',
          'CL', 'CN', 'CX', 'CC', 'CO', 'KM', 'CG', 'CD', 'CK', 'CR', 'CI', 'HR',
          'CU', 'CW', 'CY', 'CZ', 'DK', 'DJ', 'DM', 'DO', 'EC', 'EG', 'SV', 'GQ',
          'ER', 'EE', 'ET', 'FK', 'FO', 'FJ', 'FI', 'FR', 'GF', 'PF', 'TF', 'GA',
          'GM', 'GE', 'DE', 'GH', 'GI', 'GR', 'GL', 'GD', 'GP', 'GU', 'GT', 'GG',
          'GN', 'GW', 'GY', 'HT', 'HM', 'VA', 'HN', 'HK', 'HU', 'IS', 'IN', 'ID',
          'IR', 'IQ', 'IE', 'IM', 'IL', 'IT', 'JM', 'JP', 'JE', 'JO', 'KZ', 'KE',
          'KI', 'KP', 'KR', 'KW', 'KG', 'LA', 'LV', 'LB', 'LS', 'LR', 'LY', 'LI',
          'LT', 'LU', 'MO', 'MK', 'MG', 'MW', 'MY', 'MV', 'ML', 'MT', 'MH', 'MQ',
          'MR', 'MU', 'YT', 'MX', 'FM', 'MD', 'MC', 'MN', 'ME', 'MS', 'MA', 'MZ',
          'MM', 'NA', 'NR', 'NP', 'NL', 'NC', 'NZ', 'NI', 'NE', 'NG', 'NU', 'NF',
          'MP', 'NO', 'OM', 'PK', 'PW', 'PS', 'PA', 'PG', 'PY', 'PE', 'PH', 'PN',
          'PL', 'PT', 'PR', 'QA', 'RE', 'RO', 'RU', 'RW', 'BL', 'SH', 'KN', 'LC',
          'MF', 'PM', 'VC', 'WS', 'SM', 'ST', 'SA', 'SN', 'RS', 'SC', 'SL', 'SG',
          'SX', 'SK', 'SI', 'SB', 'SO', 'ZA', 'GS', 'SS', 'ES', 'LK', 'SD', 'SR',
          'SJ', 'SZ', 'SE', 'CH', 'SY', 'TW', 'TJ', 'TZ', 'TH', 'TL', 'TG', 'TK',
          'TO', 'TT', 'TN', 'TR', 'TM', 'TC', 'TV', 'UG', 'UA', 'AE', 'GB', 'US',
          'UM', 'UY', 'UZ', 'VU', 'VE', 'VN', 'VG', 'VI', 'WF', 'EH', 'YE', 'ZM',
          'ZW']</td>
        </tr>






        <tr>
          <td>driving_details</td>
          <td>15</td>
          <td>N</td>
          <td></td>
        </tr>
            

            

        <tr>
          <td>foreign_fax_number</td>
          <td>20</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>foreign_postal</td>
          <td>12</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>foreign_state</td>
          <td>2</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>foreign_telephone_number</td>
          <td>20</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>hours_of_operation</td>
          <td>255</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>lat</td>
          <td>20</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>long</td>
          <td>20</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>phone_number_extension</td>
          <td>15</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>private_email_contact</td>
          <td>15</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>public_email_contact</td>
          <td>15</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>rdi</td>
          <td>15</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>record_type</td>
          <td>2</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>telephone_number_extension</td>
          <td>10</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>us_fax_number</td>
          <td>12</td>
          <td>N</td>
          <td></td>
        </tr>

        <tr>
          <td>us_telephone_number</td>
          <td>20</td>
          <td>N</td>
          <td></td>
        </tr>


        <tr>
          <td>website</td>
          <td>15</td>
          <td>N</td>
          <td></td>
        </tr>

</table>


Taxonomies (taxonomies)
----------

<table>

<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>


<tr>
  <td>code</td>
  <td>50</td>
  <td>Y</td>
  <td>Choices for codes found at http://www.wpc-edi.com/taxonomy
</td>
</tr>


<tr>
  <td>primary</td>
  <td>None</td>
  <td>Y</td>
  <td>`true` if this is the primary taxonomy and `false` otherwise.
  Only one taxonomy code in the array can be flagged with primary=true.
</td>
</tr>


</table>


Licenses (licenses)
--------

<table>

<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>


<tr>
  <td>number</td>
  <td>50</td>
  <td>Y</td>
  <td>The unique number or identifier given to the license provided by
  the issuing organization. Required if codified version not given</td>
</tr>

<tr>
  <td>type</td>
  <td>3</td>
  <td>Y</td>
  <td>The license type according to https://github.com/HHSIDEAlab/mlvs/blob/master/docs/USProviderLicenseTypesFeb2014.csv</td>
</tr>


<tr>
  <td>state</td>
  <td>2</td>
  <td>Y</td>
  <td>State according to ISO 3166-2:US.</td>
</tr>


<tr>
  <td>status</td>
  <td>2<2/td>
  <td>N</td>
  <td>Defaults to UNKNOWN. This is determinied by verification by the enumerator
  and produced server side. If suplied, value must be in { "UNKNOWN", "ACTIVE",
  "ACTIVE_WITH_RESTRICTIONS", "EXPIRED", "REVOKED", "DECEASED"]

  
  Values are ""Status</td>
</tr>



</table>



Identifiers (identifiers)
-------------------------

<table>

<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>

<tr>
  <td>identifier</td>
  <td>20</td>
  <td>Y</td>
  <td>The number or code issued by the issuing body. </td>
</tr>


<tr>
  <td>code</td>
  <td>2</td>
  <td>Y</td>
  <td>Identifer Type code.  Accetable values are in ("", "Blank"),("01", "Other"),("02","Medicare UPIN"),
    ("04","Medicare ID Type Unspecified"),("05", "Medicaid"),
    ("06", "Medicare OSCAR/certification"), ("07", "Medicare NSC"),
    ("08", "MEDICARE PIN")</td>
</tr>

<tr>
  <td>state</td>
  <td>2</td>
  <td>Y</td>
  <td>State according to ISO 3166-2:US.</td>
</tr>

<tr>
  <td>Issuer</td>
  <td>150</td>
  <td>Y</td>
  <td>The name of the issuing body.</td>
</tr>


</table>



Direct Addresses (direct_addresses)
----------------

<table>
<tr>
  <td>Name</td>
  <td>Max Length</td>
  <td>Required</td>
  <td>Notes</td>
</tr>


<tr>
  <td>email</td>
  <td>150</td>
  <td>Y</td>
  <td>A Direct address</td>
</tr>

<tr>
  <td>organization</td>
  <td>150</td>
  <td>Y</td>
  <td>Name of organization</td>
</tr>

<tr>
  <td>is_public</td>
  <td>None</td>
  <td>Y</td>
  <td>`true` if Direct address is public and `false` otherwise.</td>
</tr>



</table>

Code Contributions
==================


We are looking for code contributions in the form of pull requests.
