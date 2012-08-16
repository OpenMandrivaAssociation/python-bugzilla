%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           python-bugzilla
Version:        0.7.0
Release:        1%{?dist}
Summary:        A python library for interacting with Bugzilla

Group:          Development/Languages
License:        GPLv2+
URL:            https://fedorahosted.org/python-bugzilla
Source0:        https://fedorahosted.org/releases/p/y/%{name}/%{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch:      noarch
BuildRequires:  python-devel
%if 0%{?fedora} >= 8
BuildRequires: python-setuptools-devel
%else
BuildRequires: python-setuptools
%endif

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
%defattr(-,root,root,-)
%doc COPYING README THANKS TODO PKG-INFO
%{python_sitelib}/*
%{_bindir}/bugzilla
%{_mandir}/man1/bugzilla.1.gz


%changelog
* Thu Jun 14 2012 Cole Robinson <crobinso@redhat.com> - 0.7.0-1
- Rebased to version 0.7.0
- Fix querying with latest Red Hat bugzilla
- Bugzilla 4 API support
- Improve querying non-RH bugzilla instances

* Tue Mar 2 2010 Will Woods <wwoods@redhat.com> - 0.6.0-1
- New version 0.6, with lots of improvements and fixes.
- Library: add NovellBugzilla implementation
- Library: use standardized LWPCookieJar by default
- Library: implement unicode(bug), fix Bug.__str__ unicode handling
- Library: make Bug class pickle-friendly
- Library: add flag info helper methods to Bug class
- Library: handle problems with missing fields in User class
- CLI: --oneline formatting tweaks and dramatic speed improvements
- CLI: add support for modifying private, status, assignee, flags, cc, fixed_in
- CLI: improve query: allow multiple flags, flag negation, handle booleans
- CLI: make --cc work when creating bugs
- CLI: new --raw output style
- CLI: special output format fields for flag and whiteboard
- CLI: fix broken --cc and -p flags
- CLI: fix problem where bz comments default to being private
- CLI: improve 'info --product' output
- CLI: handle socket/network failure cleanly
- CLI: allow adding comments when updating whiteboards

* Sun Jul 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Apr 14 2009 Will Woods <wwoods@redhat.com> - 0.5.1-2
- Fix missing util.py

* Thu Apr 9 2009 Will Woods <wwoods@redhat.com> - 0.5.1-1
- CLI: fix unicode handling
- CLI: add --from-url flag, which parses a bugzilla query.cgi URL
- CLI: fix showing aliases
- CLI: add --comment, --private, --status, --assignee, --flag, --cc for update
- CLI: fix --target_milestone

* Wed Mar 25 2009 Will Woods <wwoods@redhat.com> - 0.5-1
- Fix problem where login wasn't saving the cookies to a file 
- Fix openattachment (bug #487673)
- Update version number for 0.5 final

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5-0.rc1.1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Feb 12 2009 Will Woods <wwoods@redhat.com> 0.5-0.rc1
- Improve cookie handling
- Add User class and associated Bugzilla methods (in Bugzilla 3.4)
- Add {add,edit,get}component methods
- Fix getbugs() so a single invalid bug ID won't abort the whole request
- CLI: fix -c <component>

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 0.4-0.rc4.1
- Rebuild for Python 2.6

* Wed Oct 15 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc4
- CLI: fix traceback with --full (Don Zickus)
- CLI: add --oneline (Don Zickus)
- CLI: speedup when querying bugs by ID (Don Zickus)
- CLI: add --bztype
- CLI: --bug_status defaults to ALL
- Fix addcc()/deletecc()
- RHBugzilla3: raise useful error on getbug(unreadable_bug_id)
- Add adduser() (Jon Stanley)

* Fri Oct  8 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc3
- Add updateperms() - patch courtesy of Jon Stanley
- Fix attachfile() for RHBugzilla3
- Actually install man page. Whoops.

* Thu Sep 18 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc2
- Auto-generated man page with much more info
- Fix _attachfile()

* Thu Sep  4 2008 Will Woods <wwoods@redhat.com> 0.4-0.rc1
- Update to python-bugzilla 0.4-rc1
- We now support upstream Bugzilla 3.x and Red Hat's Bugzilla 3.x instance
- library saves login cookie in ~/.bugzillacookies
- new 'bugzilla login' command to get a login cookie

* Sat Jan 12 2008 Will Woods <wwoods@redhat.com> 0.3-1
- Update to python-bugzilla 0.3 
- 'modify' works in the commandline-util
- add Bug.close() and Bug.setstatus()

* Thu Dec 13 2007 Will Woods <wwoods@redhat.com> 0.2-4
- use _bindir instead of /usr/bin and proper BR for setuptools

* Tue Dec 11 2007 Will Woods <wwoods@redhat.com> 0.2-3
- Fix a couple of things rpmlint complained about

* Tue Dec 11 2007 Will Woods <wwoods@redhat.com> 0.2-2
- Add docs

* Wed Oct 10 2007 Will Woods <wwoods@redhat.com> 0.2-1
- Initial packaging.
