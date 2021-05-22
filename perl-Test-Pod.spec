#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Test-Pod
Version  : 1.52
Release  : 42
URL      : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Pod-1.52.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Pod-1.52.tar.gz
Summary  : 'check for POD errors in files'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Test-Pod-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
Test/Pod version 1.52
=====================
This library's module, Test::Pod, provides an interface for validating POD in
module files.

%package dev
Summary: dev components for the perl-Test-Pod package.
Group: Development
Provides: perl-Test-Pod-devel = %{version}-%{release}
Requires: perl-Test-Pod = %{version}-%{release}

%description dev
dev components for the perl-Test-Pod package.


%package perl
Summary: perl components for the perl-Test-Pod package.
Group: Default
Requires: perl-Test-Pod = %{version}-%{release}

%description perl
perl components for the perl-Test-Pod package.


%prep
%setup -q -n Test-Pod-1.52
cd %{_builddir}/Test-Pod-1.52

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Test::Pod.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/Test/Pod.pm
