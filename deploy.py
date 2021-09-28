import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

st.title('SARVAGNYA for DATASCIENCE Interview Preparation')
data= pd.read_csv(r'C:\Users\MMM-SM\21Pypractice\chatbot_project\participants\Questions_ans.csv')

# st.table(data.head())
# st.sidebar.title('Topic list')
# Topics = pd.Series(data.Labels.unique(), name='Topics')
# Topics.index = ["a",'b','c','d','e','f','g','h','i']
# st.sidebar.markdown('**Select any *one mnumeric option* from below: **')
# st.sidebar.table(Topics)
st.sidebar.title('Instructions')
st.sidebar.header('1. Options in main menu')
st.sidebar.markdown('* Anytime you want to **"EXIT"**, please type **"x"**')
st.sidebar.header('2. Options in submenu')
st.sidebar.markdown('* Press **"#"** to go back to the **"main menu"**')
st.sidebar.markdown('* Press **"?"** to list the **Questions** from the selected topic')
st.sidebar.markdown('* Anytime you want to **"EXIT"**, please type **"x"**')

flag = True
print(" ")
st.write('Hello There.....', end='\n\n')
st.write(
    '''My name is \033[1m\033[93m"Sarvagnya"\033[0m, I will help you through your \033[4mDATA SCIENCE INTERVIEW PREPERATION\033[0m....''',
    end='\n\n')
print('Anytime you want to \033[1m"EXIT"\033[0m, please type \033[1m"x"\033[0m', end='\n\n')
print('Select any one \033[4mnumeric option\033[0m from below:  ', end='\n\n')

Topics = pd.Series(data.Labels.unique(), name='Topics')
st.table(Topics)

while flag == True:
    user_response1 = st.text_input('Enter the Topic Number',value='', key='Topic no or X').lower()
    try:
        if user_response1 != 'x':

            a = Topics.values[int(user_response1)]
            print(" ")
            print(f'\033[1m\033[92mYOU SELECTED OPTION {user_response1} - \033[7m{a.upper()}\033[0m', end="\n\n")
            Questions_lst = data[data.Labels == a].loc[:, 'Questions']
            pd.set_option('display.max_colwidth', 80)
            st.write(
                '\033[1m*Select ANY ONE NUMERIC OPTION from below :- (\033[4mOR type "#" for Topics OR type "x" to Exit)\033[0m',
                end='\n\n')
            st.write(Questions_lst, end='\n\n')
            #             print('\t\033[1m\033[93mOR\033[0m',end='\n\n')
            #             print('\033[1mType "#" to go to Topics list\033[0m',end='\n\n')
            #             print('\t\033[1m\033[93mOR\033[0m',end='\n\n')
            #             print('\033[1mType "x" to Exit\033[0m',end='\n\n')

            while flag == True:
                user_response2 = st.text_input('Enter Question Number',value='', key='Question no or "#" or "X"')
                try:
                    if user_response2.lower() == 'x':
                        st.write('\n\033[7m THANKS FOR YOUR TIME, SEE YOU NEXT TIME.... \033[0m')
                        flag = False
                    elif user_response2 == '#':
                        print(" ")
                        st.write('\033[1m*Select ANY ONE NUMERIC OPTION from below :- (\033[4mOR type "x" to Exit)\033[0m',
                              end='\n\n')
                        st.write(Topics, end='\n\n')
                        #                         print('\t\033[1m\033[93mOR\033[0m',end='\n\n')
                        #                         print('\033[1mType "x" to Exit\033[0m',end='\n\n')
                        break
                    elif user_response2 == '?':
                        st.write(
                            '\033[1m*Select ANY ONE NUMERIC OPTION from below :- (\033[4mOR type "#" for Topics OR type "x" to Exit)\033[0m',
                            end='\n\n')
                        st.write(Questions_lst, end='\n\n')
                    #                         print('\t\033[1m\033[93m OR \033[0m',end='\n\n')
                    #                         print('\033[1mType "#" to go to Topics list\033[0m',end='\n\n')
                    #                         print('\t\033[1m\033[93mOR\033[0m',end='\n\n')
                    #                         print('\033[1mType "x" to Exit\033[0m',end='\n\n')

                    else:
                        b = Questions_lst[int(user_response2)]
                        st.write(f'\n\033[1mQUESTION {user_response2}:\033[0m \033[1m\033[93m\033[4m{b.upper()}\033[0m',
                              end='\n\n')
                        st.write(f'\033[7mAnswer:\033[0m', end='\n\n')
                        st.write(f'{data.values[int(user_response2)][1]}', end='\n\n')
                        st.write(f'\033[1mType "?" to see the Questions list\033[0m', end='\n\n')
                        print('\t\033[1m\033[93mOR\033[0m', end='\n\n')
                        print('\033[1mType "#" to go to Topics list\033[0m', end='\n\n')
                        print('\t\033[1m\033[93mOR\033[0m', end='\n\n')
                        print('\033[1mType "x" to EXIT\033[0m', end='\n\n')

                except:
                    print('\n\033[1m** select a valid option **\033[0m', end='\n\n')
        else:
            print('\n\033[7m THANKS FOR YOUR TIME, SEE YOU NEXT TIME.... \033[0m')
            flag = False

    except:
        print('\n\033[1m** Select a valid option.. **\033[0m', end='\n\n')
