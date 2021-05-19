#! /bin/bash
echo "hi"
cd /home/rahul/Desktop/Other_code
echo "Loading page..."
source env/bin/activate
cd Attendence
$(python Attendence.py)
deactivate

