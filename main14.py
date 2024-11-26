import time
import asyncio


async def async_example(delay):
    print("Очікую...")
    await asyncio.sleep(delay)
    print("Завершено!")


async def another_async_function():
    print("Ще одна асинхронна задача почала виконання")
    await asyncio.sleep(1)
    print("Ще одна асинхронна задача завершила виконання")


async def main():
    tasks = [async_example(3), another_async_function()]
    await asyncio.gather(*tasks)

asyncio.run(main())


def sync_example(delay):
    print("Очікую...")
    time.sleep(delay)
    print("Завершено!")


def another_sync_function():
    print("Ще одна синхронна задача почала виконання")
    time.sleep(1)
    print("Ще одна синхронна задача завершила виконання")


def main():
    sync_example(3)
    another_sync_function()


main()
