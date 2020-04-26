# Komachizan (Japanese mathematic puzzle)

Make 100 by putting "+ - * /" between "1 2 3 4 5 6 7 8 9" .

[15 Answers](https://github.com/go125/ten_puzzle/blob/8f8882694d3ab26cfaf9d090b73b924543047bc6/main.ipynb) when " " (blank) is not allowed.

```
 '1*2*3*4+5+6+7*8+9',
 '1-2+3*4*5+6*7+8-9',
 '1-2+3*4*5-6+7*8-9',
 '1+2+3+4+5+6+7+8*9',
 '1*2*3+4+5+6+7+8*9',
 '1-2*3+4*5+6+7+8*9',
 '1+2*3+4*5-6+7+8*9',
 '1-2*3-4+5*6+7+8*9',
 '1+2-3*4+5*6+7+8*9',
 '1+2*3*4*5/6+7+8*9',
 '1*2*3*4+5+6-7+8*9',
 '1-2*3-4-5+6*7+8*9',
 '1+2-3*4-5+6*7+8*9',
 '1+2+3-4*5+6*7+8*9',
 '1*2*3-4*5+6*7+8*9'
```

[101 Answers](https://github.com/go125/ten_puzzle/blob/bdf67f02c780e9feec2ae08ff76737e3ce338adc/main.ipynb) when " " (blank) is allowed.

```
'12+34+5*6+7+8+9',
 '1+23-4+56+7+8+9',
 '1/2/3*456+7+8+9',
 '1*2+34+5+6*7+8+9',
 '12+34-5+6*7+8+9',
 '1-2-3+45+6*7+8+9',
 '1+2*3+4+5+67+8+9',
 '12+3-4+5+67+8+9',
 '1-2+3*4+5+67+8+9',
 '1-2-3+4*5+67+8+9',
 '12*3-4*5+67+8+9',
 '1+23*4+5-6+7-8+9',
 '1*2+34+56+7-8+9',
 '1+2+3*4*56/7-8+9',
 '1*23+4+5+67-8+9',
 '1+2+34-5+67-8+9',
 '12+3*4+5+6+7*8+9',
 '1*2*3*4+5+6+7*8+9',
 '12-3+4*5+6+7*8+9',
 '1*2+34+5-6+7*8+9',
 '12+34-5-6+7*8+9',
 '1-2-3+45-6+7*8+9',
 '12-3-4+5*6+7*8+9',
 '1*23+4+56/7*8+9',
 '1*23*4-56/7/8+9',
 '1+2+3-4+5+6+78+9',
 '1*2*3-4+5+6+78+9',
 '1*2+3*4+5-6+78+9',
 '12+3*4-5-6+78+9',
 '1*2*3*4-5-6+78+9',
 '1*2-3+4*5-6+78+9',
 '1+2+3*4*5/6+78+9',
 '1+2*34-56+78+9',
 '1+234*5*6/78+9',
 '1+23*4-5+6+7+8-9',
 '123-4-5-6-7+8-9',
 '1-2+3*4*5+6*7+8-9',
 '123+4*5-6*7+8-9',
 '1+23*4+56/7+8-9',
 '123+45-67+8-9',
 '12/3+4*5*6-7-8-9',
 '1*2*34+56-7-8-9',
 '1*2+3+45+67-8-9',
 '1-2+3+45+6+7*8-9',
 '1-2+3*4*5-6+7*8-9',
 '12/3+4*5*6*7/8-9',
 '1+23-4+5+6+78-9',
 '1*2+3+4*5+6+78-9',
 '12*3-4+5-6+78-9',
 '1*2+3-4+5*6+78-9',
 '12/3/4+5*6+78-9',
 '1+2+3+4+5+6+7+8*9',
 '1*2*3+4+5+6+7+8*9',
 '1+23-4-5+6+7+8*9',
 '1-2*3+4*5+6+7+8*9',
 '12*3-4-5-6+7+8*9',
 '1+2*3+4*5-6+7+8*9',
 '1-2*3-4+5*6+7+8*9',
 '1+2-3*4+5*6+7+8*9',
 '1+2*3*4*5/6+7+8*9',
 '1-2-34+56+7+8*9',
 '1/2*3/4*56+7+8*9',
 '12+3*4+5+6-7+8*9',
 '1*2*3*4+5+6-7+8*9',
 '12-3+4*5+6-7+8*9',
 '1*2+34+5-6-7+8*9',
 '12+34-5-6-7+8*9',
 '1-2-3+45-6-7+8*9',
 '12-3-4+5*6-7+8*9',
 '1-2*3-4-5+6*7+8*9',
 '1+2-3*4-5+6*7+8*9',
 '1+2+3-4*5+6*7+8*9',
 '1*2*3-4*5+6*7+8*9',
 '1+23-4+56/7+8*9',
 '1*2+34-56/7+8*9',
 '1-2-3+4*56/7+8*9',
 '1+2+3-45+67+8*9',
 '1*2*3-45+67+8*9',
 '1+2+34*5+6-7-8*9',
 '1+234-56-7-8*9',
 '1*234+5-67-8*9',
 '1*2-3+4-5+6+7+89',
 '1+2*3-4-5+6+7+89',
 '1-23+4*5+6+7+89',
 '12-3-4+5-6+7+89',
 '1+2+3*4-5-6+7+89',
 '1-23-4+5*6+7+89',
 '1*2/3+4*5/6+7+89',
 '1/2*34-5+6-7+89',
 '12+3+4+5-6-7+89',
 '1*23-4+5-6-7+89',
 '12/3+4*5-6-7+89',
 '1-23-4-5+6*7+89',
 '1*2-3+4+56/7+89',
 '1+2*3-4+56/7+89',
 '12+3+4-56/7+89',
 '1*23-4-56/7+89',
 '123-45-67+89',
 '1+234*5/6-7-89',
 '12+3*45+6*7-89',
 '123+4-5+67-89'
```

17238 Answers when "(" and ")" are allowed.

Please see [aligned.csv](https://github.com/go125/ten_puzzle/blob/master/aligned.csv).

## How to make aligned.csv

### 1. Execute "main.py".

You can get "result_long.csv" and "result.csv".

"result_long.csv" contains a lot of same data.

"result.csv" doesn't contain same data, but it's not aligned.

When you execute "main.py", you also get "log.txt" as a log.

If you want to know more about "main.py", "tutrial.ipynb" provides more information about "main.py".

### 2. Execute "make_aligned_result_file.ipynb".

You can get "aligned.csv".

"aligned.csv" doesn't contain same data and it's aligned. 

By opening "check_formula_value.csv" in the Excel, you can check if the all formulas' values are 100.

