import requests
import json

# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def main():
    url = "http://ctabustracker.com/bustime/api/v3/getroutes?key=Tj9WE7DKXiMKP2sqajC8nLSgz&format=json"
    response = requests.get(url)
    print(response)
    print(response.json())
    response_json = response.json()
    data = json.dumps(response_json)
    print('\n')
    x = 0
    for routes in data:
        print(routes[0])
        #for rt_prop in routes[x]:
           # print(rt_prop[0] + rt_prop[1] + rt_prop[2] + rt_prop[3])
    x = x + 1
    #print(response_json)
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
