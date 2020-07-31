.PHONY: release local prepare clean 
COMPONENT := bbc-onion

release: clean prepare
	mock-build --os 7 --define "buildnum $(shell cosmos-release generate-version $(COMPONENT))"
	cosmos-release service $(COMPONENT) RPMS/*.rpm

local: prepare
	mock-build --os 7 

prepare: 
	tar -C .. -zcf SOURCES/src.tar.gz README.md

clean: 
	rm -rf BUILD RPMS SRPMS 
