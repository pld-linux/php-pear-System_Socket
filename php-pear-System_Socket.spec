%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	Socket
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - OO socket API
Summary(pl):	%{_pearname} - Zorientowane obiektowo API dla gniazd
Name:		php-pear-%{_pearname}
Version:	0.4.1
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	bd7fb3d8859abb29a632e6e063d92e79
URL:		http://pear.php.net/package/System_Socket/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Aims to provide a thight and robust OO API to PHPs socket extension
(ext/sockets).

In PEAR status of this package is: %{_status}.

%description -l pl
W zamierzeniu ta klasa ma dostarczyæ rozbudowanego, zorientowanego
obiektowo API dla gniazd - jednego z rozszerzeñ PHP (ext/sockets).

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/docs
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
