import re
import pyperclip
PhoneRegex = re.compile(r'''
# Example phone numbers look like 415-555-1234, 555-1234 , (415) 555-1234 , 555-2222 ext 12345,ext. 12345, x12345
(((\d\d\d)|(\(\d\d\d\)))?  #area-code(optional)
(\s|-)           #first separator
\d\d\d            #first 3 digits
-                 #separator
\d\d\d\d           #last 4 digits
(((ext(\.)?\s)|x)      #Extension word-part (optional)
 (\d{2, 5}))?)
''', re.VERBOSE)
emailRegex = re.compile(r'''
#Example some+._thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+  #name part - created own character class
@                # @ symbol
[a-zA-Z0-9_.+]+  # domain name part

''', re.VERBOSE)
text = pyperclip.paste()
extractedPhone = PhoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)
allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])
print(allPhoneNumbers)
print(extractedEmail)
result = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(result)