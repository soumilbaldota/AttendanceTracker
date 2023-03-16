"""
@author: Soumil Baldota
"""
import os
import streamlit as st
import pandas as pd
import subprocess
import sys
def main():
	st.title('Attendance')

	email = st.text_input('Enter Email')
	password = st.text_input('Enter Password')

	if(st.button('Fetch Attendance')):
		subprocess.run([f'{sys.executable}',
										 'quikspidey.py',
										  '--email',
										  email,
										  '--password',
										   password
										 ])

		df = pd.read_html('data.html')
		st.dataframe(df[0])

if __name__ == '__main__':
	main()