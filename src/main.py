import engine.engine as e

def main():
    game = e.Engine("DawnRPG", 1024, 768)
    game.start()


if __name__ == '__main__':
    main()