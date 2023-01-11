import streamlit as st

st.markdown('''
### Statistical significance
In statistics, the significance level, also known as the alpha level, is a threshold used to determine whether the results of a hypothesis test are statistically significant. The significance level is typically set at 0.05, which means that there is a 5% chance that the results of the test are due to random chance, rather than a true effect. If the p-value, or the probability of observing the data given that the null hypothesis is true, is less than the significance level, the null hypothesis is rejected, and the alternative hypothesis is accepted. In other words, if the p-value is less than the significance level, it means that the results are unlikely to be due to chance and are considered statistically significant.
[https://openai.com/blog/chatgpt/]
'''
)

st.write('---')

st.markdown('''
### Effect size
In statistics, effect size is a measure of the strength of the relationship between two variables or the magnitude of the difference between two groups. It gives an idea of the size of the difference or relationship that is being observed, independent of sample size. The Effect Size can be described in various measures such as Cohen's d, Pearson's r and Hedge's g. These are used to express the effect size of a difference between two means, correlation between two variables and the like. Effect size is important because it allows researchers to compare the strength of results across studies and also to understand the real world impact of the results.
'''
)

st.markdown('''
The interpretation of effect size as small, medium, or large is based on a convention and it is not universally agreed upon. One commonly used convention for interpreting effect sizes is Cohen's d, where the effect size is classified as:
- Small: d = 0.2
- Medium: d = 0.5
- Large: d = 0.8
However, depending on the field of research, the threshold values may differ. Another convention used is r-value for Pearson correlation coefficient, where the effect size is classified as:
- Small: r = 0.1
- Medium: r = 0.3
- Large: r = 0.5
It's worth noting that these are just rough guidelines and the interpretation of effect size should also take into account the specific context and research question of your study. Therefore, It is important to compare the effect size with effect sizes of similar studies in the field of research and also to look at the real-world or practical impact of the effect size.
[https://openai.com/blog/chatgpt/]
'''
)

st.write('---')

st.markdown('''
### Statistical Power
In statistics, power is a measure of the probability of correctly rejecting the null hypothesis when the alternative hypothesis is true. It is the complement of the probability of making a type II error (i.e., failing to reject the null hypothesis when it is false). Power is an important concept in hypothesis testing, as it helps to determine the sample size needed to detect a true effect with a specified level of confidence. The higher the power, the greater the chance of detecting an effect when it exists. A commonly used target for power is 0.8, which means that the test has an 80% chance of detecting an effect when it exists. Power analysis can be used to determine the sample size required to achieve a desired level of power, given the magnitude of the effect, the significance level, and other factors.
[https://openai.com/blog/chatgpt/]
'''
)

