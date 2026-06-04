deployconip:
	@ docker run -d --name appflask -p 7000:5000 ghcr.io/byronmoreno/appflask:2.0.0


deploy:
	@ docker stack deploy --with-registry-auth -c stack.yml byron

network:
	@ docker network create --driver overlay --scope swarn byron_net || true

volume:
	@ docker volume create v_byron