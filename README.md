# tensorflow-lambda

Example of running TensorFlow in Lambda

## Requirements

- [asdf]
- curl
- [docker]

## Setup

Clone the repository.

```bash
git clone https://github.com/RyoWakabayashi/tensorflow-lambda.git
cd tensorflow-lambda
```

Install asdf plugins.

```bash
asdf plugin-add aws-sam-cli \
  ; asdf plugin-add direnv \
  ; asdf plugin-add jq \
  ; asdf plugin-add nodejs \
  ; asdf plugin-add python \
  ; asdf plugin-add yarn
```

Install Languages and Tools.

```bash
asdf install
```

## Download models

Download MobileNet v2 model files.

```bash
python download_models.py
```

## Build

Move to the sam directory.

```bash
cd sam
```

Build sam.

Make sure Docker is launched.

```bash
sam build
```

## Run locally

```bash
$ sam local start-api
...
2022-08-01 15:12:33  * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)
```

Calling the API from another terminal.

```bash
curl -XPOST \
  http://127.0.0.1:3000/predictions \
  -H "Content-Type: image/jpeg" \
  --data-binary @imgs/sample.jpg | jq
```

## Deploy

Deploy with a guide the first time.

API URL is displayed after execution.

```bash
$ sam deploy --guided
...
-------------------------------------------------------------------------------------------------------
Outputs
-------------------------------------------------------------------------------------------------------
Key                 Api
Description         API Gateway endpoint URL for v1 stage for Tensorflow sample function
Value               https://some.execute-api.ap-northeast-1.amazonaws.com/v1/predictions
-------------------------------------------------------------------------------------------------------
```

If you save the configuration information,
you do not need to use the guide for the second time or later.

```bash
sam deploy
```

## Test

Change the URL to the value displayed after deployment.

```bash
curl -XPOST \
  https://some.execute-api.ap-northeast-1.amazonaws.com/v1/predictions \
  -H "Content-Type: image/jpeg" \
  --data-binary @imgs/sample.jpg | jq
```

You may view the log.

```bash
sam logs --stack-name some-stack-name
```

## Preparing to edit this repository

Install commitlint.

```bash
yarn
```

Install pre-commit.

```bash
pip install --requirement requirements.txt
asdf reshim python
pre-commit install
```

Run pre-commit manually.

```bash
pre-commit run --all-files
```

## Notes

No authentication is applied in this sample.

Please add authentication to the production.

[asdf]: https://asdf-vm.com/
[docker]: https://www.docker.com/
