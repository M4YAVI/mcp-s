import asyncio
from fastmcp import Client

client = Client("my_server.py")  # Connect to your server

async def call_tool(name: str):
    async with client:           # Open connection
        result = await client.call_tool("greet", {"name": name})  # Place order
        print(result)            # Receive result

asyncio.run(call_tool("Ford"))   # Execute the order


# ouput
```
>python client.py
CallToolResult(content=[TextContent(type='text', text='Hello, Ford!', annotations=None, meta=None)], structured_content={'result': 'Hello, Ford!'}, data='Hello, Ford!', is_error=False)
```
