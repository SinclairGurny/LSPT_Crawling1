from reppy.robots import Robots

#grab robots url
url = Robots.robots_url('https://science.rpi.edu/computer-science')

if 'http' in url:
    #print(url)
    robots = Robots.fetch(url)
    #print(robots)
    print(robots.allowed('https://science.rpi.edu/computer-science/', 'agent'))
    print(robots.allowed('https://science.rpi.edu/admin/', 'agent'))
