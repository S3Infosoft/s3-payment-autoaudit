import re
import pyexcel_xls


def xlparser(xlfile):
    xl = pyexcel_xls.read_data(xlfile)
    sheets = tuple(xl.keys())
    rows = xl.get(sheets[0])
    headers = rows[6][1:]
    for row in rows[7:]:
        data = dict(zip(headers, row[1:]))
        data["Description"] = (
            re.findall(r"RAZORPAY|MSWIPE|CCARD|GOOGLE|AXISROOMS|ICICI|SELF|FINO|MAKEMYTRIP|IBIBO|Paytm",
                       data.get("Description"))[0]
        )
        data.pop("ChequeNo.")
        print(data)


if __name__ == "__main__":
    xlparser("./ICICI_648805052604_sample.xls")
