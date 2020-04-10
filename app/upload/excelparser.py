import re
from datetime import date
import pyexcel


def convert_to_date(datetime: str):
    """Convert the date-time string(dd/mm/yyyy) to date time object"""
    if type(datetime) == str:
        date_, *_ = datetime.split()
        dd, mm, yyyy = [int(val) for val in date_.split("/")]
        return date(year=yyyy, month=mm, day=dd)
    return datetime


def rename_header(headers: list) -> list:
    """This function is replacing all the column names of the given excel sheet with the field names of the Type8"""
    for i in range(len(headers)):
        headers[i] = headers[i].replace("Transaction ID", "transaction_id") \
            .replace("Value Date", "transaction_value_date") \
            .replace("Txn Posted Date", "transaction_posted_date") \
            .replace("Description", "mode_of_payment") \
            .replace("Cr/Dr", "credit") \
            .replace("Transaction Amount(INR)", "transaction_amount")
    return headers


def xlparser(xlfile):
    """Parse the excel data coming from forms"""
    xl = pyexcel.get_book(file_type="xls", file_content=xlfile)
    sheets = tuple(xl.dict.keys())  # get all the sheet names from the excel file
    rows = xl.dict.get(sheets[0])
    headers = rename_header(rows[6][1:])  # get all the data from the first sheet
    for row in rows[7:]:
        data = dict(zip(headers, row[1:]))
        data["mode_of_payment"] = (
            re.findall(r"RAZORPAY|MSWIPE|CCARD|GOOGLE|AXISROOMS|ICICI|SELF|FINO|MAKEMYTRIP|IBIBO|Paytm",
                       data.get("mode_of_payment"))[0]
        )
        data['transaction_value_date'] = convert_to_date(data['transaction_value_date'])
        data['transaction_posted_date'] = convert_to_date(data['transaction_posted_date'])
        data.pop("ChequeNo.")
        yield data


if __name__ == "__main__":
    with open("./ICICI_648805052604_sample.xls", "rb") as f:
        xlparser(f.read())






