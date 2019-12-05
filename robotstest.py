from reppy.robots import Robots

url = Robots.robots_url('https://science.rpi.edu/computer-science')
robots = Robots.fetch(url)

print(robots.allowed('https://science.rpi.edu/computer-science/', 'agent'))
print(robots.allowed('https://science.rpi.edu/admin/', 'agent'))
