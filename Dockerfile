FROM python:3.11-slim

RUN useradd -m user
USER user
WORKDIR /home/user/app

COPY src/requirements.txt ./requirements.txt

ENV HOME=/home/user
ENV XDG_CACHE_HOME=/home/user/.cache
ENV XDG_CONFIG_HOME=/home/user/.config
ENV PYTHONUSERBASE=/home/user/.pythonuserbase
ENV TRANSFORMERS_CACHE=/home/user/.cache/transformers
ENV HF_HOME=/home/user/.cache/huggingface
ENV HF_DATASETS_CACHE=/home/user/.cache/huggingface/datasets
ENV PYTHONPATH=/home/user/app/src
ENV PATH="/home/user/.pythonuserbase/bin:${PATH}"

RUN mkdir -p /home/user/.cache \
    /home/user/.config \
    /home/user/.pythonuserbase \
    /home/user/.cache/transformers \
    /home/user/.cache/huggingface/datasets

RUN pip install --upgrade pip && pip install --no-cache-dir --force-reinstall --user -r requirements.txt

COPY src ./src

EXPOSE 7860

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "7860"]