FROM node:lts


RUN apt-get update
RUN apt-get install -y awscli
RUN npm install -g aws-cdk@latest

WORKDIR /infrastructure


# aws configure
# aws sts get-caller-identity
# npm --version
    # 8.19.2
# cdk version
    # 2.68.0 (build 25fda51)
# cdk bootstrap aws://120886185014/us-east-1
# cd infrastructure
# cdk init --language python
