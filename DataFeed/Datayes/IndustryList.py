# -*- coding: utf-8 -*-
"""
Created on Sun Jan 03 22:17:23 2016

@author: MY2570P
"""


#需要权限才能调用

from Datayes.dataapi import Client
from Util.Var import DatayesToken as token
if __name__ == "__main__":
    try:
        client = Client()
        client.init(token)
        url1='/api/master/getIndustry.json?field=&industryVersion=SW&industryVersionCD=&isNew=1&industryLevel=4'  #secID,secShortName
        code, result = client.getData(url1)
        if code==200:
            print result.decode('gbk').encode('utf-8')
            file_object = open('D:\MyDoc\Database\MyTradingSystem\Datayes\industrylist.csv', 'w')
            file_object.write(result)
            file_object.close( )

        else:
            print code
            print result.decode('gbk').encode('utf-8')
    except Exception, e:
        #traceback.print_exc()
        raise e