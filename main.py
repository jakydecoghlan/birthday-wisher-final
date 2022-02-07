##################### Extra Hard Starting Project ######################
import smtplib
import datetime as dt
import random
import pandas as pd

MY_EMAIL = "jakytest@gmail.com"
PASSWORD = "isla6usted"


# 1. Update the birthdays.csv
# with open("birthdays.csv", "w") as data:
#     data.write("juanca, jakytest@gmail.com, 1990,1,27")



# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
day = now.day
day_of_the_week = now.weekday()
today = (month, day)
print(f"Today is {today}")

df = pd.read_csv("birthdays.csv", index_col=False)
print(df)
# list_of_days = df.day.to_list()
# list_of_months = df.month.to_list()
# print(list_of_days)
# print(list_of_months)


birthday_dict = {(data_row["month"], data_row["day"]): data_row["name"]
                 for (index, data_row) in df.iterrows()}
print(birthday_dict)

for key, value in birthday_dict.items():
    if key == today:
        birthday_is_today = True
    else:
        birthday_is_today = False
    # print(birthday_is_today)
    if birthday_is_today:
        print(value)
        for name in df.name:
            if value == name:
                email = df[df["name"] == value].email.item()
                letter = random.randint(1, 3)
                with open(f"./letter_templates/letter_{letter}.txt", "r") as file:
                    bd_letter = file.read()
                    bd_letter = bd_letter.replace('[NAME]', f'{name}')
                    with open(f"./letter_templates/{name}letter_{letter}.txt", "w") as file:
                        file.write(bd_letter)
                    print(bd_letter)
                    with smtplib.SMTP("smtp.gmail.com") as connection:
                        connection.starttls()
                        connection.login(user=MY_EMAIL, password=PASSWORD)
                        connection.sendmail(from_addr=MY_EMAIL,
                                            to_addrs=email,
                                            msg=f"Subject:Feliz Cumple! \n\n {bd_letter}"
                                            )

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




