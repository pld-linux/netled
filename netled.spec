Summary:	NetLED monitors the RD and SD of interfaces using the LEDs on your keyboard
Summary(pl):	NetLED powiadamia o zdarzeniach RD (Receive Data) i SD (Send Data) na dowolnym interfejsie sieciowym
Name:		netled
Version:	3.0
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://mars.ark.com/~mbevan/netled/files/%{name}-%{version}.tar.gz
URL:		http://mars.ark.com/~mbevan/products/netled.shtml
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetLED monitors the RD and SD of interfaces using the LEDs on your
keyboard.

%description -l pl
NetLED powiadamia o zdarzeniach RD (Receive Data) i SD (Send Data) na
dowolnym interfejsie sieciowym.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8,%{_sysconfdir}}

install netled $RPM_BUILD_ROOT%{_sbindir}
install netled.1 $RPM_BUILD_ROOT%{_mandir}/man8/netled.8
install netled.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc netled-3.0.lsm
%attr(755,root,root) %{_sbindir}/*
%config %{_sysconfdir}/*
%{_mandir}/man8/*
