Summary:	Shows kernel function usage in a style like 'top'
Summary(pl):	Wy¶wietlanie u¿ycia funkcji j±dra w stylu programu top
Name:		kerneltop
Version:	0.8
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://www.xenotime.net/linux/kerneltop/%{name}-%{version}.tgz
# Source0-md5:	9f8a2d7d1828505141559bbae442b0ce
URL:		http://www.xenotime.net/linux/kerneltop/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
shows kernel function usage in a style like 'top'.

%description -l pl
kerneltop pokazuje u¿ycie funkcji j±dra w stylu podobnym do programu
top.

%prep
%setup -q -c

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d  $RPM_BUILD_ROOT%{_bindir}

install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf    $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
