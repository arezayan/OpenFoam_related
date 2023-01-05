
#read OpenFoam data by python
#this code reads velocity data from postProcessing directory and plot them.
#obviusly it would be useful plotting any veraiable in such way.
#Pandas packag is being used

import os
import matplotlib.pyplot as plt
import pandas as pd


samplePath=u'postProcessing/sampleDict/' #define sample directory of postProcessing Folders
timeName=0
#file name: be careful to write file precisly considering its extension.
#while "setFormat" is on "raw" mode, no need to define extension.
fName='half.csv'

tot_destin=samplePath + str(timeName) + '/'+ fName
outPut=[]
for dirStr in os.listdir(samplePath):

    tot_destin=samplePath + str(dirStr) + '/'+ fName
    data=pd.DataFrame(pd.read_csv(tot_destin))
    magU=data.iloc[:,1]
    Ux=data.iloc[:,2]
    Uy=data.iloc[:,3]
    y_cor=data.iloc[:,0]
    outPut.append(magU)

    plt.plot(magU,y_cor,label=dirStr)
    plt.xlabel(data.columns[1]+ ' (m/s)')
    plt.ylabel(data.columns[0]+' (m) ')
    plt.ylim(0,0.1)
    plt.legend(loc="lower right")




plt.figure(dpi=300)
plt.subplot(1, 2, 1)
plt.plot(Ux,y_cor)

plt.xlabel('Ux')
plt.ylabel('y (m) ')

plt.subplot(1, 2, 2)
plt.plot(Uy,y_cor)
plt.xlabel('Uy')

plt.show()
