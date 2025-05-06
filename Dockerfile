FROM --platform=linux/amd64 node:18-bullseye

RUN npm install -g azure-functions-core-tools@4 --unsafe-perm true

ENTRYPOINT ["/bin/bash"]
