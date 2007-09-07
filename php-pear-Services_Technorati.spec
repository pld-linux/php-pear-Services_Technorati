%include	/usr/lib/rpm/macros.php
%define		_class		Services
%define		_subclass	Technorati
%define		_status		beta
%define		_pearname	Services_Technorati
Summary:	%{_pearname} - a class for interacting with the Technorati API
Summary(pl.UTF-8):	%{_pearname} - klasa do interakcji z API Technorati
Name:		php-pear-%{_pearname}
Version:	0.7.1beta
Release:	0.1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	6abf7b9338a30828ed0a9118e02b378b
URL:		http://pear.php.net/package/Services_Technorati/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-HTTP_Request
Requires:	php-pear-PEAR >= 1.4.0b1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Cache/Lite.*)'

%description
Services_Technorati is a wrapper for the REST-based Technorati
webservices API. Technorati is a blog search engine that provides a
number of interfaces for interacting with recent blog entries, such as
searching for entries that link to a certain URL, are linked from a
certain URL, or have been given certain tags.

Services_Technorati provides an interface to all of the query types in
Technorati API version 1.0, and supports filesystem caching of query
data using Cache_Lite compatible cache objects.

As of version 0.7.0 this package is PHP5 only, and requires simplexml.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Services_Technorati to wrapper dla opartego na technologii REST API
webserices Technorati. Technorati to wyspecjalizowana wyszukiwarka do
blogów udostępniająca dużą liczbę interfejsów do współpracy z wpisami
na blogach, np. wyszukiwanie wpisów zawierających odnośnik do zadanej
strony, wpisy do których jest odnośnik z zadanej strony bądź też
wpisy, który niedawno nadano określone tagi.

Pakiet Services_Technorati zawiera interfejs do wszystkich typów
zapytań udostępnionych przez API Technorati w wersji 1.0, oraz pozwala
na lokalne cache'owanie wyników zapytań za pomocą obiektów
kompatybilnych z Cache_Lite.

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Services/Technorati
%{php_pear_dir}/Services/Technorati.php

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/Services_Technorati
