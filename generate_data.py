from math import nan
import os,json,string
import pandas as pd,random as r
from  datetime import datetime,timedelta
from array import array
import numpy as np
# Function to convert
def listToString(s):
        str1 = ""
        for e in s:
                str1 += e
        return str1
#generate random digite--

def random_digit(start,end):
    random_digit = r.randint(start,end)
    return random_digit

# generate random string 
def random_string(S,str_type):
    if  str_type == 'lowercase' :
           r_string = ''.join(r.choices(string.ascii_lowercase + string.digits, k = S))  
    elif str_type  == 'uppercase':
            r_string = ''.join(r.choices(string.ascii_uppercase + string.digits, k = S))  
    else :
            r_string = ''.join(r.choices(string.ascii_uppercase + string.digits, k = S))  
    
    return r_string

# -----------------------------------------Password -----------------------------------------------
def strong_password(max_len):
    DIGITS = r.choices(string.digits)
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    password = ""
    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS
    # randomly select at least one character from each character set above
    rand_digit = ''.join(r.choices(string.digits, k = 1))
    rand_upper = ''.join(r.choices(string.ascii_uppercase, k = 1))  
    rand_lower = ''.join(r.choices(string.ascii_uppercase,  k = 1))  
    rand_symbol = r.choice(SYMBOLS)
     
    # combine the character randomly selected above
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol
     
    for x in range(max_len - 4):
        temp_pass = temp_pass + r.choice(COMBINED_LIST)
     
        # convert temporary password into array and shuffle to
        # prevent it from having a consistent pattern
        # where the beginning of the password is predictable
        temp_pass_list = array('u', temp_pass)
        r.shuffle(temp_pass_list)
     
    # traverse the temporary password array and append the chars
    # to form the password
    for x in temp_pass_list:
            password = password + x
             
    return password

#---------------------------------------Generate random Phone Number --------------------------------------------------
#--Generate  random phone number
def get_phone_num():
     number = phone_number_strt_with(6,9)
     return number

#---Generate number with country 
def number_with_country_code(code):
   number = code + get_phone_num()
   return number
   
#---Generate number with starting Bewting  
def phone_number_strt_with(from_start, to_star):
    p_number = []
    p_number.append(r.randint(from_start, to_star))# the first number should be in the range of 6 to 9
    for i in range(1, 10):
        p_number.append(r.randint(0, 9))
    p_number_str = map(str, p_number) # convert into string
    phone_number =  (listToString(p_number_str))
    
    return phone_number

#---------------------------------------email id generator ---------------------------#
def email():
    length = 7
    provider = ['@gmail.com','@outlook.com','@airte.com']
    provider_prob = [.2,.3,.5]
    a = ''.join(r.choice(string.ascii_lowercase) for _ in range(length))
    email = a + np.random.choice(provider, p = provider_prob)
    return email

##------------------------------------Data Time Generator -----------------------------#
# Get time stamp
def random_epoch_time():
    y = r.randint(2017,2022)
    m = r.randint(1,12)
    d = r. randint(1,28)
    h = r. randint(1,23)
    min = r. randint(1,50)
    epoch_time = datetime(y, m, d, h, min, 0).strftime('%s')
    return epoch_time

def random_date_time():
    start = datetime.strptime('1/1/2008 1:30 PM', '%m/%d/%Y %I:%M %p')
    end = datetime.strptime('1/1/2009 4:50 AM', '%m/%d/%Y %I:%M %p')
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = r.randrange(int_delta)
    time_stamp = start + timedelta(seconds=random_second)
   # time_stamp = str(time_stamp)
    time_stamp = str(time_stamp)
    return time_stamp

def current_time_stamp():
    currentDT = datetime.now()
    yyyymmddhhmmss = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
    yyyy = currentDT.strftime("%Y")
    mm = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
    dd = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
    hh = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
    mi = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
    ss = currentDT.strftime("%Y-%m-%d_%H:%M:%S")
   
    return yyyymmddhhmmss

#---------------check directory is avilable -------------------#
def isdir(path):
    isdir = os.path.isdir(path) 
    return isdir

 #--------------------------------Start main function to generate data -------------------------- 
def function_gen_data(df,col_names):
    function_list = {'random_epoch_time':random_epoch_time(),'number':get_phone_num()}
    data_dict = {} 
    for col in col_names:
        if col in function_list:
            data_dict[col] = "test"
        
        if col == "meta" or col[-5:]== "_meta":
            col_list = df[col].tolist()
            sheet_name =  col_list[0]
            data_dict[col] = generate_meta(sheet_name)
       
        else :
            col_list = df[col].tolist()  
            data_dict[col] = (r.choice(col_list))                          
    
    return data_dict  

def generate_meta(sheet_name):
    with pd.ExcelFile('data.xlsx') as reader:
        meta_df = pd.read_excel(reader,sheet_name = sheet_name)

    col_names = meta_df.columns
    meta_data = (function_gen_data(meta_df, col_names))
    return meta_data

def data_function(no_of_record,sheet_name,file_path):
    data = []
    with pd.ExcelFile(file_path) as reader:
        data_df = pd.read_excel(reader,sheet_name = sheet_name)
    
    col_names = data_df.columns
    for i in range(no_of_record):
        data_v = function_gen_data(data_df,col_names,)
        data.append(data_v)
    return data


#_________________________Craete json file and write data ____________________________________
def json_file(data):
    with open('test.json', 'w', encoding='utf-8') as f:
           json.dump(data, f, ensure_ascii=False, indent=4)


def read_sheet(sheet_name):
    try:
        with pd.ExcelFile(file_path) as reader:
            df = pd.read_excel(reader,sheet_name = sheet_name)
        return df

    except OSError as e:
         print("ERROR: Unable to read file", e)

def generte_rcord():
    data_df = read_sheet(data_sheet) 
    try:
        col_names = data_df.columns
        data_dict = {} 
        for col in col_names:
            col_list = data_df[col].tolist() # store  excel column  names in col_list 
            new_col_list = [item for item in col_list if not(pd.isnull(item)) == True] # clear all nan value from column
            print()
            if new_col_list[0] in function_list:
            #if (col in function_list): 
                col_list = data_df[col].tolist()
                data_dict[new_col_list[0]] =  function_list[col]
         
            elif col == "meta" or col[-5:]== "_meta":
                #col_list = data_df[col].tolist()
                sheet_name =  new_col_list[0]
                data_dict[col] = generate_meta(sheet_name)              
            else :
                    #col_list = data_df[col].tolist()  
                    data_dict[col] = (r.choice(new_col_list))       
        
        return(data_dict)
    except AttributeError as e:
         print("ERROR: ", e)

def records(no_of_record):
    data_list = []
    for i in range(no_of_record):
        data_v = generte_rcord()
        data_list.append(data_v)
    return data_list


if __name__=="__main__":
    function_list = {'random_epoch_time':random_epoch_time(),'number':get_phone_num(),'current_time_stamp':current_time_stamp(),\
    'email':email(),'random_date_time':random_date_time()}
    
   
   
    file_path = 'UPCDeatils.xlsx' #input("Enter excel file path  : ") # 
    data_sheet = 'data' #input ("Sheet Name for read semple data : ")
    no_of_record = 10 #int(input("No of record : "))
    
    data = records(no_of_record)
    json_file(data)
    print("Data generateed")