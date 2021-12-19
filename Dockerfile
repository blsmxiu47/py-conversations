FROM python:3.9-slim

RUN mkdir -p /opt/dagster/dagster_home /opt/dagster/app

# COPY requirements.txt /opt/app/requirements.txt 
# RUN pip install -r requirements.txt
RUN pip install dagit dagster-postgres

# Copy code and workspace to /opt/dagster/app
COPY py_conversations/repository.py workspace.yaml /opt/dagster/app/

ENV DAGSTER_HOME=/opt/dagster/dagster_home/

# Copy dagster instance YAML to $DAGSTER_HOME
COPY dagster.yaml /opt/dagster/dagster_home/

WORKDIR /opt/dagster/app

EXPOSE 3000

ENTRYPOINT ["dagit", "-h", "0.0.0.0", "-p", "3000"]