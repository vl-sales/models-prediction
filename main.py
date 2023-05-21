from src.app import create_app
import sys
import logging
logging.basicConfig(level=logging.DEBUG)

app = create_app()

if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) < 1:
        args.append('8080')
    print(args)

    logging.debug("Starting SERVER on port: " + args[0])
    app.run(port=args[0], host='0.0.0.0')
