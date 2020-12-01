"""
Scenario
Now that the competition gets tough it will Sort out the men from the boys .
Men are the Even numbers and Boys are the odd

Task
Given an array/list [] of n integers , Separate The even numbers from the odds , or Separate the men from the boys

Notes
Return an array/list where Even numbers come first then odds
Since , Men are stronger than Boys , Then Even numbers in ascending order While odds in descending .
Array/list size is at least *4*** .
Array/list numbers could be a mixture of positives , negatives .
Have no fear , It is guaranteed that no Zeroes will exists .

Input >> Output Examples:
menFromBoys ({7, 3 , 14 , 17}) ==> return ({14, 17, 7, 3}) 
menFromBoys ({-94, -99 , -100 , -99 , -96 , -99 }) ==> return ({-100 , -96 , -94 , -99})
menFromBoys ({49 , 818 , -282 , 900 , 928 , 281 , -282 , -1 }) ==> return ({-282 , 818 , 900 , 928 , 281 , 49 , -1})
"""

def men_from_boys(arr):
    mens = sorted([i for i in set(arr) if i%2==0])
    boys = sorted(list(set(arr) - set(mens)), reverse=True)
    return mens + boys