import streamlit as st
from pingouin import power_chi2
from math import ceil

with st.container():
    col1, col2, col3 = st.columns([1,2,3])
    with col1:
        # select desired alpha
        sig_lvl = st.radio(
            "Choose the desired level of significance: ",
            ('1%', '5%', '10%', '15%'), index=1
        )

        if sig_lvl == '1%':
            alpha = 0.01
        elif sig_lvl == '5%':
            alpha = 0.05
        elif sig_lvl == '10%':
            alpha = 0.10
        else:
            alpha = 0.15

    with col2:        
        # select desired power
        pwr = st.number_input(
            'Select desired statistical power: ',
            step = 0.10,
            value = 0.80,
            key = 'pwr'
        )

    with col3:        
        # select desired power
        phi = st.number_input(
            'Select desired effect size: ',
            step = 0.10,
            value = 0.50,
            key = 'phi'
        )
        st.write('---')
        st.write('Small: 0.10') 
        st.write('Medium: 0.30') 
        st.write('Large: 0.50')

# calculation
sample_size = power_chi2(
    dof = 1,
    w = phi,
    n = None,
    power = pwr,
    alpha = alpha
)

st.write('---')
st.markdown(f'''
### Needed sample size for a level of significance of {sig_lvl}, 
### an effect size of {round(phi,1)} and a power of {round(pwr,1)} is n={ceil(sample_size)} in each branch.
''')