%global repository v4l-utils
%global commit 8fb667bc4ec202529799cca28fff5b69d34cee19
%global shortcommit %(echo -n %{commit} | head -c 8)

Name: v4l-utils-edids
Version: 0.0.2
Release: %{shortcommit}%{?dist}
License: GPLv2+ and GPLv2 and MIT
Summary: RPM package to install the decoded edids from https://git.linuxtv.org/v4l-utils.git on immutable filesystems.
Url: https://git.linuxtv.org/v4l-utils.git/tree/utils/edid-decode/data

BuildRequires: git

%description
RPM package to install the decoded edids from https://git.linuxtv.org/v4l-utils.git

%define installdir %{_libdir}/firmware/edid
%define workdir %{_builddir}/%{name}

%prep
# Get chromebook-linux-audio script
git clone https://git.linuxtv.org/%{repository}.git %{workdir}
cd %{workdir}
git reset --hard %{commit}

%build

%install
mkdir -p %{buildroot}/%{installdir}
install %{workdir}/utils/edid-decode/data/* %{buildroot}/%{installdir}

%files
%{installdir}/*
