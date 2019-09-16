import threading
import Queue


class MultiThreading(threading.Thread):
    def __init__(self, function, *args, **kwargs):
        self._function = function
        self._args = args
        self._kwargs = kwargs
        self.__return = None
        threading.Thread.__init__(self, verbose=False)

    def __str__(self):
        s = list()
        s.append("function name: " + str(self._function))
        s.append("parameters: " + str(self._args))
        s.append("dictionary parms: " + str(self._kwargs))
        return '\n'.join(s)

    def run(self):
        try:
            self.__return = self._function(*self._args, **self._kwargs)
        except:
            pass

    def output(self):
        return self.__return


def doActionInParallel(*functionList):
    actionList = list()
    print("do_action_in_parallel() starts")
    if len(functionList) == 0:
        return
    if len(functionList) == 1:
        if type(functionList[0]) == type([]):
            for fun in functionList[0]:
                actionList.append(fun)
        else:
            actionList.append(functionList[0])
    else:
        if type(functionList[0]) != type([]):
            actionList.extend(functionList)
        else:
            # # not support
            return

    for action in actionList:
        if not isinstance(action, MultiThreading):
            continue
        action.start()

    for action in actionList:
        if not isinstance(action, MultiThreading):
            continue
        action.join()
que = Queue.Queue()
def add(a,b):
    print a+b
    que.put(a+b)
    return
L = [1,2,3,4,5,6]
i = 0
operations = list()
while i < len(L):
    j = i+1
    print j
    if j >= len(L):
        break
    thread = MultiThreading(add, L[i], L[j])
    operations.append(thread)
    i += 1
print operations
doActionInParallel(operations)
results = [que.get() for x in xrange(len(operations))]
print results


for i,z  in enumerate(L):
    print i,z