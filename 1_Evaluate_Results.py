import streamlit as st
from scipy.stats import chi2_contingency 
from scipy.stats import fisher_exact 
import pandas as pd
import statsmodels.stats as sm
import numpy as np
from pingouin import power_chi2

tab1, tab2 = st.tabs(["⚙︎ Test", "🔬 Detailed Results"])

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
            stat, p, dof, ex= chi2_contingency(cont_table, correction=False)
            phi_effect=np.sqrt(stat/(group_A+group_B))
            if phi_effect < 0.3:
                effect_string =  'small'
            elif phi_effect < 0.5:
                effect_string =  'medium'
            else:
                effect_string =  'large'
            # calculate odds ratio
            odds_ratio_xi = (num_pos_A*num_neg_B)/(num_neg_A*num_pos_B)
            # calculate power
            pwr = power_chi2(
                dof = dof,
                w = phi_effect,
                n = (group_A+group_B),
                power = None,
                alpha = significance_level
            )
            if p < significance_level:
                st.markdown(f'''
                # Chi-square Test of Independence
                
                The chi-square test of independence was conducted to assess the association between two categorical variables. 

                ### Results
                - Chi-square value: {round(stat,2)}
                - Degrees of freedom: {dof}
                - p-value: {round(p,4)}
                - Phi: {round(phi_effect,2)} (effect size)
                - Odds Ratio (OR): {round(odds_ratio_xi,2)}
                - Power: {round(pwr,3)}

                ### Interpretation

                The p-value of {round(p,4)} is less than the significance level of {significance_level}, indicating that there is a statistically significant difference between the two groups. The effect size (Phi) is {round(phi_effect,2)}, which is considered a ({effect_string}) effect. The odds ratio (OR) of {round(odds_ratio_xi,2)} suggests that there is a {round(odds_ratio_xi,2)} times higher odds of the outcome occurring in one group compared to the other. The power of the test is {round(pwr,3)}, which means that the test has a {round(pwr*100,1)}% probability of detecting a statistically significant effect if one exists.
                ''')
            else:
                st.markdown(f'''
                # Chi-square Test of Independence
                
                The chi-square test of independence was conducted to assess the association between two categorical variables. 

                ### Results
                - Chi-square value: {round(stat,2)}
                - Degrees of freedom: {dof}
                - p-value: {round(p,4)}
                - Power: {round(pwr,3)}

                ### Interpretation

                The p-value of {round(p,4)} is greater or equal to the significance level of {significance_level}, indicating that there is no statistically significant difference between the two groups. The power of the test is {round(pwr,3)}, which means that the test has a {round(pwr*100,1)}% probability of detecting a statistically significant effect if one exists.
                ''')


        else:
            odds_ratio_fi, p= fisher_exact(cont_table)
            if p < significance_level:
                st.markdown(f'''
                # Fisher's Exact Test

                The Fisher's exact test was conducted to assess the association between two categorical variables in a 2x2 contingency table. The Fisher's exact test was chosen because one or more of the values in the contingency table were lower or equal to 5, which would not meet the assumption of the chi-square test.

                ### Results
                - p-value: {round(p,4)}
                - Odds Ratio (OR): {round(odds_ratio_fi,2)}

                ### Interpretation

                The p-value of {round(p,4)} is less than the significance level of {significance_level}, indicating that there is a statistically significant difference between the two groups and rejecting the null hypothesis that there is no difference between the two groups. The odds ratio (OR) of {round(odds_ratio_fi,2)} suggests that there is a {round(odds_ratio_fi,2)} times higher odds of the outcome occurring in one group compared to the other.
               ''')
            else:
                st.markdown(f'''
                # Fisher's Exact Test

                The Fisher's exact test was conducted to assess the association between two categorical variables in a 2x2 contingency table. The Fisher's exact test was chosen because one or more of the values in the contingency table were lower or equal to 5, which would not meet the assumption of the chi-square test.

                ### Results
                - p-value: {round(p,4)}

                ### Interpretation

                The p-value of {round(p,4)} is greater or equal to the significance level of {significance_level}, indicating that there is no statistically significant difference between the two groups and failing to reject the null hypothesis that there is no difference between the two groups.
               ''')

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