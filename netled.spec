Summary:	NetLED - interfaces RD and SD monitoring using the LEDs on your keyboard
Summary(pl.UTF-8):	NetLED - powiadamianie o zdarzeniach RD i SD na dowolnym interfejsie sieciowym
Name:		netled
# 5.0.0a looks too messy, problaby some work-in-progress
Version:	4.0.10
Release:	1
License:	GPL
Group:		Applications/Networking
Source0:	http://ftp.marginsoftware.com/subdomains/ftp/pub/software/linux/netled/%{name}-%{version}.tar.bz2
# Source0-md5:	17377504fe7c47685b460f3af6a2d4fe
# 404 URL:	http://www.marginsoftware.com/products/netled/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
NetLED monitors the RD and SD of interfaces using the LEDs on your
keyboard.

%description -l pl.UTF-8
NetLED powiadamia o zdarzeniach RD (Receive Data) i SD (Send Data) na
dowolnym interfejsie sieciowym.

%prep
%setup -q

%build
%{__make} -C src \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -DNDEBUG -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man{5,8},%{_sysconfdir}}

install src/netled $RPM_BUILD_ROOT%{_sbindir}
install doc/netled.1 $RPM_BUILD_ROOT%{_mandir}/man8/netled.8
install doc/netled.conf.5 $RPM_BUILD_ROOT%{_mandir}/man5/netled.conf.5
install data/netled.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_sbindir}/netled
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/netled.conf
%{_mandir}/man5/netled.conf.5*
%{_mandir}/man8/netled.8*
