def makeTrigger(triggerMap, triggerType, params, name):
    print triggerMap, triggerType, params, name
    aa = raw_input()
    '''if triggerType == 'SUBJECT':
        trigger = SubjectTrigger(' '.join(params))
    elif triggerType == 'TITLE':
        trigger = TitleTrigger(' '.join(params))
    elif triggerType == 'PHRASE':
        trigger = PhraseTrigger(' '.join(params))
    elif triggerType == 'AND':
        trigger = AndTrigger(' '.join(params))
    elif triggerType == 'OR':
        trigger = OrTrigger(' '.join(params))
    elif triggerType == 'NOT':
        trigger = NotTrigger(' '.join(params))'''
        
    #triggerMap[name] = trigger
    #return trigger
def readTriggerConfig(filename):
    """
    Returns a list of trigger objects
    that correspond to the rules set
    in the file filename
    """

    # Here's some code that we give you
    # to read in the file and eliminate
    # blank lines and comments
    triggerfile = open(filename, "r")
    all = [ line.rstrip() for line in triggerfile.readlines() ]
    lines = []
    for line in all:
        if len(line) == 0 or line[0] == '#':
            continue
        lines.append(line)

    triggers = []
    triggerMap = {}

    # Be sure you understand this code - we've written it for you,
    # but it's code you should be able to write yourself
    for line in lines:

        linesplit = line.split(" ")
        print "linesplit ", linesplit
        # Making a new trigger
        if linesplit[0] != "ADD":
            trigger = makeTrigger(triggerMap, linesplit[1],
                                 linesplit[2:], linesplit[0])

        # Add the triggers to the list
        else:
            for name in linesplit[1:]:
                print "l1: ", linesplit[1:]
                print "name ", name, triggerMap[name]
                aa = raw_input()
                triggers.append(triggerMap[name])

    return triggers

readTriggerConfig('triggers.txt')