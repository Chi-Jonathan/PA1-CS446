import sys
import os.path

def main():
	if len(sys.argv) != 3:
		print("Please provide command line arguments when running. \npython3 batchSchedulingComparison.py batchfile.txt Priority")
		return 1
	if (os.path.exists(sys.argv[1])):
		with open(sys.argv[1], "r") as f:
			data = f.read().splitlines()
		fdata = []
		for line in data:
			fdata.append([int(n) for n in line.split(", ")])
	else:
		print("Input batchfile not found!")
		return 1
	if sys.argv[2] == "ShortestRemaining":
		#ShortestRemainingSort(datadict)
		print("fjka")
	elif sys.argv[2] == "Priority":
		pid, time_completed = PrioritySort(fdata)
		burst_times = []
		arrival_times = []
		for i in range(len(fdata)):
			burst_times.append(fdata[i][2])
		for i in range(len(fdata)):
			arrival_times.append(fdata[i][1])  
		avg_tat, tat, avg_wt, wt = ComputeStat(time_completed, arrival_times, burst_times) 
		print("\nPID ORDER OF EXECUTION: \n")
		for i in range(len(pid)):
			print(pid[i])
		print("\nAverage Process Turnaround Time: ", avg_tat)
		print("Average Process Wait TIme: ", avg_wt)
	else:
		print("Unidentified sorting algorithm. Please input either ShortestRemaining or Priority.")
		return 1

def ComputeStat(processCompletionTimes, processArrivalTimes, processBurstTimes):
	count = len(processArrivalTimes)
	wt = sum(processCompletionTimes) - processCompletionTimes[count-1] - sum(processArrivalTimes)
	avg_wt = wt/count
	tat = wt + sum(processBurstTimes)
	avg_tat = tat/count
	return avg_tat, tat, avg_wt, wt
	
#def ShortestRemainingSort(batchFileData):

def PrioritySort(batchFileData):
	process_count = len(batchFileData)
	batchFileData = sorted(batchFileData, key = lambda batchFileData:batchFileData[1])
	time = 0
	check = True
	completed = 0
	completed_proc = []
	pid = []
	time_completed = []
	while(completed != process_count):
		waiting_processes = []
		for i in range(process_count): #remember u did a -1 here could mess you up in the future, and it probably will you idiot
			if (batchFileData[i][1]<=time) and (batchFileData[i] not in completed_proc):
				waiting_processes.append(batchFileData[i])
		waiting_processes = sorted(waiting_processes, key = lambda waiting_processes:waiting_processes[3])
		pid.append(waiting_processes[0][0])
		time+=waiting_processes[0][2]
		time_completed.append(time)
		completed_proc.append(waiting_processes[0])
		completed+=1

	return pid, time_completed

if __name__ == "__main__":
	main()