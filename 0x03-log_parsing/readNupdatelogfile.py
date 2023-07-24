async def log_reader():
    with open(LOG_PATH, "r", encoding='utf-8', errors='ignore') as logfile:
        logfile.seek(0, os.SEEK_END)
        while True:
            line = logfile.readline()
            if not line:
                await asyncio.sleep(0.2)
                continue
            # do stuff
