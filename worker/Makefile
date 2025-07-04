IMAGE_NAME=njdmvappointmenthelper-worker
CONTAINER_NAME=njdmvappointmenthelper-worker

build:
	docker build -t $(IMAGE_NAME) .

run:
	docker run --rm --name $(CONTAINER_NAME) $(IMAGE_NAME)

clean:
	docker rmi -f $(IMAGE_NAME) || true

rebuild: clean build run
