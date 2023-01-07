import streamlit as st
from scipy.stats import chi2_contingency 
from scipy.stats import fisher_exact 
import pandas as pd
import statsmodels.stats as sm
import numpy as np
from pingouin import power_chi2

tab1, tab2 = st.tabs(["⚙︎ Test", "🔬 Stats"])

with tab1:
    st.markdown('''
    ## Evaluate your experiment.
    '''
    )

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
            min_value=0,
            key = 'group_size_A')

        # Input average response percentage for target group A
        response_rate_A = st.number_input(
            'Input conversion rate in percent (%)', 
            min_value=0.0, 
            max_value=100.0,
            step = 1.0,
            value = 50.0,
            key = 'response_rate_A')

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
            min_value=0,
            key = 'group_size_B')

        # Input average response percentage for target group A
        response_rate_B = st.number_input(
            'Input conversion rate in percent (%)', 
            min_value=0.0, 
            max_value=100.0,
            step = 1.0,
            value=50.0,
            key = 'response_rate_B')

    # prepare values for chi-squared test
    num_pos_A = round(group_A * response_rate_A / 100)
    num_pos_B = round(group_B * response_rate_B / 100)

    num_neg_A = group_A - num_pos_A
    num_neg_B = group_B - num_pos_B

    with st.container():
        col1, col2 = st.columns([1,2])
        with col1:
            sig_lvl = st.radio(
            "Choose the level of significance:",
            ('1%', '5%', '10%', '15%'), index=1)

            # create contingency table
            cont_table = [[num_pos_A, num_neg_A], [num_pos_B, num_neg_B]]
        with col2:
            st.markdown('''
            ### Contingency Table:
            '''
            )

            d = {'A' : [num_pos_A, num_neg_A], 'B' : [num_pos_B, num_neg_B]}
            cont_df = pd.DataFrame(data = d, index = ['converted', 'not converted'])
            cont_df

    st.markdown('---')

    if sig_lvl == '1%':
        significance_level = 0.01
    elif sig_lvl == '5%':
        significance_level = 0.05
    elif sig_lvl == '10%':
        significance_level = 0.10
    else:
        significance_level = 0.15

    with tab2:
        # check if sample size too small for chi-square test
        # in that case use fisher exact test

        if num_pos_A > 5 and num_pos_B > 5 and num_neg_A > 5 and num_neg_B > 5:
            st.markdown('**Chi-square test of independence of variables in a contingency table.**')
            stat, p, dof, ex= chi2_contingency(cont_table, correction=False)
            st.write(f'Chi-square value: {round(stat,2)}') 
            st.write(f'p-value: {round(p,4)}') 
            st.write(f'Degrees of freedom: {dof}') 
            # st.write(f'Expected: {ex}')
            # calculate effect size
            phi_effect=np.sqrt(stat/(group_A+group_B))
            if phi_effect < 0.3:
                st.write(f'Phi: {round(phi_effect,2)} (small effect)')
            elif phi_effect < 0.5:
                st.write(f'Phi: {round(phi_effect,2)} (medium effect)')
            else:
                st.write(f'Phi: {round(phi_effect,2)} (large effect)')
            # calculate odds ratio
            odds_ratio_xi = (num_pos_A*num_neg_B)/(num_neg_A*num_pos_B)
            st.write(f'Odds Ratio (OR): {round(odds_ratio_xi,2)}')
            # calculate power
            pwr = power_chi2(
                dof = dof,
                w = phi_effect,
                n = (group_A+group_B),
                power = None,
                alpha = significance_level
            )
            st.write(f'Power: {round(pwr,4)}')
        else:
            st.markdown('**Fisher exact test on a 2x2 contingency table.**')
            odds_ratio_fi, p= fisher_exact(cont_table)
            st.write(f'p-value: {round(p,4)}')
            st.write(f'Odds Ratio (OR): {round(odds_ratio_fi,2)}')
            # TO DO: implement other metrics for fisher exact
            

    # eval test
    if p <= significance_level:
        if num_pos_A > 5 and num_pos_B > 5 and num_neg_A > 5 and num_neg_B > 5:
            st.markdown('''
            # ✅ Group A & Group B *have significantly* different conversion rates!
            ''')
            st.write('---')
            st.markdown(f'### Effect size: {round(phi_effect,2)}')
            st.write('Small: 0.10') 
            st.write('Medium: 0.30') 
            st.write('Large: 0.50')
        else:
            st.markdown('''
            # ✅ Group A & Group B *have significantly* different conversion rates!
            ''')
            st.write('---')
            st.markdown(f'### Effect size in terms of odds ratio: {round(odds_ratio_fi,2)}')
            st.markdown('The further away from 1, the bigger the effect.')
    else: 
        st.markdown('''
        # ❌ Group A & Group B do *not* have significantly different conversion rates!
        ''')