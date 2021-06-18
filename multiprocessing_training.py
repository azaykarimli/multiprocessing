from multiprocessing import Process, current_process
import os

def square(number):
    result = number * number
    print("square root of " + str(number) +" " "is" " " + str(result))

    prproc = os.getpid()

    print("Proces id is :" + str(prproc))

    process_name = current_process().kill

    print(process_name)

    # burdaki processler spawn olunub curbandilar

if __name__ == '__main__':

   
    processes= []
    for number in range(1, 5):
        
        process = Process(target=square, args=(number,))
        processes.append(process)
        
        process.start()
        process.join()

# burdaki process parent dir atadir oglannigi 110du
        chproc = os.getpid()
        print(chproc)
        
