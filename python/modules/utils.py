import time

def Timer(nloops=1):

    def decorator(orig_func):
    
        def wrapper(*args, **kwargs):

            dts = []

            for i in range(nloops):
                t1 = time.time()
                result = orig_func(*args, **kwargs)
                t2 = time.time()
                dt = t2 - t1
                dts.append(dt)
            
            dt_avg = sum(dts)/nloops

            print('{} ran in: {} sec ({} loop avg)'.format(orig_func.__name__, dt_avg, nloops) )

            return result
    
        return wrapper
    return decorator
