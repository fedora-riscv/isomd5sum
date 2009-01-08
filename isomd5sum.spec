Summary: Utilities for working with md5sum implanted in ISO images
Name: isomd5sum
Version: 1.0.5
Release: 1%{?dist}
Epoch: 1
License: GPLv2+
Group: Applications/System
URL: http://git.fedorahosted.org/git/?p=isomd5sum.git;a=summary
Source0: http://fedorahosted.org/releases/i/s/isomd5sum/%{name}-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: popt-devel

%description
The isomd5sum package contains utilities for implanting and verifying
an md5sum implanted into an ISO9660 image.

%package devel
Summary: Development headers and library for using isomd5sum 
Group: Development/System
Requires: %{name} = %{epoch}:%{version}-%{release}

%description devel
This contains header files and a library for working with the isomd5sum
implanting and checking.


%prep
%setup -q

%build
make checkisomd5 implantisomd5

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install-bin install-devel

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc COPYING
/usr/bin/implantisomd5
/usr/bin/checkisomd5
%{_mandir}/man*/*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*.h
%{_libdir}/*.a

%changelog
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

