from csv import DictReader
import Register_user
from Register_multiple_user.Excel_register import load_data
import Register_user
import pytest

@pytest.mark.parametrize("firstname,lastname,username,password", load_data())

def test_execute(firstname,lastname,username,password):

 

    with open("keyword.csv", "r") as f:
        reader = DictReader(f)

        for row in reader:
            keyword = row["Keywords"]
            locator_type = row["Locatortype"]
            locator_path = row["locatorpath"]
            # locator=row["Locatortype"],row["Locatorpath"]
            value = row["Value"]

          
            func = getattr(Register_user,keyword)

            # Call the function with correct params
            print(f" Executing: {keyword} | Locator: {locator_type}, {locator_path}, Value: {value}")
            if locator_type and locator_path and value:
                func(locator_type,locator_path,value)
            elif locator_type and locator_path:
                func(locator_type,locator_path)
            elif value:
                func(value)
            else:
                func()

        # for row in reader:
        #     keyword = row["Keywords"]
        #     locator = (row["Locatortype"], row["locatorpath"])
        #     value = row["Value"]
        #
        #     func = getattr(Register_user, keyword)
        #
        #     if locator[0] and locator[1] and value:
        #         func(*locator, value)
        #     elif locator[0] and locator[1]:
        #         func(*locator)
        #     elif value:
        #         func(value)
        #     else:
        #         func()








