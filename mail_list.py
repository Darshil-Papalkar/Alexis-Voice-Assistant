email = dict()
email['myself']='papalkardarshil13@gmail.com'
email['father']='tushar.papalkar@gmail.com'
email['mother']='shraddhapapalkar@gmail.com'
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




