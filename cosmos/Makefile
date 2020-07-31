.PHONY: release local prepare clean 
COMPONENT := ws-onion

release: clean prepare
	mock-build --os 7 --define "buildnum $(shell cosmos-release generate-version $(COMPONENT))"
	cosmos-release service $(COMPONENT) RPMS/*.rpm

local: prepare
	mock-build --os 7 

prepare: 
	mkdir -p SOURCES deploy/var/www/backend
	tar -zcf SOURCES/vendor.tar.gz vendor
	cp -a Makefile bin src features translations Application templates config public scripts deploy/var/www/backend
	mkdir deploy/var/www/backend/var
	tar -C deploy -zcf SOURCES/src.tar.gz etc usr var

clean: 
	rm -rf BUILD RPMS SRPMS deploy/var
