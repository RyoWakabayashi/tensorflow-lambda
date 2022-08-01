FROM tensorflow/tensorflow:2.9.1

ENV PYTHONUNBUFFERED=TRUE
ENV PYTHONDONTWRITEBYTECODE=TRUE

ADD https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie /usr/bin/aws-lambda-rie

RUN chmod 755 /usr/bin/aws-lambda-rie

COPY entry.sh "/entry.sh"

RUN chmod +x /entry.sh

# hadolint ignore=DL3013
RUN pip install --no-cache-dir --upgrade pip

RUN mkdir -p /opt/ml

COPY models /opt/ml/model

RUN chmod -R +r /opt/ml/model

WORKDIR /work

COPY ./requirements.txt /work/

# hadolint ignore=DL3006
RUN pip install --no-cache-dir --requirement requirements.txt

COPY ./prg /work/prg

WORKDIR /work/prg

RUN chmod +x /work/prg/lambda.py

ENV PATH="/work/prg:${PATH}"

ENTRYPOINT [ "/bin/bash", "/entry.sh" ]

CMD ["lambda.lambda_handler"]
