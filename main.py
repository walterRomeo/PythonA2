# COS60016: Programming for Development
# Assignment 2: API ChatBot
# Code by Walter Rodas
# March 2023
import inspect
import asyncio
import time
from passwords import password_generator_min10
from UTEST import my_logger
from django.http import HttpResponse
from django.views import View
import json


alphaNumerical = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890"
allCharacters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM123456789!@#$%^&*()_+{}|>?<[];'\,./~`><"

# Wrapper to print arguments passed into a function
def printfunc_args(function):
    def wrapper_printfunc_args(*args):
        print("{0} is called with parameters {1}".format(function.__name__, args))
        return function(*args)

    return wrapper_printfunc_args


@printfunc_args
def add(x, y):
    return x + y


add(2, 2)


@my_logger
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))


display_info('Johnny', 20)


def digit_validation_decorator(function):
    def digit_validation_wrapper(*args):
        if not args[0].isdigit() or not args[1].isdigit():
            raise Exception("Both numbers have to be integers")
        else:
            first_input = int(args[0])
            second_input = int(args[1])
        if isinstance(first_input, int) and isinstance(first_input, int):
            return function(first_input, second_input)
        else:
            raise Exception("Both numbers have to be integers")

    return digit_validation_wrapper


max_characters = 15

password = password_generator_min10(max_characters, allCharacters)
print("Password: ", password)
print(password_generator_min10.__annotations__)

print(inspect.getfullargspec(password_generator_min10))


async def test_01():
    print("something")
    await asyncio.sleep(4)
    print("anything")

async def test_02():
    print("hi")
    await asyncio.sleep(1)
    print("Goodbyee")

async  def main():
    await asyncio.gather(test_01(), test_02(), test_01())

start = time.perf_counter()
asyncio.run(main())
execution_time = time.perf_counter() - start
print("Execution Time: "+ str(round(execution_time,2)) + "seconds")

async def test_03():
   print("Something")
   return await test_04()


async def test_04():
   print("Hi")
   return await test_05()


async def test_05():
   print("Walk")
   return await test_end()


async def test_end():
   print("Finished!")


async def main():
   await asyncio.gather(test_03(), test_05(), test_04(), test_05(), test_end())


time_start = time.time()
asyncio.run(main())
time_end = time.time()
print("Execution Time: " + str(round(time_end - time_start, 10)) + " seconds")

