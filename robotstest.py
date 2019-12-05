from reppy.robots import Robots

# This utility uses `requests` to fetch the content
robots = Robots.fetch("https://science.rpi.edu/robots.txt")
print(robots.allowed('https://science.rpi.edu/computer-science/', 'agent'))
print(robots.allowed('https://science.rpi.edu/admin/', 'agent'))
