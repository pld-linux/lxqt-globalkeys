#
# Conditional build:
#
%define		qtver		5.3.1

Summary:	lxqt-globalkeys
Name:		lxqt-globalkeys
Version:	0.11.0
Release:	1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://downloads.lxqt.org/lxqt/%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	827836c3d33195efd7ddb580887c0769
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.11.0
BuildRequires:	libqtxdg-devel >= 2.0.0
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-globalkeys

%package devel
Summary:	lxqt-globalkeys - header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do lxqt-globalkeys
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	Qt5Core-devel >= %{qtver}
Requires:	Qt5Gui-devel >= %{qtver}
Requires:	Qt5Xml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt-globalkeys.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt-globalkeys.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	-DPULL_TRANSLATIONS=OFF \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

#%find_lang %{name} --all-name --with-qm

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-globalkeyshortcuts

%attr(755,root,root) %{_bindir}/lxqt-globalkeysd
%{_desktopdir}/lxqt-config-globalkeyshortcuts.desktop

#%dir %{_datadir}/lxqt/translations/lxqt-config-globalkeyshortcuts
%attr(755,root,root) %ghost %{_libdir}/liblxqt-globalkeys-ui.so.0
%attr(755,root,root) %{_libdir}/liblxqt-globalkeys-ui.so.0.11.*
%attr(755,root,root) %ghost %{_libdir}/liblxqt-globalkeys.so.0
%attr(755,root,root) %{_libdir}/liblxqt-globalkeys.so.0.11.*

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/lxqt-globalkeys-ui
%dir %{_includedir}/lxqt-globalkeys-ui/LXQtGlobalKeysUi
%{_includedir}/lxqt-globalkeys-ui/LXQtGlobalKeysUi/ShortcutSelector
%{_includedir}/lxqt-globalkeys-ui/shortcut_selector.h
%{_includedir}/lxqt-globalkeys-ui/shortcutselector.h
%dir %{_includedir}/lxqt-globalkeys
%dir %{_includedir}/lxqt-globalkeys/LXQtGlobalKeys
%{_includedir}/lxqt-globalkeys/LXQtGlobalKeys/Action
%{_includedir}/lxqt-globalkeys/LXQtGlobalKeys/Client
%{_includedir}/lxqt-globalkeys/LXQtGlobalKeys/LXQtGlobalKeys
%{_includedir}/lxqt-globalkeys/action.h
%{_includedir}/lxqt-globalkeys/client.h
%{_includedir}/lxqt-globalkeys/lxqt-globalkeys.h
%{_includedir}/lxqt-globalkeys/lxqtglobalkeys.h
%{_libdir}/liblxqt-globalkeys-ui.so
%{_libdir}/liblxqt-globalkeys.so
%{_pkgconfigdir}/lxqt-globalkeys-ui.pc
%{_pkgconfigdir}/lxqt-globalkeys.pc
%dir %{_datadir}/cmake/lxqt-globalkeys-ui
%{_datadir}/cmake/lxqt-globalkeys-ui/lxqt-globalkeys-ui-config-version.cmake
%{_datadir}/cmake/lxqt-globalkeys-ui/lxqt-globalkeys-ui-config.cmake
%{_datadir}/cmake/lxqt-globalkeys-ui/lxqt-globalkeys-ui-targets-pld.cmake
%{_datadir}/cmake/lxqt-globalkeys-ui/lxqt-globalkeys-ui-targets.cmake
%dir %{_datadir}/cmake/lxqt-globalkeys
%{_datadir}/cmake/lxqt-globalkeys/lxqt-globalkeys-config-version.cmake
%{_datadir}/cmake/lxqt-globalkeys/lxqt-globalkeys-config.cmake
%{_datadir}/cmake/lxqt-globalkeys/lxqt-globalkeys-targets-pld.cmake
%{_datadir}/cmake/lxqt-globalkeys/lxqt-globalkeys-targets.cmake
