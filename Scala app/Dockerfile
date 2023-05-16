FROM openjdk:11-jdk

WORKDIR /app

COPY . .

RUN sbt compile

CMD ["java", "-cp", "target/scala-2.13/*", "HelloWorld"]