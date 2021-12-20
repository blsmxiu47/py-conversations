FROM python:3.9-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

# Install python package requirements

COPY requirements.txt settings.py /opt/dagster/app/

WORKDIR /opt/dagster/app

RUN pip install -r requirements.txt
# RUN pip install \
#     dagit \
#     dagster-postgres \
#     dagster-docker

# Copy repo and workspace to /opt/dagster/app

# RUN pwd
# RUN ls -la

COPY workspace.yaml /opt/dagster/app/

COPY py_conversations /opt/dagster/app/py_conversations

# ENV PYTHONPATH "${PYTHONPATH}:/py_conversations"

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

# Copy dagster instance YAML to $DAGSTER_HOME

COPY dagster.yaml $DAGSTER_HOME



# Run dagster gRPC server on port 4000

EXPOSE 4000

CMD ["dagster", "api", "grpc", "-h", "0.0.0.0", "-p", "4000", "-f", "py_conversations/repository.py"]

# EXPOSE 3000

# ENTRYPOINT ["dagit", "-h", "0.0.0.0", "-p", "3000"]