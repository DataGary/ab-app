import streamlit as st

st.markdown('''
### Statistical significance
In statistical hypothesis testing, a result has statistical significance when a result at least as "extreme" would be very infrequent if the null hypothesis were true. More precisely, a study's defined significance level, denoted by 
α, is the probability of the study rejecting the null hypothesis, given that the null hypothesis is true;
and the p-value of a result, p, is the probability of obtaining a result at least as extreme, 
given that the null hypothesis is true. 
The result is statistically significant, by the standards of the study, when 
p≤α. The significance level for a study is chosen before data collection, 
and is typically set to "5%" or much lower—depending on the field of study.
https://en.wikipedia.org/wiki/Statistical_significance
'''
)

st.write('---')

st.markdown('''
### Effect size
In statistics, an effect size is a value measuring the strength of the relationship between two variables in a population, or a sample-based estimate of that quantity.
[...]
Effect sizes complement statistical hypothesis testing, and play an important role in power analyses, sample size planning, and in meta-analyses.
https://en.wikipedia.org/wiki/Effect_size
'''
)

st.write('---')

st.markdown('''
### Statistical Power
In statistics, the power of a binary hypothesis test is the probability that the test correctly rejects the null hypothesis 
(H0) when a specific alternative hypothesis (H1) is true. 
It is commonly denoted by 1−β, and represents the chances of a true positive detection 
conditional on the actual existence of an effect to detect. 
Statistical power ranges from 0 to 1, and as the power of a test increases, 
the probability β of making a type II error by wrongly failing to reject the null hypothesis decreases.
https://en.wikipedia.org/wiki/Power_of_a_test
'''
)

