.PHONY: all
all: SOURCES RPMS

.PHONY: clean
clean:
	rm -r BUILD BUILDROOT RPMS SOURCES SRPMS

SOURCES:
	bash template-to-repos.sh

RPMS: SOURCES
	rpmbuild --define "_topdir $(PWD)" -bb SPECS/*
