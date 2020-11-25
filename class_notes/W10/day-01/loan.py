# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 18:07:10 2020

@author: platf
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QPushButton, QGridLayout


class Window(QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.setFixedSize(440, 200)

    def init_ui(self):
        layout = QGridLayout()

        # let's create some labels

        label_loan = QLabel('Prinicipal loant amount')
        label_interest = QLabel('Yearly Interest (%)')
        label_period = QLabel('Period in months')
        label_payment = QLabel('Monthly payment    ')


        #create some text fields

        edit_loan = QLineEdit()
        edit_interest = QLineEdit()
        edit_period = QLineEdit()

        # add some push buttons

        button_calculate = QPushButton('Calculate')

        # some action when clicked on button

        button_calculate.clicked.connect(
            lambda: self.on_button_calculate_clicked(edit_loan,edit_interest, edit_period, label_payment))


        # adding labels to the layout
        layout.addWidget(label_loan, 0, 0)
        layout.addWidget(label_interest, 1, 0)
        layout.addWidget(label_period, 2, 0)
        layout.addWidget(label_payment, 4, 0)

        layout.addWidget(edit_loan, 0, 1)
        layout.addWidget(edit_interest, 1, 1)
        layout.addWidget(edit_period, 2, 1)

        layout.addWidget(button_calculate, 3, 1)

        self.setLayout(layout)


    def on_button_calculate_clicked(self, edit_loan, edit_interest, edit_period, label_payment):
        loan = float(edit_loan.text())
        interest = float(edit_interest.text())
        interest_per_month = interest / (12 * 100)
        period = float(edit_period.text())

        emi = (loan * interest_per_month * (1 + interest_per_month) ** period) / (
                (1 + interest_per_month) ** period -1
            )

        print(emi)

        text = label_payment.text()
        label_payment.setText(text + str(emi))




def main(args):
    app = QApplication(args)

    application = Window()
    application.setWindowTitle("EMI Calculator for Home Loans")
    application.show()
    app.exec_()


if __name__ == '__main__':
    main(sys.argv)





