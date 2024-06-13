"""Package imports"""
from asyncio import create_task, run, gather

"""Source imports"""
from src.ministerio import ministerio_mulheres, ministerio_direitos_humanos, ministerio_saude

async def main():
    task1 = create_task(ministerio_mulheres())
    task2 = create_task(ministerio_direitos_humanos())
    # task3 = create_task(ministerio_saude())
    
    # await gather(task1, task2, task3)
    await gather(task1)

if __name__ == "__main__":
    run(main())
