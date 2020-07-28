number = dict()
number['one']='1'
number['two']='2'
number['three']='3'
number['four']='4'
number['five']='5'
number['six']='6'
number['seven']='7'
number['eight']='8'
number['nine']='9'
number['ten']='10'
number['eleven']='11'
number['twelve']='12'
number['thirteen']='13'
number['fourteen']='14'
number['fifteen']='15'
number['sixteen']='16'
number['seventeen']='17'
number['eighteen']='18'
number['nineteen']='19'
number['twenty']='20'

def check(num):
    for k,v in number.items():
        if k==num:
            return(int(v))
            
        
if __name__=='__main__':
    print(number)
    check(input())
