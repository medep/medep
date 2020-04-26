FROM maven:latest as build-env

RUN mkdir -p /project

ADD mpg-common /project/mpg-common
ADD mpg-local-UMCM /project/mpg-local-UMCM

WORKDIR /project/mpg-common
RUN mvn clean install -U

WORKDIR /project/mpg-local-UMCM
RUN mvn clean package -U

FROM openjdk:8u131-jdk-alpine

COPY --from=build-env /project/mpg-local-UMCM/target/mpg-local-UMCM-0.0.1-SNAPSHOT.war /project/mpg-local-UMCM.war

WORKDIR /project
CMD ["java", "-jar", "mpg-local-UMCM.war"]