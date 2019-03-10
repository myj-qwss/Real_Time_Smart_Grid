# Real_Time_Smart_Grid
Continuation of Smart Grid capstone project. The focus is on Wide Area Monitoring and Control (WAMC) systems, and anomaly detection. Primary objectives are to refine the user interface/WAMC, integrate cyber monitoring tools, develop a machine learning based anomaly detection algorithm and implement using parallel computing and Apache Spark, and design, build, test a remote controlled energy storage system (battery bank) for the power grid emulator. 


# Helpful Instructions

Setup Instructions:

        chmod +x setup.sh

        ./setup.sh

Instructions:

        make clean

        make

        ./battery_polling

Help:

        You get a "Unable blah blah /var/lib/dpkg/. is another process using it?

        Do:

                sudo lsof /var/lib/dpkg/lock

                        > take number under PID

                sudo kill <number>

                sudo rm /var/lib/dpkg/lock

                sudo dpkg --configure -a

        If that doesn't work -- youre on your own.


