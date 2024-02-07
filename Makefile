init:
	@docker compose build 
	@docker compose up -d

up:
	@docker compose up -d
	
down:
	@docker compose down

exec:
	@docker exec -it southy bash
