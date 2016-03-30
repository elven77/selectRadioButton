import baseTest
from pages.homePages import HomePages
from pages.tablePages import TablePages


class TableTest(baseTest.BaseTest):
    def test_table_test(self):
        # Load table
        home=HomePages(self.driver)
        home.load()

        # Get table data
        table=TablePages(self.driver)
        table.getColumnNum()
        table.getRowNum()
        table.selectRadioAccFirstname("Elvis")