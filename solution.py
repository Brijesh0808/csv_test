import time

t1=time.time()

once=True
path='/home/brijesh08/Documents/csv_test/data/'
op = '/home/brijesh08/Documents/csv_test/'

df = pd.read_csv(path+'0'+'.csv')
df.to_csv(op+'abc.csv', index=False, header=True)

n=100_000
for s_no in range(1, n):
    file_path = path+str(s_no)+'.csv'
    df = pd.read_csv(file_path)
    df.to_csv(op+'abc.csv', mode='a', index=False, header=False)
    
t2=time.time()
t2-t1
