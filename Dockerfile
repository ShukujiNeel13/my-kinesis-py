FROM public.ecr.aws/lambda/python:3.7

COPY app.py ./
CMD ["app.handler"]
