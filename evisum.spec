Summary:	Evisum - System Monitor
Name:		evisum
Version:	0.6.1
Release:	1
License:	BSD
Group:		Applications
Source0:	https://download.enlightenment.org/rel/apps/evisum/%{name}-%{version}.tar.xz
# Source0-md5:	6b1664da537a5a310b7544a15c7b56ca
URL:		http://enlightenment.org/
BuildRequires:	efl-devel >= 1.27.0
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.726
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a process and system monitor for Linux, OpenBSD, FreeBSD and
DragonFlyBSD. It is server-client based and includes rudimentary tools
for process, CPU, memory, network, storage and sensor querying. The
current set of features aims to reach a common denominator between the
three popular and viable Unix-like operating systems at this time:
Linux, FreeBSD and OpenBSD.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS BUGS COPYING CREDITS README TODO
%attr(755,root,root) %{_bindir}/evisum
%{_desktopdir}/evisum*.desktop
%{_datadir}/evisum
%{_iconsdir}/hicolor/*x*/apps/evisum*.png
