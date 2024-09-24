from aiokafka import AIOKafkaProducer
import asyncio

async def send_one():
    producer = AIOKafkaProducer(
        bootstrap_servers='192.168.137.1:9092')
    # Get cluster layout and initial topic/partition leadership information
    await producer.start()
    try:
        # Produce message
        print("Sending...")
        await producer.send_and_wait("my_topic", b"Hello from Karn")
    finally:
        # Wait for all pending messages to be delivered or expire.
        print("Finally...")
        await producer.stop()

asyncio.run(send_one())