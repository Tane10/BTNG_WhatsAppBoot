from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sms", methods=['GET','POST'])


def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')




    forum_message = "Please join 'Kobo Forum' WhatsApp Group to connect with other like minded people"
    contract_message = "Kobo\r\n Contact number: +234-802-5557-8 \r\n Email: kobo@contact-munchet.ltd \r\n Address: 1,Yusuf Oladehinde Street \r\n Ifako Ijaiye \r\n Lagos \r\n"
    loantemplate_message = "Please copy and edit the below template. Once complete send back with the word LOAN at the start \r\n" \
                           "Name: <Your full name here>,\r\n" \
                           "Age: <Your age>\r\n" \
                           "Date of Birth: <dd/mm/yyyy>\r\n" \
                           "Contact Number: <include dial code>\r\n" \
                           "Breif: <What bussiness do you run>\r\n" \
                           "Address: <Please enter your address>\r\n" \
                           "Zip Code: <Zip code>\r\n" \
                           "Amount Required: <Amount required in naira>\r\n"
    receivedloanrequest_message = "We have reviced your loan and its currently being proccesed. We will contact you in 5 to 10 working days"
    resources_message = "Create a Business Budget in 5 Simple Steps: https://www.freshbooks.com/blog/the-5-step-plan-to-creating-a-balanced-business-budget\r\n" \
                        "How to Effectively Pitch Business Ideas to Investors: https://medium.com/swlh/how-to-effectively-pitch-business-ideas-to-investors-dd76661b02f1 \r\n" \
                        "How to calculate company income tax in Nigeria Read more: https://www.legit.ng/1179976-how-calculate-company-income-tax-nigeria.html \r\n" \
                        "List of accelerators / incubators / startups programs in Nigeria: https://blog.accounteer.com/list-of-accelerators-incubators-startups-programs-in-nigeria-d2ce1eac74c7"
    milestone_message = "You currently have 10 days to reach your goal"
    help_message = "Key words to send and use our whats app: \r\n" \
                  "Forum = This will send you the name of our Forum WhatsApp group so you can join it \r\n\r\n" \
                  "Contact = Will send you our contact details \r\n\r\n" \
                  "Template = Will send you a Loan template that you can copy and edit and send back with the key word LOAN, and we can start processing it \r\n\r\n" \
                  "Resources = Will send you a list of helpful links to aid you bussniss \r\n\r\n " \
                  "Milestone = Will send you how many days your have leave to reach your milestone \r\n\r\n" \
                  "Pay: <Money amount> = Will allow you to pay some of your loan back"

    # Create reply
    resp = MessagingResponse()


    if msg == "Forum":
        resp.message(forum_message.format(msg))
    if "LOAN" in msg:
        resp.message(receivedloanrequest_message.format(msg))
    if "Pay:" in msg:
        payment = msg.split(":")
        payment = float(payment[1])
        amountLeft = str(40000 - payment)
        message = "You have: " + amountLeft + " to pay of your loan"
        resp.message(message.format(msg))
    elif msg == "Contact":
        resp.message(contract_message.format(msg))
    elif msg == "Template":
        resp.message(loantemplate_message.format(msg))
    elif msg == "Resources":
        resp.message(resources_message.format(msg))
    elif msg == "Milestone":
        resp.message(milestone_message.format(msg))
    elif msg == "Help":
        resp.message(help_message.format(msg))




    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)