Name:		perl-Params-SomeUtil
Version:	1.11
Release:	1
Summary:	Selected utility functions from Params::Util
License:	Artistic-2.0
Group:		Development/Perl
URL:		https://metacpan.org/release/Params-SomeUtil
Source0:	https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/Params-SomeUtil-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test2::V0)

%description
Params::SomeUtil provides a small subset of the functions from Params::Util.

%prep
%autosetup -p1 -n Params-SomeUtil-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%make_install

%files
%doc Changes README
%{perl_vendorlib}/Params/*
%{_mandir}/man3/*
