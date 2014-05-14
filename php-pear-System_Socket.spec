%define		_status		alpha
%define		_pearname	System_Socket
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - OO socket API
Summary(pl.UTF-8):	%{_pearname} - Zorientowane obiektowo API dla gniazd
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	10
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bd7fb3d8859abb29a632e6e063d92e79
URL:		http://pear.php.net/package/System_Socket/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.654
Requires:	php(core) >= 4.3.0
Requires:	php(sockets)
Requires:	php-pear
Requires:	php-pear-PEAR-core
Suggests:	php-pear-Log
Suggests:	php-pear-Net_IPv4 >= 1.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq_pear Net/IPv4.* Log.*

%description
Aims to provide a thight and robust OO API to PHPs socket extension
(ext/sockets).

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
W zamierzeniu ta klasa ma dostarczyć rozbudowanego, zorientowanego
obiektowo API dla gniazd - jednego z rozszerzeń PHP (ext/sockets).

Ta klasa ma w PEAR status: %{_status}.

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
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/System/*.php
%{php_pear_dir}/System/Socket
