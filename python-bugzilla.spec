Name:           python-bugzilla
Version:        1.2.2
Release:        1
Summary:        A python library for interacting with Bugzilla
Group:          Development/Python
License:        GPLv2+
URL:            https://fedorahosted.org/python-bugzilla
Source0:        https://fedorahosted.org/releases/p/y/%{name}/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires: python-devel
BuildRequires: python-setuptools

%description
python-bugzilla is a python library for interacting with bugzilla instances
over XML-RPC. This package also includes the 'bugzilla' command-line tool
for interacting with bugzilla from shell scripts.

%prep
%setup -q


%build
%{__python} setup.py build


%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT


%files
%doc COPYING README.md CONTRIBUTING.md
%{python_sitelib}/*
%{_bindir}/bugzilla
%{_mandir}/man1/bugzilla.1.*
