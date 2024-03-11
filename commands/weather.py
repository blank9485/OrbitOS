from termcolor import colored as c

def cmd(args):
    print(c("Weather for new York", "green"))
    print(c("temperature: 25°C", "red"))
    print(c("humidity: 50%", "blue"))
    print(c("wind speed: 10km/h", "yellow"))
    print(c("sunrise: 6:00 AM", "green"))
    print(c("sunset: 6:00 PM", "red"))