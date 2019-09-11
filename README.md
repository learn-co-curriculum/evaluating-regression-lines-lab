
# Evaluating Regression Lines Lab

### Introduction

In the previous lesson, we learned to evaluate how well a regression line estimated our actual data.  In this lab, we will turn these formulas into code.  In doing so, we'll build lots of useful functions for both calculating and displaying our errors for a given regression line and dataset.

> In moving through this lab, we'll access to the functions that we previously built out to plot our data, available in the [graph](https://github.com/learn-co-curriculum/evaluating-regression-lines-lab/blob/master/graph.py) here.

### Determining Quality

In the file, `movie_data.py` you will find movie data written as a python list of dictionaries, with each dictionary representing a movie.  The movies are derived from the first 30 entries from the dataset containing 538 movies [provided here](https://raw.githubusercontent.com/fivethirtyeight/data/master/bechdel/movies.csv).


```python
from movie_data import movies 
len(movies)
```

> Press shift + enter


```python
movies[0]
```


```python
movies[0]['budget']/1000000
```

The numbers are in millions, so we will simplify things by dividing everything by a million


```python
scaled_movies = list(map(lambda movie: {'title': movie['title'], 'budget': round(movie['budget']/1000000, 0), 'domgross': round(movie['domgross']/1000000, 0)}, movies))
scaled_movies[0]
```

Note that, like in previous lessons, the budget is our explanatory value and the revenue is our dependent variable.  Here revenue is represented as the key `domgross`.  

#### Plotting our data

Let's write the code to plot this data set.

As a first task, convert the budget values of our `scaled_movies` to `x_values`, and convert the domgross values of the `scaled_movies` to `y_values`.


```python
x_values = None
y_values = None
```


```python
x_values and x_values[0] # 13.0
```


```python
y_values and y_values[0] # 26.0
```

Assign a variable called `titles` equal to the titles of the movies.


```python
titles = None
```


```python
titles and titles[0]
```

Great! Now we have the data necessary to make a trace of our data.


```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, plot

movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')

plot([movies_trace])
```

#### Plotting a regression line

Now let's add a regression line to make a prediction of output (revenue) based on an input (the budget).  We'll use the following regression formula:

* $\hat{y} = m x + b$, with $m = 1.7$, and $b = 10$. 


* $\hat{y} = 1.7x + 10$

Write a function called `regression_formula` that calculates our $\hat{y}$ for any provided value of $x$. 


```python
def regression_formula(x):
    pass
```

Check to see that the regression formula generates the correct outputs.


```python
regression_formula(100) # 180.0
regression_formula(250) # 435.0
```

Let's plot the data as well as the regression line to get a sense of what we are looking at.


```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, m_b_trace, plot

if x_values and y_values:
    movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    regression_trace = m_b_trace(1.7, 10, x_values, name='estimated revenue')
    plot([movies_trace, regression_trace])
```

### Calculating errors of a regression Line

Now that we have our regression formula, we can move towards calculating the error. We provide a function called `y_actual` that given a data set of `x_values` and `y_values`, finds the actual y value, provided a value of `x`.




```python
def y_actual(x, x_values, y_values):
    combined_values = list(zip(x_values, y_values))
    point_at_x = list(filter(lambda point: point[0] == x,combined_values))[0]
    return point_at_x[1]
```


```python
x_values and y_values and y_actual(13, x_values, y_values) # 26.0
```

Write a function called `error`, that given a list of `x_values`, and a list of `y_values`, the values `m` and `b` of a regression line, and a value of `x`, returns the error at that x value.  Remember ${\varepsilon_i} =  y_i - \hat{y}_i$.  


```python
def error(x_values, y_values, m, b, x):
    pass
```


```python
error(x_values, y_values, 1.7, 10, 13) # -6.099999999999994
```

Now that we have a formula to calculate our errors, write a function called `error_line_trace` that returns a trace of an error at a given point.  So for a given movie budget, it will display the difference between the regression line and the actual movie revenue.

![](./error-line.png)

Ok, so the function `error_line_trace` takes our dataset of `x_values` as the first argument and `y_values` as the second argument.  It also takes in values of $m$ and $b$ as the next two arguments to represent the regression line we will calculate errors from. Finally, the last argument is the value $x$ it is drawing an error for.

The return value is a dictionary that represents a trace, and looks like the following:

```python
{'marker': {'color': 'red'},
 'mode': 'lines',
 'name': 'error at 120',
 'x': [120, 120],
 'y': [93.0, 214.0]}

```

The trace represents the error line above. The data in `x` and `y` represent the starting point and ending point of the error line. Note that the x value is the same for the starting and ending point, just as it is for each vertical line. It's just the y values that differ - representing the actual value and the expected value. The mode of the trace equals `'lines'`.


```python
def error_line_trace(x_values, y_values, m, b, x):
    pass
```


```python
error_at_120m = error_line_trace(x_values, y_values, 1.7, 10, 120)

# {'marker': {'color': 'red'},
#  'mode': 'lines',
#  'name': 'error at 120',
#  'x': [120, 120],
#  'y': [93.0, 214.0]}
error_at_120m
```

We just ran the our function to draw a trace of the error for the movie Elysium.  Let's see how it looks.


```python
scaled_movies[17]
```


```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)
from graph import trace_values, m_b_trace, plot
if x_values and y_values:
    movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    regression_trace = m_b_trace(1.7, 10, x_values, name='estimated revenue')
    plot([movies_trace, regression_trace, error_at_120m])
```

From there, we can write a function called `error_line_traces`, that takes in a list of `x_values` as an argument, `y_values` as an argument, and returns a list of traces for every x value provided.


```python
def error_line_traces(x_values, y_values, m, b):
    pass
```


```python
errors_for_regression = error_line_traces(x_values, y_values, 1.7, 10)
```


```python
errors_for_regression and len(errors_for_regression) # 30
```


```python
errors_for_regression and errors_for_regression[-1]

# {'x': [200.0, 200.0],
#  'y': [409.0, 350.0],
#  'mode': 'lines',
#  'marker': {'color': 'red'},
#  'name': 'error at 200.0'}
```


```python
from plotly.offline import iplot, init_notebook_mode
init_notebook_mode(connected=True)

from graph import trace_values, m_b_trace, plot

if x_values and y_values:
    movies_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    regression_trace = m_b_trace(1.7, 10, x_values, name='estimated revenue')
    plot([movies_trace, regression_trace, *errors_for_regression])
```

> Don't worry about some of the points that don't have associated error lines.  It is a complication with Plotly and not our functions.

### Calculating RSS

Now write a function called `squared_error`, that given a value of x, returns the squared error at that x value.

${\varepsilon_i}^2 =  (y_i - \hat{y}_i)^2$


```python
def squared_error(x_values, y_values, m, b, x):
    pass
```


```python
x_values and y_values and squared_error(x_values, y_values, 1.7, 10, x_values[0]) # 37.20999999999993
```

Now write a function that will iterate through the x and y values to create a list of squared errors at each point, $(x_i, y_i)$ of the dataset.


```python
def squared_errors(x_values, y_values, m, b):
    pass
```


```python
x_values and y_values and squared_errors(x_values, y_values, 1.7, 10)
```

Next, write a function called `residual_sum_squares` that, provided a list of x_values, y_values, and the m and b values of a regression line, returns the sum of the squared error for the movies in our dataset.


```python
def residual_sum_squares(x_values, y_values, m, b):
    pass
```


```python
residual_sum_squares(x_values, y_values, 1.7, 10) # 327612.2800000001
```

Finally, write a function called `root_mean_squared_error` that calculates the RMSE for the movies in the dataset, provided the same parameters as RSS.  Remember that `root_mean_squared_error` is a way for us to measure the approximate error per data point.


```python
import math
def root_mean_squared_error(x_values, y_values, m, b):
    return math.sqrt(residual_sum_squares(x_values, y_values, m, b)/len(x_values))
```


```python
root_mean_squared_error(x_values, y_values, 1.7, 10) # 104.50076235766578
```

#### Some functions for your understanding

Now we'll provide a couple functions for you.  Note that we can represent multiple regression lines by a list of m and b values:


```python
regression_lines = [(1.7, 10), (1.9, 20)]
```

Then we can return a list of the regression lines along with the associated RMSE.


```python
def root_mean_squared_errors(x_values, y_values, regression_lines):
    errors = []
    for regression_line in regression_lines:
        error = root_mean_squared_error(x_values, y_values, regression_line[0], regression_line[1])
        errors.append([regression_line[0], regression_line[1], round(error, 0)])
    return errors
```

Now let's generate the RMSE values for each of these lines.


```python
x_values and y_values and root_mean_squared_errors(x_values, y_values, regression_lines)
```

Now we'll provide a couple functions for you:
* a function called `trace_rmse`, that builds a bar chart displaying the value of the RMSE.  The return value is a dictionary with keys of `x` and `y`, both which point to lists.  The $x$ key points to a list with one element, a string containing each regression line's m and b value.  The $y$ key points to a list of the RMSE values for each corresponding regression line.


```python
import plotly.graph_objs as go

def trace_rmse(x_values, y_values, regression_lines):
    errors = root_mean_squared_errors(x_values, y_values, regression_lines)
    x_values_bar = list(map(lambda error: 'm: ' + str(error[0]) + ' b: ' + str(error[1]), errors))
    y_values_bar = list(map(lambda error: error[-1], errors))
    return dict(
        x=x_values_bar,
        y=y_values_bar,
        type='bar'
    )


x_values and y_values and trace_rmse(x_values, y_values, regression_lines)
```

Once this is built, we can create a subplot showing the two regression lines, as well as the related RMSE for each line.


```python
import plotly
from plotly.offline import iplot
from plotly import tools
import plotly.graph_objs as go

def regression_and_rss(scatter_trace, regression_traces, rss_calc_trace):
    fig = tools.make_subplots(rows=1, cols=2)
    for reg_trace in regression_traces:
        fig.append_trace(reg_trace, 1, 1)
    fig.append_trace(scatter_trace, 1, 1)
    fig.append_trace(rss_calc_trace, 1, 2)
    iplot(fig)
```


```python
### add more regression lines here, by adding new elements to the list
regression_lines = [(1.7, 10), (1, 50)]

if x_values and y_values:
    regression_traces = list(map(lambda line: m_b_trace(line[0], line[1], x_values, name='m:' + str(line[0]) + 'b: ' + str(line[1])), regression_lines))

    scatter_trace = trace_values(x_values, y_values, text=titles, name='movie data')
    rmse_calc_trace = trace_rmse(x_values, y_values, regression_lines)

    regression_and_rss(scatter_trace, regression_traces, rmse_calc_trace)
```

As we can see above, the second line (m: 1.0, b: 50) has the lower RMSE. We thus can conclude that the second line "fits" our set of movie data better than the first line. Ultimately, our goal will be to choose the regression line with the lowest RSME or RSS. We will learn how to accomplish this goal in the following lessons and labs.
