import pandas as pd
cols = ["day","time","H1","H2","H3","H4","H5","H6","H7","H8","H9","H10"]
df = pd.read_csv(r"D:\College materials\Acads\4th year\8th sem\FYP\Raghu files\testing_with_python.csv")
print(df.head())
def temp_cal(c,data_frame):
    data_frame.insert(len(data_frame.columns),c,float)
    j=0
    for i in data_frame[c]:
        data_frame[c][j]= 25+(11*data_frame["Insolation"][j]/400)
        j+=1

def House_production(h_prod,max_prod,c_no,data_frame):
    data_frame.insert(c_no,h_prod,float)
    j=0
    for i in data_frame[h_prod]:
        data_frame[h_prod][j] = ((max_prod*data_frame["Insolation"][j]/1000)*(1-(0.0041*(data_frame["Temperature"][j]-25))))
        j+=1

def House_BESS(h_bess,h_prod,h_cons,bess,c_no,data_frame):
    data_frame.insert(c_no,h_bess,float)
    data_frame[h_bess][0] = 0 
    j=1
    for i in data_frame[h_bess]:
        if(j==len(data_frame[h_bess])):
            break
        battery = data_frame[h_bess][j-1]+data_frame[h_prod][j]-data_frame[h_cons][j]
        if(battery>0):
            if(battery>1000):
                data_frame[h_bess][j] = bess
            else:
                data_frame[h_bess][j] = battery
        else: 
            data_frame[h_bess][j] = 0
        j+=1


temp_cal("Temperature",df)

House_production("H1_prod",2000,3,df)
House_production("H2_prod",1500,5,df)
print(df.head(10))
 
House_BESS("H1_bess","H1_prod","H1",1000,4,df)
House_BESS("H2_bess","H2_prod","H2",1000,7,df)
print(df.head(10))