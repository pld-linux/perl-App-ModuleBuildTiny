#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	App
%define		pnam	ModuleBuildTiny
%include	/usr/lib/rpm/macros.perl
Summary:	App::ModuleBuildTiny - A standalone authoring tool for Module::Build::Tiny
Name:		perl-App-ModuleBuildTiny
Version:	0.010
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/App/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8e3be63c6ba857207046d67aa4150934
URL:		http://search.cpan.org/dist/App-ModuleBuildTiny/
BuildRequires:	perl-Module-Build
BuildRequires:	perl-Module-Build-Tiny
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(CPAN::Meta::Prereqs::Filter)
BuildRequires:	perl(File::Slurper)
BuildRequires:	perl(Software::LicenseUtils)
BuildRequires:	perl-CPAN-Meta
BuildRequires:	perl-Module-CPANfile
BuildRequires:	perl-Module-Runtime
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
App::ModuleBuildTiny contains the implementation of the mbtiny tool.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	--installdirs=vendor
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT
./Build install \
	--destdir=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%attr(755,root,root) %{_bindir}/mbtiny
%{perl_vendorlib}/App/ModuleBuildTiny.pm
%{_mandir}/man1/mbtiny.1p*
%{_mandir}/man3/App::ModuleBuildTiny.3pm*
