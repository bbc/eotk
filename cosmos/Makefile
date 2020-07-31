.PHONY: release local prepare clean 
COMPONENT := bbc-onion

release: clean prepare
	#mock-build --os 7 --define "buildnum $(shell cosmos-release generate-version $(COMPONENT))"
	mock-build --os 7 --define "buildnum 1"
	cosmos-release service $(COMPONENT) RPMS/*.rpm

local: prepare
	mock-build --os 7 

prepare: 
	mkdir SOURCES
	mkdir tmp
	cp /var/lib/jenkins/workspace/bbc-onion/README.md tmp
	tar zcf SOURCES/src.tar.gz tmp

clean: 
	rm -rf BUILD RPMS SRPMS SOURCES
