import lesson_checkup

if __name__ == '__main__':
    container = lesson_checkup.Splash()
    container.run()
    input("input something to stop container\n")
    container.stop()