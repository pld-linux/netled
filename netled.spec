Summary:	NetLED monitors the RD and SD of interfaces using the LEDs on your keyboard.
Summary(pl):	NetLED powiadamia o zdarzeniach RD (Receive Data) i SD (Send Data) na dowolnym interfejsie sieciowym.
Name:		netled
Version:	3.0
Release:	1
License:	GPL
Group:		Applications/Networking
Group(de):	Applikationen/Netzwerkwesen
Group(pl):	Aplikacje/Sieciowe
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
%{__install} -d $RPM_BUILD_ROOT%{_sbindir}
%{__install} netled $RPM_BUILD_ROOT%{_sbindir}
%{__install} -d $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} netled.1 $RPM_BUILD_ROOT%{_mandir}/man8/netled.8
%{__install} -d $RPM_BUILD_ROOT%{_sysconfdir}
%{__install} netled.conf $RPM_BUILD_ROOT%{_sysconfdir}

gzip -9nf netled-3.0.lsm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
%config %{_sysconfdir}/*
%doc *.gz
