# Create an option to build locally without fetchting own repo
# for sourcing and patching
%bcond local 0

# Source repo 1
%global author pvermeer
%global source v4l-utils
%global sourcerepo https://git.linuxtv.org/v4l-utils.git
%global commit c363e9aa6d7047e4bdfb68a96fddde884c63487d
%global versioncommit %(echo -n %{commit} | head -c 8)

# Own copr repo
%global coprrepo https://github.com/PVermeer/copr_v4l-utils-edid-data.git
%global coprsource copr_v4l-utils-edid-data

Name: v4l-utils-edids
Version: 0.0.3
Release: %{versioncommit}%{?dist}
License: GPLv2+ and GPLv2 and MIT
Summary: RPM package to install the decoded edids from https://git.linuxtv.org/v4l-utils.git on immutable filesystems.
Url: https://git.linuxtv.org/v4l-utils.git/tree/utils/edid-decode/data

BuildRequires: git

%description
RPM package to install the decoded edids from https://git.linuxtv.org/v4l-utils.git

%define workdir %{_builddir}/%{name}
%define coprdir %{workdir}/%{coprsource}
%define sourcedir %{workdir}/%{source}
%define installdir /usr/lib/firmware/edid

%prep
# To apply working changes handle sources / patches locally
# COPR should clone the commited changes
%if %{with local}
  # Get sources / patches - local build
  mkdir -p %{coprdir}
  cp -r %{_topdir}/SOURCES/* %{coprdir}
%else
  # Get sources / patches - COPR build
  git clone %{coprrepo} %{coprdir}
  cd %{coprdir}
  rm -rf .git
  cd %{workdir}
%endif

git clone %{sourcerepo} %{sourcedir}
cd %{sourcedir}
git reset --hard %{commit}

%build

%install
mkdir -p %{buildroot}/%{installdir}
install %{sourcedir}/utils/edid-decode/data/* %{buildroot}/%{installdir}

%check

%post

%files
%{installdir}/*
