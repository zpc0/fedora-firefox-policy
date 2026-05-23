Name:		firefox-policy
Version:	151.0.0
Release:	1%{?dist}
Summary:	Custom policies for Mozilla Firefox

License:	GPL-3.0-or-later
URL:		https://zpc.st
Source0:	policies.json
Source1:	COPYING
Source2:	autoconfig.js
Source3:	firefox.cfg.js

BuildArch:	noarch
Requires:	firefox

%description
This is a enterprise policies for Mozilla Firefox.

%prep

%build

%install
mkdir -p %{buildroot}%{_libdir}/firefox/distribution
install -m 0644 %{SOURCE0} %{buildroot}%{_libdir}/firefox/distribution/policies.json
mkdir -p %{buildroot}%{_libdir}/firefox/defaults/pref
install -m 0644 %{SOURCE2} %{buildroot}%{_libdir}/firefox/defaults/pref/autoconfig.js
install -m 0644 %{SOURCE3} %{buildroot}%{_libdir}/firefox/firefox.cfg

%files
%{_libdir}/firefox/firefox.cfg
%{_libdir}/firefox/defaults/pref/autoconfig.js
%{_libdir}/firefox/distribution/policies.json

%changelog
%autochangelog
