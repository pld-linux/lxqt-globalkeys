#
# Conditional build:
#
%define		qtver		4.8.5

Summary:	lxqt-globalkeys
Name:		lxqt-globalkeys
Version:	0.7.0
Release:	0.1
License:	GPLv2 and LGPL-2.1+
Group:		X11/Applications
Source0:	http://lxqt.org/downloads/lxqt/0.7.0/%{name}-%{version}.tar.xz
# Source0-md5:	0c5e6974d892d08411940f4fc05b839d
URL:		http://www.lxqt.org/
BuildRequires:	cmake >= 2.8.3
BuildRequires:	liblxqt-devel >= 0.7.0
BuildRequires:	libqtxdg-devel >= 0.5.3
BuildRequires:	xz-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
lxqt-globalkeys

%package devel
Summary:	lxqt-globalkeys - header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do lxqt-globalkeys
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= %{qtver}
Requires:	QtGui-devel >= %{qtver}
Requires:	QtXml-devel >= %{qtver}

%description devel
This package contains header files and development documentation for
lxqt-globalkeys.

%description devel -l pl.UTF-8
Pakiet ten zawiera pliki nagłówkowe i dokumentację potrzebną przy
pisaniu własnych programów wykorzystujących lxqt-globalkeys.

%prep
%setup -q -c %{name}-%{version}

%build
install -d build
cd build
%cmake \
	../

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/lxqt-config-globalkeyshortcuts
%attr(755,root,root) %{_bindir}/lxqt-globalkeysd
%ghost %{_libdir}/liblxqt-globalkeys-ui.so.0
%attr(755,root,root) %{_libdir}/liblxqt-globalkeys-ui.so.*.*.*
%ghost %{_libdir}/liblxqt-globalkeys.so.0
%attr(755,root,root) %{_libdir}/liblxqt-globalkeys.so.*.*.*
%{_desktopdir}/lxqt-config-globalkeyshortcuts.desktop
%dir %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts
%lang(ar) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ar.qm
%lang(cs) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_cs.qm
%lang(cs_CZ) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_cs_CZ.qm
%lang(da) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_da_DK.qm
%lang(de) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_de.qm
%lang(de_DE) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_de_DE.qm
%lang(el) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_el_GR.qm
%lang(eo) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_eo.qm
%lang(es) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_es.qm
%lang(es_VE) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_es_VE.qm
%lang(eu) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_eu.qm
%lang(fi) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_fi.qm
%lang(fr) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_fr_FR.qm
%lang(it) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_it_IT.qm
%lang(ja) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ja.qm
%lang(lt) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_lt.qm
%lang(nl) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_nl.qm
%lang(pl) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_pl_PL.qm
%lang(pt) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_pt.qm
%lang(pt_BR) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_pt_BR.qm
%lang(ro) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ro_RO.qm
%lang(ru) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ru.qm
%lang(ru_RU) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_ru_RU.qm
%lang(sl) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_sl.qm
%lang(th) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_th_TH.qm
%lang(tr) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_tr.qm
%lang(uk) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_uk.qm
%lang(zh_CN) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_zh_CN.qm
%lang(zh_TW) %{_datadir}/lxqt/lxqt-config-globalkeyshortcuts/lxqt-config-globalkeyshortcuts_zh_TW.qm

%files devel
%defattr(644,root,root,755)
%{_includedir}/lxqt-globalkeys-ui
%{_includedir}/lxqt-globalkeys.h
%{_includedir}/lxqt-globalkeys
%{_libdir}/liblxqt-globalkeys-ui.so
%{_libdir}/liblxqt-globalkeys.so
%{_pkgconfigdir}/lxqt-globalkeys-ui.pc
%{_pkgconfigdir}/lxqt-globalkeys.pc
%{_datadir}/cmake/lxqt_globalkeys
%{_datadir}/cmake/lxqt_globalkeys_ui
