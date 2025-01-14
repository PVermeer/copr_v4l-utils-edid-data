Name: v4l-utils-edids
Version: 0.0.0
Release: 1%{?dist}
License: GPLv2+ and GPLv2
Summary: RPM package to install the decoded edids from https://git.linuxtv.org/v4l-utils.git on immutable filesystems.
Url: https://git.linuxtv.org/v4l-utils.git/tree/utils/edid-decode/data

BuildRequires: git

%description
RPM package to install the decoded edids from https://git.linuxtv.org/v4l-utils.git

%define installdir /usr/lib

%prep
# Get chromebook-linux-audio script
git clone https://git.linuxtv.org/v4l-utils.git

%build

%install
mkdir -p $RPM_BUILD_ROOT/%{installdir}/firmware/edid
mv %{_builddir}/v4l-utils/utils/edid-decode/data/* $RPM_BUILD_ROOT/%{installdir}/firmware/edid

%files
%{installdir}
