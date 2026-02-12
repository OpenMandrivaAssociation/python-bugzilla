%define module bugzilla
%define oname python_bugzilla

Name:		python-bugzilla
Version:	3.3.0
Release:	1
Summary:	A python library for interacting with Bugzilla
License:	GPL-2.0-or-later
Group:		Development/Python
URL:		https://github.com/python-bugzilla/python-bugzilla
Source0:	https://github.com/python-bugzilla/python-bugzilla/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:	python
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
python-bugzilla is a python library for interacting with bugzilla instances
over XML-RPC. This package also includes the 'bugzilla' command-line tool
for interacting with bugzilla from shell scripts.

%prep -a
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%files
%doc README.md CONTRIBUTING.md
%license COPYING
%{_bindir}/%{module}
%{_mandir}/man1/%{module}.1.*
%{python_sitelib}/%{module}
%{python_sitelib}/%{oname}-%{version}-py%{pyver}.egg-info
