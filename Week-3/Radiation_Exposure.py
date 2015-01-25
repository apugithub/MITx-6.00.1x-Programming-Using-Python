###1st Appraoch:

def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):
    # FILL IN YOUR CODE HERE...
    if start >= stop - step:
        return f(stop-step) * step
    return (f(start) * step) + radiationExposure(start + step, stop, step)


  
  
  #### 2nd Appraoch:
  def radiationExposure(start, stop, step):
      total = 0.0;
      k = start;
      while(k<stop):
        total += step * f(k);
        k = k + step;
    return total;
    
    
    
    
    
    #####3rd Approach:
    
    def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)
    
def radiationExposure(start, stop, step):
    '''
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
 
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
      the step size will always partition the space evenly.

    returns: float, the amount of radiation exposed to 
      between start and stop times.
    '''

    if stop <= start:
        return 0
    else:
       return step * f(start) + radiationExposure(start + step, stop, step)
    
    
    
    
    
    ##### 4th Appraoch:
    
    def radiationExposure(start, stop, step):
    """
    Computes and returns the amount of radiation exposed
    to between the start and stop times. Calls the 
    function f (defined for you in the grading script)
    to obtain the value of the function at any point.
    
    start: integer, the time at which exposure begins
    stop: integer, the time at which exposure ends
    step: float, the width of each rectangle. You can assume that
        the step size will always partition the space evenly.
        
    returns: float, the amount of radiation exposed to 
        between start and stop times.
    """
    area = 0
    while start <  stop:
        area = area + f(start) * step
        start += step

    return area
