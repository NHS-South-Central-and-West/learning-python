# TODO:

I want to add a version of the "ordered_months.ipynb" chart example as a function that people can import, rather than having to include that hefty 
bit of code.

It will likely be called **monthly_line_chart()** and will include some arguments that will allow some customisation e.g. setting the chart title. 
The **kwarg will be set as "title = None" in the function definition & there will be some logic in the function that creates a default title when
title = None e.g. "{y} by Month".