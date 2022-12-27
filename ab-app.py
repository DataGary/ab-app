import streamlit as st
from scipy.stats import chi2_contingency 
from scipy.stats import fisher_exact 
import pandas as pd

sig_lvl = st.sidebar.radio(
"Choose the level of significance:",
('1%', '5%', '10%', '15%'), index=1)

col1, col2 = st.columns(2)

with col1:
    st.markdown('''
    ### Setup A:
    '''
    )

    # Input target group A
    group_A = st.number_input(
        'Input size of group A: ',
        step = 5,
        value = 100,
        key = 'group_size_A')

    # Input average response percentage for target group A
    response_rate_A = st.number_input(
        'Input response rate in percent', 
        min_value=0.0, 
        max_value=100.0,
        step = 1.0,
        value = 50.0,
        key = 'response_rate_A')  
    st.write(response_rate_A, ' %')

with col2:
    st.markdown('''
    ### Setup B:
    '''
    )

    # Input target group A
    group_B = st.number_input(
        'Input size of group B: ',
        step = 5,
        value=100,
        key = 'group_size_B')

    # Input average response percentage for target group A
    response_rate_B = st.number_input(
        'Input response rate in percent', 
        min_value=0.0, 
        max_value=100.0,
        step = 1.0,
        value=50.0,
        key = 'response_rate_B')  
    st.write(response_rate_B, ' %')

# prepare values for chi-squared test
num_pos_A = round(group_A * response_rate_A / 100)
num_pos_B = round(group_B * response_rate_B / 100)

num_neg_A = group_A - num_pos_A
num_neg_B = group_B - num_pos_B

# create contingency table
cont_table = [[num_pos_A, num_neg_A], [num_pos_B, num_neg_B]]

st.markdown('''
### Contingency Table:
'''
)

d = {'A' : [num_pos_A, num_neg_A], 'B' : [num_pos_B, num_neg_B]}
cont_df = pd.DataFrame(data = d, index = ['response', 'no response'])
cont_df


st.sidebar.markdown('---')

# check if sample size too small for chi-square test
# in that case use fisher exact test

if num_pos_A > 5 and num_pos_B > 5 and num_neg_A > 5 and num_neg_B > 5:
    st.sidebar.markdown('**Chi-square test of independence of variables in a contingency table.**')
    stat, p, dof, ex= chi2_contingency(cont_table)
    st.sidebar.write(f'Statistic Value: {stat}') 
    st.sidebar.write(f'p-value: {p}') 
    st.sidebar.write(f'Degrees of Freedom: {dof}') 
    st.sidebar.write(f'Expected: {ex}')
else:
    st.sidebar.markdown('**Fisher exact test on a 2x2 contingency table.**')
    odd_ratio, p= fisher_exact(cont_table)
    st.sidebar.write(f'Odds ratio: {odd_ratio}') 
    st.sidebar.write(f'p-value: {p}')

st.markdown('---')

if sig_lvl == '1%':
    significance_level = 0.01
elif sig_lvl == '5%':
    significance_level = 0.05
elif sig_lvl == '10%':
    significance_level = 0.10
else:
    significance_level = 0.15

##st.write("p value: " + str(round(p,2)))
if p <= significance_level: 
    st.markdown('**Group A & Group B have significantly different response rates!**') 
else: 
    st.markdown('**Group A & Group B do *not* have significantly different response rates!**')
