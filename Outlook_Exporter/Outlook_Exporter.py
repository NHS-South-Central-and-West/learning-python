import datetime
import pandas as pd
import win32com.client


#Define the outlook object
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")

# Print Outlook Folders
for folder in outlook.Folders: 
    print(folder.Name)



#Define the folder you want to search (inbox default is 6)
mbox_name = 'emile.hampson@nhs.net'  ### mailbox to scrape
mbox = outlook.Folders[mbox_name].Folders['Inbox']

print(outlook.Folders(3).Name)

#Fetch messages from the above defined folder                                    
messages = mbox.Items

# Create dataframes to hold data
message_extract = pd.DataFrame(columns=(
    'message_id', 'received_date', 'subject', 'sender_id', 'message_body'))
recipient_lkp = pd.DataFrame(columns=('message_id', 'recipient_id'))
user_extract = pd.DataFrame(columns=('ID', 'Name', 'Company', 'Email'))


# Main loop
for i, m in enumerate(messages):
    # print(m.Subject)
    if 'Test_python_outlook' in m.subject:
        # print(m.Subject)
        m_id = len(message_extract)
        m_received_date = m.senton.date()
        m_subject = m.subject

        if m.SenderEmailType == 'Ex':
            s_address = m.Sender.GetExchangeUser().PrimarySmtpAddress
            s_name = m.Sender.AddressEntry.GetExchangeUser().Name
            s_company = m.Sender.AddressEntry.GetExchangeUser().CompanyName
        else:
            s_address = m.Sender.address
            s_name = m.Sender.address.split("@")[0]
            s_company = None


        if s_address in user_extract['Email'].unique():
            m_sender_id =  user_extract[user_extract.Email == s_address].iloc[0]['ID']

        else:
            m_sender_id = len(user_extract)

            # Add sender to user extract
            user_extract.loc[m_sender_id]=[
                m_sender_id,
                s_name,
                s_company,
                s_address
                ]
        m_body = str(m.body)
        
        # Append message details to message extract
        message_extract.loc[m_id] = [
            m_id,
            m_received_date,
            m_subject,
            m_sender_id,
            m_body
        ]

        # sub-loop to work through recipients
        for j, r in enumerate(m.Recipients):
            # check if user belongs to an exchange user and get info.
            if r.AddressEntry.GetExchangeUser().PrimarySmtpAddress is not None:
                r_address = r.AddressEntry.GetExchangeUser().PrimarySmtpAddress
                r_name = r.AddressEntry.GetExchangeUser().Name
                r_company = r.AddressEntry.GetExchangeUser().CompanyName

            else:
                r_address = r.address
                r_name = r.address.split("@")[0]
                r_company = None
            


            # Check if user exists, if so grab id else add row
            if r_address in user_extract['Email'].unique():
                r_id = user_extract[user_extract.Email == r_address].iloc[0]['ID']
            else:
                r_id = len(user_extract)
                user_extract.loc[r_id] = [
                    r_id,
                    r_name,
                    r_company,
                    r_address
                    ]
            

            # Append ids to lookup
            recipient_lkp.loc[len(recipient_lkp)] = [
                m_id,
                r_id,
            ]

# print extracts
print(message_extract)
print(user_extract)
print(recipient_lkp)

# print unidentified address
print(user_extract.iloc[0, 3])
