from datetime import datetime

date_str = 'January 23, 2023'

date_object = datetime.strptime(date_str, '%B %d, %Y').date()
print(type(date_object))
print(date_object)  # printed in default format
date_string = datetime.strftime(date_object, '%Y-%m-%d')
print(type(date_string))
print(date_string)