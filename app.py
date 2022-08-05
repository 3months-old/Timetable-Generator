from flask import Flask, render_template, request, send_file, send_from_directory
import pandas as pds
import numpy as np
import xlsxwriter

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    return render_template ('index.html')

@app.route('/data', methods=['GET', 'POST'])

def data():
        if request.method=='POST':
            file=request.form['upload-file']
            newdata=pds.read_excel(file)
            copy=newdata
            newdata['Course Code']=newdata['Course Code'].str.lower()
            newdata['Sub.Code']=newdata['Sub.Code'].str.lower()
            newdata['T Names']=newdata['T Name'].str.lower()
            course_codelis=newdata['Course Code'].tolist()      #converting the course code into lists
            #print('list is',course_codelis)
            course_dict={}
            b='a'
            j=ord(b[0])
            for i in course_codelis:
                i.lower()                        #creating the codes and assigning to the different courses
                j+=1
                b=chr(j)
                if i in course_dict:
                    continue
                else:
                    y={i:b}
                    course_dict.update(y)
            #print('dict',course_dict)
            for i in course_dict:                               #Update Course column with codes.
                newdata=newdata.replace(i,course_dict[i])
            prof_codelis=newdata['T Name'].tolist()
            #print(prof_codelis)
            prof_codedict={}
            c=10
            for i in prof_codelis:
                i.lower()                         #creating the codes for professor name and assigning
                c+=1
                if i in prof_codedict:
                    continue
                else:
                    y={i:c}
                    prof_codedict.update(y)
            #print(prof_codedict)
            for i in prof_codedict:                         #creating the new dataframe with updated codes for course and professor name
                newdata=newdata.replace(i,prof_codedict[i])
            #print(copy)
            #print(newdata)
            def create_list(dictionary,df):                 #creating a list of dictionaries.
                li=[]
                for i in dictionary:
                    di={}
                    for k in range(len(df)):
                        if dictionary[i]==df.loc[k,'Course Code']:
                            l=[df.loc[k,'T Name'],df.loc[k,'Class/Week'],6]
                            ke=df.loc[k,'Sub.Code']
                            y={ke:l}
                            di.update(y)
                        else:  continue
                    li.append(di)
                return(li)
            li=(create_list(course_dict,newdata))
            global avail
            avail=[]

            def arrange(dix):
                t_t=np.zeros([6,5],dtype=object)
                k=1
                week=['Mon','Tue','Wed','Thu','Fri']
                time=['8:30-10:45','11:00-1:15','2:00-4:15','4:30-6:45']
                x,y=1,0
                for i in week:
                    t_t[x,y]=i
                    x+=1
                x,y=0,1
                for i in time:
                    t_t[x,y]=i
                    y+=1
                for i in dix:
                    class_week=dix[i][1]
                    if k%2==0:
                          day=5
                          slot=4
                          t=-1
                    else:
                          day=1
                          slot=1
                          t=1
                    while class_week>0:
                        #print('k',k)
                        #print('day slot',day,slot)
                        if t_t[day,slot]==0 and str(dix[i][0])+'-'+str(day)+','+str(slot) not in avail:
                               t_t[day,slot]=i
                               class_week-=1
                               avail.append(str(dix[i][0])+'-'+str(day)+','+str(slot))
                               #print(i)
                               day=day+t
                               if day>5:
                                   day=1
                                   slot=slot+t
                               elif day<1:
                                   day=5
                                   slot=slot+t
                        else:
                               day=day+t
                               if day>5:
                                   day=1
                                   slot=slot+t
                               elif day<1:
                                   day=5
                                   slot=slot+t
                    k=k+1
                return(t_t)
            def getlist(dict):
                lisi = []
                for key in dict.keys():
                    lisi.append(key)
                return lisi
            newfile=pds.ExcelWriter('Final_timetables.xlsx',engine='xlsxwriter')
            a=0
            for i in li:
                df=pds.DataFrame(arrange(i))
                df=df.replace(0,'----')
                df.to_excel(newfile, sheet_name=getlist(course_dict)[a],index=False)
                #print('timetable for course {} is \n {}'.format(getlist(course_dict)[a], df))
                a+=1
            newfile.save() #1
            return send_file(newfile,attachment_filename="Timetable_final.xlsx", as_attachment=True)

@app.route('/download')

def download_file():
    p= "Timetable_raw.xls"
    return send_file(p,as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
