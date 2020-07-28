email = dict()
# edit by entering person name on left and mail id on right
email['myself']='myself@gmail.com' # enter the mail id 
email['father']='father@gmail.com' # enter the mail id
email['mother']='mother@gmail.com' # enter the mail id

def mail(K):
    for k,v in email.items():
        if K in k:
            return(v)

def check_email(K):
    for k,v in email.items():
        if k==K:
            return('True')
            break    


if __name__ == '__main__':
    id = input()
    mail(id)
    check_email(id)




