Summary: Utilities for working with md5sum implanted in ISO images
Name:    isomd5sum
Version: 1.2.1
Release: 4%{?dist}
Epoch: 1
License: GPLv2+
Group: Applications/System

Url:     https://github.com/rhinstaller/isomd5sum
Source0: https://github.com/rhinstaller/%{name}/archive/%{version}.tar.gz

BuildRequires: popt-devel
BuildRequires: python2-devel python3-devel

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary: Development headers and library for using isomd5sum 
Group: Development/System
Requires: %{name} = %{epoch}:%{version}-%{release}
Provides: %{name}-static = %{epoch}:%{version}-%{release}

%description devel
This contains header files and a library for working with the isomd5sum
implanting and checking.

%package -n python2-isomd5sum
Summary: Python bindings for isomd5sum
%{?python_provide:%python_provide python2-isomd5sum}

%description -n python2-isomd5sum
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package -n python3-isomd5sum
Summary: Python bindings for isomd5sum

%description -n python3-isomd5sum
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.


%prep
%setup -q

rm -rf %{py3dir}
cp -a . %{py3dir}

%build
CFLAGS="$RPM_OPT_FLAGS -Wno-strict-aliasing"; export CFLAGS
PYTHON=%{__python2} make checkisomd5 implantisomd5 pyisomd5sum.so

pushd %{py3dir}
PYTHON=%{__python3} make checkisomd5 implantisomd5 pyisomd5sum.so
popd

%install
PYTHON=%{__python2} make DESTDIR=$RPM_BUILD_ROOT install-bin install-devel install-python

pushd %{py3dir}
PYTHON=%{__python3} make DESTDIR=$RPM_BUILD_ROOT install-bin install-devel install-python
popd

%files
%license COPYING
%{_bindir}/implantisomd5
%{_bindir}/checkisomd5
%{_mandir}/man*/*

%files devel
%{_includedir}/*.h
%{_libdir}/*.a

%files -n python2-isomd5sum
%{python2_sitearch}/pyisomd5sum.so

%files -n python3-isomd5sum
%{python3_sitearch}/pyisomd5sum.so

%changelog
* Sat Aug 19 2017 Zbigniew Jędrzejewski-Szmek <zbyszek@in.waw.pl> - 1:1.2.1-4
- Python 2 binary package renamed to python2-isomd5sum
  See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.2.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Jun 09 2017 Brian C. Lane <bcl@redhat.com> - 1:1.2.1-1
- New Version 1.2.1 (bcl)
- Let the user pass their own file descriptor (squimrel)
- Correct format specifiers (squimrel)

* Thu Jun 08 2017 Brian C. Lane <bcl@redhat.com> - 1:1.2.0-1
- New Version 1.2.0 (bcl)
- Improve the python test and add a test target to the Makefile (bcl)
- Improve error handling of libimplantisomd5 (squimrel)
- Fix popt memory leak and avoid exit in main (squimrel)
- Add derived clang format and editorconfig (squimrel)
- Format, constify, castify, decl-at-use code (squimrel)
- Make libimplantisomd5 use the utilities (squimrel)
- Implement shared utilities (squimrel)
- Refactor libcheckisomd5 (squimrel)

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Mon Dec 19 2016 Miro Hrončok <mhroncok@redhat.com> - 1:1.1.0-4
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.1.0-3
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Fri Dec 04 2015 Brian C. Lane <bcl@redhat.com> 1.1.0-1
- New upstream with Python3 support

* Mon Jul 20 2015 Peter Robinson <pbrobinson@fedoraproject.org> 1:1.0.12-6
- Use github source so it will build
- Cleanup spec
- Use %%license

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.12-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 1:1.0.12-4
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.12-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.12-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri Jan 10 2014 Brian C. Lane <bcl@redhat.com> 1.0.12-1
- Display supported iso status (#1026336) (bcl)
- Add ppc64le (bcl)

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.11-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Jul 17 2013 Brian C. Lane <bcl@redhat.com> 1.0.11-1
- Add aarch64 (#985568) (bcl)

* Tue Feb 26 2013 Brian C. Lane <bcl@redhat.com> 1.0.10-1
- Fix for gcc type-punned and sizeof pointer warnings. (bcl)
- Add exit code 2 for user abort (#907600) (bcl)
- Cleanup TABs and update Copyrights (bcl)
- Standardize *FLAGS in Makefile (ryan)

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.9-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.9-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Mar 09 2012 Brian C. Lane <bcl@redhat.com> 1.0.9-1
- Add python-isomd5sum package with python bindings
- Add callback and interrupt support to the python library
- Add RPM_OPT_FLAGS to CFLAGS and update makefile to use CFLAGS from environment

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.7-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Apr 8 2011 Radek Vykydal <rvykydal@fedoraproject.org> - 1:1.0.7-1
- Allocate one more char for string sentinel (#692135) (rvykydal)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.6-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Jun 30 2010 Michael Schwendt <mschwendt@fedoraproject.org> - 1:1.0.6-2
- Add virtual -static package to -devel package (#609607).

* Fri Mar 26 2010 Radek Vykydal <rvykydal@redhat.com> - 1:1.0.6-1
- Add abort check feature (#555107) (dpierce, rvykydal)
  Changes prototype of exported checkMediaFile function.
- Fix exit value of checkisomd5 (rvykydal)
- Remove output to stderr from library (#576251) (bcl)
- Use separate return value for image not found (#578160) (bcl)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jan  8 2009 Jeremy Katz <katzj@redhat.com> - 1:1.0.5-1
- Don't install the unused python module (#479005)

* Sat Nov 29 2008 Ignacio Vazquez-Abrams <ivazqueznet+rpm@gmail.com> - 1:1.0.4-4
- Rebuild for Python 2.6

* Wed Nov  5 2008 Hans de Goede <hdegoede@redhat.com> - 1:1.0.4-3
- Fix permission on installed manpages (#469936)

* Thu Apr 24 2008 Dennis Gilmore <dennis@ausil.us> - 1:1.0.4-2
- add patch for making libdir /usr/lib64 for sparc64

* Thu Feb  7 2008 Jeremy Katz <katzj@redhat.com> - 1:1.0.4-1
- Add man pages from Ryan Finnie (ryan AT finnie DOT org)
- Use popt in checkisomd5 (Ryan Finnie)
- Fix verbose/gauge interactions (Ryan Finnie)
- A few other little janitorial things (Ryan Finnie)

* Mon Dec 10 2007 Jeremy Katz <katzj@redhat.com> - 1:1.0.2-1
- The "fix the build after changing the API" release

* Mon Dec 10 2007 Jeremy Katz <katzj@redhat.com> - 1:1.0.1-1
- Add some simple callback support in the library

* Fri Dec  7 2007 Jeremy Katz <katzj@redhat.com> - 1.0-1
- Initial build.

