#%% [markdown]
## Will ACB be confirmed before Election Day?
### Reference
#
#- Prediction Market: Metaculus
#- Link: [here](https://www.metaculus.com/questions/5298/acb-confirmed-before-november-3-2020/)
#- Close Date: 2020-10-14
### Initial Prediction
#*updated 2020-09-27*
#### Thought processs
#The relevant sub-questions I can see here are:
#
#1. How often are Supreme Court nominees confirmed once nominated? What does this figure look like conditional on the Senate and Presidency both being held by the same party?
#2. What is the mortality rate for on average person that fits Barrett's demographics?
#3. How long does the nomination process usually take?
#
#From a more qualitative read of the process, based on public statements the following things seem relevant:
#
#- The votes exist to confirm.
#- Senate Leader says this will happen before the election.
#- Senate Minority Leader says they will try to slow this down procedurally as much as possible.
#### Reference Classes
#The Senate has a list of all SCOTUS nominations and thier outcomes [here](https://www.senate.gov/legislative/nominations/SupremeCourtNominations1789present.htm). Of 163 nominations for the Court, 126 were confirmed. Some that were confirmed declined to serve, but that is irrelevant to the question. This [Congressional Research Service report](https://www.everycrsreport.com/files/20160316_IN10458_798cc145841968d0dc9b74f1c3ff9d143f7012f6.pdf) breaks down nomination outcomes by party control from 1946-2016. Adjusting for the 2 SCOTUS nomination processes post-2016, when a party controls both the Senate and the Presidency 19 out of 22 nominations were confirmed. Conditioning on undivided government and the past ~century seems more appropriate here.
#
#According to [this data pull from the CDC](https://wonder.cdc.gov/controller/datarequest/D76;jsessionid=7C5F0B56D47CB8962015E7F22182), the average national mortality rate for a 48 year old white woman between 1999 and 2018 was ~.002. Very low, would not expect this to weigh heavily on the calc.
# 
#Per [this article](https://www.cnbc.com/2020/09/25/how-long-to-confirm-supreme-court-justice.html), since 1975 only 3 successful confirmations have occured in the time window between nomination and the election (39 days). This seems like an accurate representation of the past but do not believe it to hold as much weight given the current political context.

#### Other Sources
#- Predictit is about ~87% that the confirmation vote will happen before the election. 
#### Model(s)
#%%
undivided_gov_nomination = 19/22
general_mortality = 1-(3550/1353143)
confirmation_window = .87

undivided_gov_nomination * general_mortality * confirmation_window

#%% [markdown]
#### Prediction
#Adjusting the references classes upwards due to the context names above moves a ~75% to an ~85%. 