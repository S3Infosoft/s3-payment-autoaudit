import random
from names import get_full_name

MONTH_ABBR = {"01": "Jan", "02": "Feb", "03": "Mar", "04": "Aor", "05": "May", "06": "June",
              "07": "July", "08": "Aug", "09": "Sep", "10": "Oct", "11": "Nov", "12": "Dec"}


def random_ints(size, start=1, stop=100):
    return [random.randint(start, stop) for _ in range(size)]


def provide_master_data(month: int, year: int) -> dict:
    """
    Provide sample data to populate all the values in the master data excel.
    Later on this structure would be provided by autoaudit API call.
    :return: dictionary of data to populate master data for excel report geenration.
    """
    data = {
        "metadata": {
            "filename": "master_data_sample_1.xlsx",
            "tab1_name": f"Master data {MONTH_ABBR[month]} - {year}",
            "tab2_name": f"Bank Reconcilitaion {MONTH_ABBR[month]} -{year}"
        },
        "tab1_table1": {
            "headers": ['Sr. No', 'Booking Date ', ' Guest Name ', 'Email Id', 'Contact No', 'Web Site ', 'Check-in ',
                        'Check-Out', 'NO. Of  Adults', 'Stay Period', 'No of Rooms', 'Room Nights', 'Room Nos',
                        ' Total Tax ',
                        'Commission Amt  ', 'Supplier Amt ', 'Advance Date', ' Advance  Amt  ', 'Room Bill ',
                        'Food Bill ', 'Taxi', 'Drink', ' Discount ', 'Total', 'Cash', 'Status',
                        'Per Day Room Charges Realised', 'BanK'],
            "data": [{}]
        },
        "tab1_table2": {
            "headers": ['Sr.No.', 'Description', 'No of Rooms', '', '', 'Days in Month', '100% Capacity Room Nights',
                        'Rooms Nights Used', 'Capacity Utilisation', 'Rate Realisation'],
            "data": [{
                "row1": ['1', 'NO OF ROOMS', 12, '', '', 13, 550, 13, '60%', 34578.21],
                "row2": ['2', 'NO OF BUNGLOW', 20, '', '', 3, 445, 10, '40%', 4008.91],
                "row3": ['3', 'FOOD PER BILL', '', '', '', 3, '', 10, '', 40000],
                "row4": ['4', 'AVERAGE PER DAY', '', '', '', 4, '', 12, '', 8000],
                "row5": ['5', 'AVERAGE PER ROOM NIGHT', '', '', '', 8, '', 11, '', 7000],
            }]

        },
        "tab2_table1": {
            "headers": ['Customer Name', 'Stay Period', 'Check in', 'Check Out', 'Razorpay(Direct Booking',
                        'Razorpay Commission',
                        'Bank Credit(B+3)', 'Bank Crdit Date', 'ICICI Machine', 'ICICI Commission', 'Bank Credit',
                        'Bank Credit Date', 'Paytm', 'Paytm Commission', 'Bank Credit(CI-3 Days)', 'Bank Credit Date',
                        'Google Pay', 'Bank Credit', 'Bank Date', 'MMT', 'MMT Commission', 'Bank Credit(CI-3 Days)',
                        'Bank Credit Date', 'Go Ibibo', 'Go Ibibo Commission', 'Bank Credit(CI-3 Days)',
                        'Bank Credit Date', 'Axis Rooms(Booking.com)', 'Axis Rooms Commission', 'Bank Credit(B+5)',
                        'Bank Credit Date', 'Direct Bank', 'Atom', 'Atom Commission', 'Bank Credit(S+1)',
                        'Bank Credit Date', 'M Swipe', 'M Swipe Commission', 'Bank Credit(S+1)', 'Bank Credit Date',
                        '42', '43'],
            "data": [{}]

        },
        "tab2_table2": {
            "headers": ["", "SALE AMT",	"COMMISSION AMT", "AMT IN BANK"],
            "data": [{
                "row1": ['', 'RAZORPAY', 45637, 5347, 89756],
                "row2": ['', 'MMT', 1700, 2345.89, 8000],
                "row3": ['', 'Google Pay', 1800, 2345, 8000],
                "row4": ['', 'ICICI Machine', 8000, 7634, 87345],
                "row5": ['', 'MMT', 9000, 7634, 87345],
                "row6": ['', 'GOIBIBO', 5900, 7634, 87345],
                "row7": ['', 'AXIS ROOMS', 7000, 7634, 87345],
                "row8": ['', 'DIRECT BANK', 4000, 7467, 87345],
                "row9": ['', 'ATOM', 5200, 9000, 87345],
                "row10": ['', 'M SWIPE', 23000, 45678, 8735],
            }]
        }
    }
    data_length = random.randint(5, 50)
    dates = random_ints(data_length, stop=31) if month != "02" else random_ints(data_length, stop=28)
    dates.sort()
    date_format = "{:02}-{}-{}"
    data_template = [None, None, None, '', '', 'Booking.com', None, None, 'A3', 1, 1, 1, 'R1',
                     '', '', '', None, 2012, 2241, 4306, 3586, '', '', 1071, 4272, 'Done', 1627, 1777]
    data_template2 = ['', None, 'Direct', None, None, '', '', '', None, 4458, 5643,
                      6563, None, '', '', '', None, 5607, 4673, None, 3988, 6959, 1788,
                      None, 3397, 5167, 2014, None, '', '', '', None, '', '', '', '',
                      None, 5375, 1509, 1478, None, 1878]
    for i in range(data_length):
        d = data_template.copy()
        d2 = data_template2.copy()
        for index in (1, 6, 7, 16):
            d[index] = date_format.format(dates[i], month, year)
        for index in (3, 4, 8, 12, 16, 19, 23, 27, 31, 36, 40):
            d2[index] = date_format.format(dates[i], month, year)
        d[0] = i+1
        d[2] = get_full_name()
        d2[1] = get_full_name()
        data["tab1_table1"]["data"][0][f"row{i}"] = d
        data["tab2_table1"]["data"][0][f"row{i}"] = d2

    return data

    # TODO: Populate the data to create structure as expected for report generation.


if __name__ == "__main__":
    pass
