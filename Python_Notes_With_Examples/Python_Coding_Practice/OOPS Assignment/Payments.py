class Payments:
    creditCardNumber=None
    debitCardNumber=None
    upiNumber=None
    stripeDetails=None

    def addCreditCardDetails(self):
        print("Enter credit card details")

    def addDebitCardDetails(self):
        print("Enter debit card details")

    def editUPINumber(self):
        print("Edit UPI details")

    def deleteStripeDetails(self):
        print("Delete stripe details")

razorPay=Payments()
razorPay.addCreditCardDetails()
razorPay.addDebitCardDetails()
razorPay.deleteStripeDetails()
razorPay.editUPINumber()

instaMojo=Payments()
instaMojo.editUPINumber()