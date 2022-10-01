'''


def todo_middleware(get_response):
    print("Code for initialization and Configuration")


    def todo_function(request):
        print("code is executed before view is called")
        response=get_response(request)
        print("code is executed after view is called")
        return response

    return todo_function
    '''



class todo_middleware:
    def __init__(self,get_response):
        self.get_response=get_response
        print("Code for initialization and Configuration")


    def __call__(self,request):
        print("code is executed before view is called")
        response=self.get_response(request)
        print("code is executed after view is called")
        return response
