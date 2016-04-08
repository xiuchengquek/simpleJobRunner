# A Simple JobRunner using Zeromq 
 
 
### Purpose 

The original code was written to beat the waiting time on the SGE cluster. 
I had to run 3000 jobs that took only around 2 to 3 mins each. 
Most of time was wasted on environment setups and the queue time.

Using zeromq on top of the SGE scheduler will allow me to run task directly on the compute node without going thru the SGE schduler
This is faciliated by submitting "workers" that recieves command from the ventitlator on the login node. 
Simple logging to done by running a sinker which recieves information from the worker.


### Requirements

1. Zeromq : zeromq library
2. Python - works on pyhon2.7.10
3. pyZMQ :  python api for zeromq


### How it works

Using python zmq library, the worker code will listen to a user defined tcp port and sends message to the sinker.
The port that the worker listens to will be the port that the ventillator will send to

In this version, the ventitlator will send the name of the bash script that you want to run.
The worker will run the bash script 
The worker will then send the outcome to sinker

### Diagram 

![alt text](https://github.com/imatix/zguide/raw/master/images/fig5.png "Zeromq Parrallel Image")



### More information 

1. [Zeormq Official Documentation]( http://zguide.zeromq.org/py:all )
2. [Real Application for Studying of RNAStructures](https://github.com/xiuchengquek/zeromq_rnadistance)


### How to run and test it yourself 

1. Clone the repo
```
git clone https://github.com/xiuchengquek/simpleJobRunner.git
```
2. Create a simple bash script
```
echo -e '#!/bin/bash\nls -l > results.txt'  > simple.sh
```
3. Gives it excutable permission
```
chmod +x simple.sh
```
4. Qsub the worker
    - you will need to find outthe ventitlator and sinker ip, you can find by running `hostname -i` .

```
qsub -cwd -b y -j y -pe smp 2 -V -N simpleWorker python simpleJobRunner/genericWorker.py <ventitlator_ip_and_port_here_> <sinker_up_and_port_here>
# example : qsub -cwd -b y -j y -pe smp 2 -V -N simpleWorker python simpleJobRunner/genericWorker.py tcp://123.456.789:5555 tcp://123.456.789:5556
```
5. Start the sinker
    - you will need to listen to the port that the the worker is sending to 
```
python simpleJobRunner/genericSinker.py <tcp_ip_and_port_here>_
# example :  python simpleJobRunner/genericSinker.py tcp://*:5558
```
6. Start sending your jobs using the ventilator
    - you will need to send it to the port that the worker is listening to
```
python  simpleJobRunner/genericVentilator.py  <worker_recieving_port_and_ip_>_ <sinker_recieving_ip_and_port> <bash_script_to_run>
# example python simpleJobRunner/genericVentilator.py  tcp://*:5555 tcp://localhost:5556 sample.sh
```







 
