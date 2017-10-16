
## Pandas Visualization and Plotting Tools.
Practical applications of the course
```Applied Plotting, Charting & Data representation in Python ```


```python statistical libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

%matplotlib inline
```
```python
plt.style.use('seaborn-colorblind')
```

DataFrame.Plot


```python
np.random.seed(123)
# create a data series plot with three columns
cumsum-cumulativy sums

df = pd.DataFrame({'A': np.random.randn(365).cumsum(0),
                   'B': np.random.randn(365).cumsum(0)+20,
                   'C': np.random.randn(365).cumsum(0)-20},
                 index= pd.date_range('1/1/2017', periods=365))

len(df) #365
df.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>A</th>
      <th>B</th>
      <th>C</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2017-01-01</th>
      <td>-1.085631</td>
      <td>20.059291</td>
      <td>-20.230904</td>
    </tr>
    <tr>
      <th>2017-01-02</th>
      <td>-0.088285</td>
      <td>21.803332</td>
      <td>-16.659325</td>
    </tr>
    <tr>
      <th>2017-01-03</th>
      <td>0.194693</td>
      <td>20.835588</td>
      <td>-17.055481</td>
    </tr>
    <tr>
      <th>2017-01-04</th>
      <td>-1.311601</td>
      <td>21.255156</td>
      <td>-17.093802</td>
    </tr>
    <tr>
      <th>2017-01-05</th>
      <td>-1.890202</td>
      <td>21.462083</td>
      <td>-19.518638</td>
    </tr>
  </tbody>
</table>
</div>



# simple plot


```python
df.plot(); #semi-colon to supress unwanted details on the plot
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_7_0.png)
# scattter plot


```python
df.plot('A', 'B', kind = 'scatter');
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_9_0.png)



```python
df.plot.scatter('A', 'C', c='B', s = df['B'], colormap='viridis');
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_10_0.png)


# sub plots


```python
ax = df.plot.scatter('A', 'C', c='B', s = df['B'], colormap='viridis');
ax.set_aspect('equal')
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_12_0.png)



```python
df.plot.box();
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_13_0.png)



```python
df.plot.hist(alpha=0.7);
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_14_0.png)



```python
df.plot.kde();
'''kernel density estimation (KDE) is a
way to estimate probability'''
```




    'kernel density estimation (KDE) is a \nway to estimate probability'




![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_15_1.png)


# Pandas plotting tools


```python
iris = pd.read_csv('iris.csv')

iris.head()
```




<div>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>SepalLength</th>
      <th>SepalWidth</th>
      <th>PetalLength</th>
      <th>PetalWidth</th>
      <th>Name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>5.1</td>
      <td>3.5</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>1</th>
      <td>4.9</td>
      <td>3.0</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>2</th>
      <td>4.7</td>
      <td>3.2</td>
      <td>1.3</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>3</th>
      <td>4.6</td>
      <td>3.1</td>
      <td>1.5</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5.0</td>
      <td>3.6</td>
      <td>1.4</td>
      <td>0.2</td>
      <td>Iris-setosa</td>
    </tr>
  </tbody>
</table>
</div>


# Scatter Matrix

```python
pd.tools.plotting.scatter_matrix(iris);
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_18_0.png)


# Parallel Coordinates
```python
plt.figure()
pd.tools.plotting.parallel_coordinates(iris, 'Name');
```


![png](https://github.com/4bic-attic/data_school/blob/data_school/coursera/resources/output_19_0.png)



```python

```
