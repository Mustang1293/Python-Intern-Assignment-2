import subprocess, time

def runCommands(commandList): # Define a function to run the commands
    
    elapsed = []
    for c in commandList: # iterate through list of commands 
        start = time.clock() # start time of popen
        p = subprocess.Popen(c, shell=True) # create a subprocess that runs the list of commands
        end = time.clock() # end time of popen
        elapsed.append(end-start) #store the elapsed time of popen for each command in list

        while p.poll() == None: #check if subprocess is still running 
            p.terminate() # terminate running processes 
                 
    return elapsed # return list of process times

commands = ['sleep 3','ls -l /','find /','sleep 4','find /usr','date','sleep 5','uptime']
elapsed = []
for float in runCommands(commands): #iterate through the list returned by function
    elapsed.append(float) # append floating point times to new list

print('------------------------------Report Statistics------------------------------')
print('Total elapsed time: ' + str(sum(elapsed)))
print('Average: ' + str(sum(elapsed)/len(elapsed)) + ' / ' + 'Maximum: ' + str(max(elapsed)) + ' / ' + 'Minimum: ' + str(min(elapsed)))  
