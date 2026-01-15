%bcond clang 1

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg tde-style-ia-ora
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	1.0.8
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Mandriva theme for TDE - Widget design
Group:		Environment/Desktop
URL:		http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/applications/themes/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz

BuildSystem:  cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{tde_version}
BuildRequires:	trinity-tdebase-devel >= %{tde_version}

BuildRequires:	trinity-tde-cmake >= %{tde_version}

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig
BuildRequires:	libtool

# ACL support
BuildRequires:  pkgconfig(libacl)

# GTK2 support
BuildRequires:  pkgconfig(gtk+-2.0)

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)

BuildRequires:  pkgconfig(xft)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xtst)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)

Requires:	trinity-twin

Obsoletes:	trinity-style-ia-ora < %{?epoch:%{epoch}:}%{version}-%{release}
Provides:	trinity-style-ia-ora = %{?epoch:%{epoch}:}%{version}-%{release}

%description
Mandriva theme for Trinity


%files
%defattr(-,root,root,-)
%{tde_prefix}/%{_lib}/trinity/plugins/styles/ia_ora.la
%{tde_prefix}/%{_lib}/trinity/plugins/styles/ia_ora.so
%{tde_prefix}/%{_lib}/trinity/twin3_iaora.la
%{tde_prefix}/%{_lib}/trinity/twin3_iaora.so
%{tde_prefix}/%{_lib}/trinity/twin_iaora_config.la
%{tde_prefix}/%{_lib}/trinity/twin_iaora_config.so
%{tde_prefix}/share/apps/tdestyle/themes/ia_ora.themerc
%{tde_prefix}/share/apps/twin/iaora.desktop
%{_libdir}/gtk-2.0/2.10.0/engines/libia_ora.la
%{_libdir}/gtk-2.0/2.10.0/engines/libia_ora.so
%{_datadir}/themes/Ia*
%lang(it) %{tde_prefix}/share/locale/it/LC_MESSAGES/*.mo
%lang(ka) %{tde_prefix}/share/locale/ka/LC_MESSAGES/*.mo
%lang(nl) %{tde_prefix}/share/locale/nl/LC_MESSAGES/*.mo
%lang(ru) %{tde_prefix}/share/locale/ru/LC_MESSAGES/*.mo

