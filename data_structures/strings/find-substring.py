# find the phone model info
user_agent = "Mozilla/5.0 (Linux; " \
             "Android 9; SM-N960F) " \
             "AppleWebKit/537.36 " \
             "(KHTML, like Gecko) " \
             "Chrome/91.0.4472.120 " \
             "Mobile Safari/537.36"

start = user_agent.find("(") + 1
end = user_agent.find(")")

print(user_agent[start:end])
