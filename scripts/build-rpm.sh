#!/bin/bash

set -e
set -x

rm -rf ./rpmbuild
mkdir -p ./rpmbuild/SOURCES

rpmlint ./v4l-utils-edids.spec
rpmbuild --define "_topdir $PWD/rpmbuild" -bb ./v4l-utils-edids.spec
rpm -qvlp ./rpmbuild/RPMS/**/*.rpm
rpm -qp --scripts ./rpmbuild/RPMS/**/*.rpm
