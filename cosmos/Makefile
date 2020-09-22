.PHONY: release local prepare clean 
COMPONENT := bbc-onion

release: clean prepare
	mock-build --os 7 --define "buildnum $(shell cosmos-release generate-version $(COMPONENT))"
	cosmos-release service $(COMPONENT) RPMS/*.rpm

local: prepare
	mock-build --os 7 

prepare: 
	mkdir SOURCES
	mkdir tmp
	cp /var/lib/jenkins/workspace/bbc-onion/README.md tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/eotk tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/demo.d tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/doc.d tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/lib.d tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/opt.d tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/templates.d tmp
	cp -r /var/lib/jenkins/workspace/bbc-onion/tools.d tmp
	tar zcf SOURCES/src.tar.gz tmp

clean: 
	rm -rf BUILD RPMS SRPMS SOURCES tmp
