SENTRY_AUTH_TOKEN=415ea20e4c664f17a966ee1785749115d818142dc6884119a77992a509469852
SENTRY_ORG=julia-test-org
SENTRY_PROJECT=backend-monitoring
VERSION=1

deploy: install create_release associate_commits run_django

install:
	pip3 install -r ./requirements.txt

create_release:
	sentry-cli releases -o $(SENTRY_ORG) new -p $(SENTRY_PROJECT) $(VERSION)

associate_commits:
	sentry-cli releases -o $(SENTRY_ORG) -p $(SENTRY_PROJECT) \
		set-commits $(VERSION) --auto

run_django:
	VERSION=$(VERSION) python3 manage.py runserver
