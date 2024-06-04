services:
  fibonacci-backend-cs:
    image: oshokry/fibonacci-backend
    command: -v v5.0 -l true
    ports:
      - 30060:5000
    volumes:
      - /mnt/c/Fibonacci/logs:/logs

  fibonacci-frontend:
    image: oshokry/fibonacci-frontend
    ports:
      - 30088:80
    environment:
      PASS_PHRASE: Test123
