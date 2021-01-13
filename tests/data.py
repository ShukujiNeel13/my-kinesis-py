REAL_KINESIS_DATA = {
    'Records': [
        {
            'kinesis': {
                'kinesisSchemaVersion': '1.0',
                'partitionKey': '{DEVID}',
                'sequenceNumber': '49613080621330485147153478696213622075206153825331183666',
                'data': 'eyJ0IjogIjIwMjEwMTEzMDgzMzIxIiwgIkRldlR5cGUiOiAiT0RSRFRSIiwgIkRldlN1YlR5cGUiOiAiMi45LjgiLCAidGltZSI6ICIyMDIxLTAxLTEzVDA4OjMzOjIxKzA1MzAiLCAidW5peFQiOiAxNjEwNTA3MDAxNTE5LCAiUmVnaW9uIjogIkFzaWEvS29sa2F0YSIsICJERVZJRCI6ICIwMWJlOGY0NGU1YzE0N2ExOTkyNGFmMjQ3ZWUxMTBlZiIsICJ2IjogeyJyc3NpIjogIi04OCIsICJhbW1fZXhwZWN0ZWQiOiAzLjc4MTY5MiwgImFtbV96c2NvcmUiOiAwLjQ0MjczMSwgImFtbSI6IDMuNzg1Mzk1LCAiYWxjX2V4cGVjdGVkIjogMC4xMDgzMDQsICJhbGNfenNjb3JlIjogMC40NzU1MTgsICJhbGMiOiAwLjExMDM5MiwgIm5vMl9leHBlY3RlZCI6IDEuMjA0ODIzLCAibm8yX3pzY29yZSI6IDAuMDAxNzI1LCAibm8yIjogMS4yMDQ4Mjd9LCAiREFTU09DIjogIjE5MTAyMDEwMjQ1MzI0NkYyODFGRTYxQyIsICJQSUQiOiAiNWQ1NWNmNjFiNzNkNGI0ZmE0YWE5ZjQzYzk5ZDVhYmQiLCAiSW5zSUQiOiAiNDU5YzI5YTdkNjc5NGY1ODhmOGE3NmRiNThhODhlNmMiLCAiRGlzcGxheSI6ICJBaXIgUXVhbGl0eSIsICJ1dGMiOiAxNjEwNTA3MDAxLCAiZXhwaXJlX2F0IjogMTYyNjA1OTAwMSwgImRvdyI6ICIzIiwgIm1vbnRoIjogIjAxIiwgImhvdXIiOiAiMDgiLCAiZG9tIjogIjEzIiwgIm1pbnV0ZSI6ICIzMyJ9',
                'approximateArrivalTimestamp': 1610507001.629
            },
            'eventSource': 'aws:kinesis',
            'eventVersion': '1.0',
            'eventID': 'shardId-000000000003:49613080621330485147153478696213622075206153825331183666',
            'eventName': 'aws:kinesis:record',
            'invokeIdentityArn': 'arn:aws:iam::520739359176:role/service-role/DataHandler-V2-role-lucnp0g9',
            'awsRegion': 'ap-southeast-1',
            'eventSourceARN': 'arn:aws:kinesis:ap-southeast-1:520739359176:stream/SmartClean-Processed-Data-Stream/consumer/DataHandlerV2:1610506920'
        },
        {
            'kinesis': {'kinesisSchemaVersion': '1.0', 'partitionKey': '{DEVID}', 'sequenceNumber': '49613080621330485147153478696342977137904919147024744498', 'data': 'eyJ0IjogIjIwMjEwMTEzMTEwMzIxIiwgIkRldlR5cGUiOiAiUFBMQ1RSIiwgIkRldlN1YlR5cGUiOiAidjIuMCIsICJ0aW1lIjogIjIwMjEtMDEtMTNUMTE6MDM6MjErMDgwMCIsICJ1bml4VCI6IDE2MTA1MDcwMDE2NjcsICJSZWdpb24iOiAiQXNpYS9TaW5nYXBvcmUiLCAiREVWSUQiOiAiMTkwNDMwMTQ0NjA1M0M3MUJGNjQyMzI4IiwgInYiOiB7Im91dF9jb3VudCI6ICIwIiwgImNvdW50IjogMC4wfSwgIkRBU1NPQyI6ICIxOTA0MzAxNDQ2MDUzQzcxQkY2NDIzMjgiLCAiUElEIjogIlRPSF9QQVlPSCIsICJJbnNJRCI6ICJUT0hfUEFZT0hfTDJfRkVNQUxFIiwgIkRpc3BsYXkiOiAiVXNhZ2UgQ291bnRlciIsICJ1dGMiOiAxNjEwNTA3MDAxLCAiZXhwaXJlX2F0IjogMTYyNjA1OTAwMSwgImRvdyI6ICIzIiwgIm1vbnRoIjogIjAxIiwgImhvdXIiOiAiMTEiLCAiZG9tIjogIjEzIiwgIm1pbnV0ZSI6ICIwMyJ9', 'approximateArrivalTimestamp': 1610507001.778},
            'eventSource': 'aws:kinesis',
            'eventVersion': '1.0',
            'eventID': 'shardId-000000000003:49613080621330485147153478696342977137904919147024744498',
            'eventName': 'aws:kinesis:record',
            'invokeIdentityArn': 'arn:aws:iam::520739359176:role/service-role/DataHandler-V2-role-lucnp0g9',
            'awsRegion': 'ap-southeast-1',
            'eventSourceARN': 'arn:aws:kinesis:ap-southeast-1:520739359176:stream/SmartClean-Processed-Data-Stream/consumer/DataHandlerV2:1610506920'
        }
    ]
}
