from Velotrade_scrap import parser
import xlsxwriter


def writer(parametr):
    book = xlsxwriter.Workbook(r"C:\Users\User\Desktop\velotrade.xlsx")
    page = book.add_worksheet("товар")

    row = 0
    column = 0

    page.set_column("A:A", 50)
    page.set_column("B:B", 20)
    page.set_column("C:C", 10)
    page.set_column("D:D", 20)
    page.set_column("E:E", 100)
    page.set_column("F:F", 70)

    for item in parametr():
        page.write(row, column, item[0])
        page.write(row, column+1, item[1])
        page.write(row, column+2, item[2])
        page.write(row, column+3, item[3])
        page.write(row, column+4, item[4])
        page.write(row, column+5, item[5])
        row += 1

    book.close()


writer(parser)