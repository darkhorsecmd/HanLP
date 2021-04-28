import jpype
from jpype import *

startJVM(getDefaultJVMPath(), "-Djava.class.path=D:\\triz_work\\hanlp\\hanlp-1.8.1-release\\hanlp-1.8.1.jar;D:\\triz_work\\hanlp\\data-for-1.7.5",

         "-Xms1g",

         "-Xmx1g")

jpype.java.lang.System.out.println("hello")



HanLP = JClass('com.hankcs.hanlp.HanLP')
# HanLP = JClass('com.hankcs.hanlp')

print(HanLP.segment('你好，欢迎在Python中调用HanLP的API'))

