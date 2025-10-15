import asyncio

#async does not mean multithreading , it's more like context switching done by os kernel  when multiple process are running
#here the multiple process are the different tasks basically , when  one task is in awaiting or idle due to i/o operartions over network
# or anything  the other task  doesn't have to wait , basicaly the process 2 will begin independently of process 1 which is idel or waitng for some resoursse
#

#This same concept is used in may libraries and frameworks just like we use threads in different puprpose in java.
# In web services built using  FastApi(spring boot/ java servlets equivalent) + uvicorn ( ASGI Server) the concurency model is
#fundamentally different forom java's thread per request model. The equivalent of the Java Web Container (Tomcat) is the ASGI Server (Uvicorn).
#Uvicorn starts a small number of worker processes (often 2-4 processes, depending on your CPU cores).
#Uvicorn Worker Processes (Parallelism): Uvicorn starts, for example, 4 worker processes.
# Each process runs independently and in parallel on different CPU cores.
# This is the multiprocessing part (like having 4 separate mini-Tomcats).Request Reception: The network traffic is distributed among these 4 worker processes.

#Corrected Summary
#Each Uvicorn worker process receives multiple concurrent requests and uses its single thread's asyncio loop to handle them all
# efficiently by cooperatively switching between the tasks (coroutines).
#So, if you have 4 worker processes, your machine is truly handling 4 separate threads in parallel, and each of those threads is
# handling a large number of requests concurrently via asyncio.


async def say_hello_async( ):
    await asyncio.sleep(2)  # Simulates waiting for 2 seconds
    print("Hello, Async World!")

async def do_something_else():
    print("Starting another task...")
    await asyncio.sleep(1)  # Simulates doing something else for 1 second
    print("Finished another task!")

async def main():
    # Schedule both tasks to run concurrently
    await asyncio.gather(
        say_hello_async(),
        do_something_else(),
    )

asyncio.run(main())