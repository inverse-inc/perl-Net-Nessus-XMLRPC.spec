%define		real_name Net-Nessus-XMLRPC
Name:		perl-%{real_name}
Version:	0.30
Release:	1%{?dist}
Summary:	Communicate with Nessus scanner(v4.2+) via XMLRPC

Group:		Development/Libraries
License:	Artistic/GPL
URL:		http://search.cpan.org/dist/Net-Nessus-XMLRPC/
Source0:	http://search.cpan.org/CPAN/authors/id/K/KO/KOST/Net-Nessus-XMLRPC-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildArch: 	noarch
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(HTTP::Request::Common)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(XML::Simple)
Requires:	perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Requires:	perl(HTTP::Request::Common)
Requires:	perl(LWP::UserAgent)
Requires:	perl(Net::SSL)
Requires:	perl(XML::Simple)

%{?perl_default_filter}

%description
This is Perl interface for communication with Nessus scanner over XMLRPC. You
can start, stop, pause and resume scan. Watch progress and status of scan,
download report, etc.


%prep
%setup -q -n %{real_name}-%{version}


%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
make %{?_smp_mflags}


%install
rm -rf $RPM_BUILD_ROOT
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null ';'
%{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changes MANIFEST META.yml README TODO
%{perl_vendorlib}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*.3*


%changelog
* Tue Aug 14 2012 Olivier Bilodeau <olivier@bottomlesspit.org> - 0.30-1
- Initial release.
