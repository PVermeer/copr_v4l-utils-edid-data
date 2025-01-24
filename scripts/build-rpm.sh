#!/bin/bash

set -e
set -x

spec_file=./v4l-utils-edids.spec
repo=$(grep '%global repository\s.*$' $spec_file | awk '{ print $3 }')
commit=$(grep '%global commit\s.*$' $spec_file | awk '{ print $3 }')

(cd ./$repo; git reset --hard $commit)

rm -rf ./rpmbuild
mkdir -p ./rpmbuild/SOURCES

rpmlint ./v4l-utils-edids.spec
rpmbuild --define "_topdir $PWD/rpmbuild" -bb ./v4l-utils-edids.spec
rpm -qvlp ./rpmbuild/RPMS/**/*.rpm
rpm -qp --scripts ./rpmbuild/RPMS/**/*.rpm
