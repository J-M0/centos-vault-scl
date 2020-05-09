SPECS=SPECS/*

all:
	rpmbuild --define "_topdir $(PWD)" -bb $(SPECS)

clean:
	rm -r BUILD BUILDROOT RPMS SRPMS
