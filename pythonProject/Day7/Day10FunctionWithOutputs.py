#Functions with outputs


# def format_name(f_name, l_name):
#    formated_f_name = f_name.title()
#    formated_l_name = l_name.title()
#    return f"{formated_f_name} {formated_l_name}"
#
# formated_string = format_name("nick", "jurchescu")
#
#
# print(formated_string)
def is_leap(year):
   '''Takes a year as input and returns True if the Year is Leap Year or False if its not '''
   if year % 4 == 0:
      if year % 100 == 0:
         if year % 400 == 0:
            return True
         else:
            return False
      else:
           return True
   else:
      return False


def days_in_month(year, month):
   month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
   if is_leap(year):
      month_days[1] += 1
   return month_days[month-1]



# 🚨 Do NOT change any of the code below
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)


