# This is the pipeline to be "demoed" in the QIN meeting.
# This pipeline will not be using the Tactc CMS systems.
# The scope of the script is to demonstrate how to used the deployed applications utilizing the pygrunt and the grunt based dockers.
# We want to focus in the flexibility of out tool and demonstrate that tools like XNAT and Slicer can be used to stream data to grunt based services since both provide a python way to execute code.

# The library needed is called pygrunt.
# Can be found here: https://github.com/Mayo-QIN/pygrunt

# Steps to be executed

# Stream the data to the Standrord feature calculator (We added grunt over their docker mechanism)
#       Maybe submit multiple jobs to demonstrate job handling

# Stream the output to the Classifer and retrive back a report

# Then use dcmqi and slicer to get some more features

# Stream them as well to the classifier and get a descision as well

# Perform N4 bias correction and used the riiply again and compare the resutls on the featues?

import sys
import os
sys.path.append("/Users//Dropbox/GRUNT__PYTHON/")
from pygrunt import grunt
import uuid
subdir = str(uuid.uuid4())
# Create a folder for all the temporary stuff and remove at the end
directory='/Users//Downloads/'+subdir+'/'

if not os.path.exists(directory):
    os.makedirs(directory)

print ('I am saving temporary things in: %s'%(directory))

# Lets Calculate some features

# So we need to have just the address of the grunt based docker... the responce we get back from the grunt service has anything we need.
# Although this runs from my local comuter the dockers can be located everywhere enabling collaboration between different institutions
print ('Example of responce')
g = grunt("http://0.0.0.0:9901")
print (g.services)
j=g.features
j.output='output.zip'
j.dicom='/Users//Downloads/Subjects/test.zip'
job =j()
# Commands can be executed synchronously or asynchronously
job.wait()
job.save_output("output",directory)
del j

# Lets apply a classifier!
directoryn=directory+'/nodule/'
if not os.path.exists(directoryn):
    os.makedirs(directoryn)

# So we need to have just the address of the grunt based docker... the responce we get back from the grunt service has anything we need.
# Although this runs from my local comuter the dockers can be located everywhere enabling collaboration between different institutions
print ('Example of responce')
g = grunt("http://0.0.0.0:9908")
print (g.services)
j=g.noduleclassifier
j.output='output.pdf'
j.dataset=directory+'/output.zip'
job =j()
# Commands can be executed synchronously or asynchronously
job.wait()
job.save_output("output",directoryn)
