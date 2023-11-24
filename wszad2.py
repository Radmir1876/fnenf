#1

# import asyncio
# import time
#
# async def fast_operation(a, b):
#     result = a + b
#     print(f"Fast operation result: {result}")
#
# async def slow_operation(a):
#     # Медленная операция (заменена на a**2 для примера)
#     result = a ** 2
#     print(f"Slow operation result: {result}")
#
# async def main():
#     # Запускаем обе операции параллельно
#     task1 = asyncio.create_task(fast_operation(2, 3))
#     task2 = asyncio.create_task(slow_operation(5))
#
#     # Ожидаем завершения обеих операций
#     await asyncio.gather(task1, task2)
#
# # Выполняем асинхронную функцию main()
# start_time = time.time()
# asyncio.run(main())
# end_time = time.time()
#
# execution_time = end_time - start_time
# print(f"Total execution time: {execution_time} seconds")

#2
# import os
#
#
# def print_reps(directory):
#     for root, dirs, files in os.walk(directory):
#         level = root.replace(directory, '').count(os.sep)
#         indent = ' ' * 4 * (level)
#         print('{}{}/'.format(indent, os.path.basename(root)))
#         subindent = ' ' * 4 * (level + 1)
#         for f in files:
#             print('{}{}'.format(subindent, f))
#
#
# print_reps('твой путь к папке venv')


