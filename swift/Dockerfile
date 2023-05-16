FROM swift:5.5-bionic

WORKDIR /app

COPY . .

RUN swift build

CMD ["./.build/debug/MyApp"]