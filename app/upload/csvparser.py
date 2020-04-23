from datetime import datetime
import pandas as pd


def convert_to_date(transaction_date: str):
    """Convert the date-time string(dd/mm/yyyy hh:min_) to date time object"""
    if type(transaction_date) == str:
        date_, time = transaction_date.split()
        dd, mm, yyyy = [int(val) for val in date_.split("/")]
        hh, min_ = [int(val) for val in time.split(":")]
        return datetime(year=yyyy, month=mm, day=dd, hour=hh, minute=min_)
    return transaction_date


def rename_header(headers: list) -> list:
    """This function is replacing all the column names of the given excel sheet with the field names of the Type8"""
    for i in range(len(headers)):
        name = headers[i].lower().split()
        headers[i] = "_".join(name).replace("#", "")  # convert fields like 'invoice#' to 'invoice
    return headers


def csvparser(csvfile):
    """Parse the csv data coming from forms"""
    df = pd.read_csv(csvfile)
    df.drop(["Email", "Labels", "Ref# 2", "Ref# 3", "Ref# 4", "Ref# 5", "Ref# 6", "Ref# 7", "Receipt No",
             "Error Code", "Additional Information", "PG Error Code", "PG Error Message", "Latitude", "Longitude",
             "Bank Name", "Bank Code", "Cheque No", "Cheque Date", "Bank Account no."], inplace=True, axis=1)
    headers = rename_header(df.columns.values.tolist())
    for row in df.values.tolist():
        data = dict(zip(headers, row))
        data['date'] = convert_to_date(data['date'])
        data['settled_on'] = convert_to_date(data['settled_on'])
        yield data


if __name__ == "__main__":
    csvparser("/home/harshita/Documents/S3-Infosoft/files/type9_sample.csv")
