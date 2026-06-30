import logging
logging.disable(logging.CRITICAL)
from androguard.core.apk import APK

apk = APK(r'C:\Users\Sha0_s1\Downloads\auto_modified_unsigned.apk')
print('Package:', apk.get_package())
print('Version:', apk.get_androidversion_name())
print('First 5 activities:', apk.get_activities()[:5])
print()
print('Providers:')
for p in apk.get_providers():
    print(f'  {p}')
