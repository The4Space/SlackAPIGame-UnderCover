TRAVIS_BUILD_DIR ?= $(shell pwd)
REPO ?= $(shell basename ${TRAVIS_BUILD_DIR})
TRAVIS_BRANCH ?= test

code.zip: package

package:
	zip -q -r code.zip hooks SlackAPIGame-UnderCover appspec.yml scripts certifications env

build:
	echo ${TRAVIS_BRANCH} > env && \

deploy: clean build code.zip
	aws s3 cp code.zip s3://mptmusic-packages/${REPO}/${REPO}-${TRAVIS_COMMIT}/ && \
	aws s3 cp codedeploy.yml s3://mptmusic-packages/${REPO}/${REPO}-${TRAVIS_COMMIT}/ && \
	/bin/echo -n "${REPO}/${REPO}-${TRAVIS_COMMIT}" > ${REPO}.${TRAVIS_BRANCH} && \
	aws s3 cp ${REPO}.${TRAVIS_BRANCH} s3://mptmusic-packages/${REPO}/

clean:
	rm -rf code.zip *.test mpt-music-api env

.PHONY: package deploy clean
