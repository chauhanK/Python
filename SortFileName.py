import os

os.chdir('C:/Users/kchauhan/Documents/Sample')

print(os.getcwd()) # current working directory

for f in os.listdir():

  #print(os.path.splitext(f))

  #f_name, f_ext = os.path.splitext(f)  
  #print(f_name)
  #print(f_name.split('.'))

  f_name,f_ext1,f_ext2=f.split('.')
  #print(f_name)

  f_shortName, f_course, f_num = f_name.split('-')

  f_shortName = f_shortName.strip()
  f_course = f_course.strip()
  f_num = f_num.strip()[1:].zfill(2)

  new_name = '{}-{}.{}'.format(f_num,f_shortName,f_ext2)

  os.rename(f,new_name)
 