# filter bad requires on private lib
%define __noautoreq 'devel\\(libKF5BalooEngine.*'

Summary:	Baloo is a framework for searching and managing metadata
Name:		baloo5
Version:	5.14.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	http://download.kde.org/stable/frameworks/%(echo %{version} |cut -d. -f1-2)/baloo-%{version}.tar.xz
Patch1:		baloo-5.13.0-pkgconfig.patch
BuildRequires:	pkgconfig(QJson)
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5DBus)
BuildRequires:	pkgconfig(Qt5Gui)
BuildRequires:	pkgconfig(Qt5Network)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Sql)
BuildRequires:	pkgconfig(Qt5Test)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	pkgconfig(Qt5Xml)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Gettext)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5Service)
BuildRequires:	cmake(KF5IdleTime)
BuildRequires:	cmake(KF5KCMUtils)
BuildRequires:	cmake(KF5Auth)
BuildRequires:	cmake(KF5Crash)
BuildRequires:	cmake(KF5Solid)
BuildRequires:	cmake(KF5KIO)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	cmake(KF5AkonadiServer)
BuildRequires:	lmdb-devel
# (tpg) https://issues.openmandriva.org/show_bug.cgi?id=865
Requires:	qt5-database-plugin-sqlite
Requires:	kfilemetadata5

%description
Baloo is a framework for searching and managing metadata.

%files -f baloo_file.lang,baloo_file_extractor.lang,balooctl.lang,baloosearch.lang,balooshow.lang,kio_baloosearch.lang,kio_tags.lang,kio_timeline.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.baloo.filewatch.conf
%{_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_bindir}/baloo_file
%{_bindir}/baloo_file_extractor
%{_bindir}/baloo-monitor
%{_bindir}/balooctl
%{_bindir}/baloosearch
%{_bindir}/balooshow
%{_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.fileindexer.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.main.xml
%{_datadir}/dbus-1/interfaces/org.kde.baloo.scheduler.xml
%{_datadir}/dbus-1/system-services/org.kde.baloo.filewatch.service
%{_datadir}/icons/hicolor/*/*/baloo.png
%{_datadir}/polkit-1/actions/org.kde.baloo.filewatch.policy
%{_libdir}/libexec/kauth/kde_baloo_filewatch_raiselimit
%{_libdir}/qt5/plugins/kf5/kded/baloosearchmodule.so
%{_libdir}/qt5/plugins/kf5/kio/baloosearch.so
%{_libdir}/qt5/plugins/kf5/kio/tags.so
%{_libdir}/qt5/plugins/kf5/kio/timeline.so
%{_datadir}/kservices5/baloosearch.protocol
%{_datadir}/kservices5/tags.protocol
%{_datadir}/kservices5/timeline.protocol
%{_libdir}/qt5/qml/org/kde/baloo

#----------------------------------------------------------------------------

%define baloo_major 5
%define libbaloo %mklibname KF5Baloo %{baloo_major}

%package -n %{libbaloo}
Summary:	Baloo Core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
Obsoletes:	%{mklibname KF5BalooCore 1}
Obsoletes:	%{mklibname KF5BalooFiles 1}
Obsoletes:	%{mklibname KF5BalooNaturalQueryParser 1}
Obsoletes:	%{mklibname KF5Baloo 1} < 5.13.0

%description -n %{libbaloo}
Baloo Core library

The core library of the Baloo file indexing service.

%files -n %{libbaloo}
%{_libdir}/libKF5Baloo.so.%{baloo_major}
%{_libdir}/libKF5Baloo.so.%{version}

#----------------------------------------------------------------------------

%define balooengine_major 5
%define libbalooengine %mklibname KF5BalooEngine %{balooengine_major}

%package -n %{libbalooengine}
Summary:	Plasma searching and managing metadata shared library
Group:		System/Libraries

%description -n %{libbalooengine}
Plasma searching and managing metadata shared library.

%files -n %{libbalooengine}
%{_libdir}/libKF5BalooEngine.so.%{balooengine_major}
%{_libdir}/libKF5BalooEngine.so.%{version}

#----------------------------------------------------------------------------

%define devbaloo %mklibname baloo5 -d

%package -n %{devbaloo}
Summary:	Development files for Baloo
Group:		Development/KDE and Qt
Requires:	%{libbaloo} = %{EVRD}
Requires:	%{libbalooengine} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloo}
This package contains header files needed if you wish to build applications
based on Baloo.

%files -n %{devbaloo}
%{_includedir}/KF5/Baloo/
%{_includedir}/KF5/baloo_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5Baloo
%{_libdir}/pkgconfig/Baloo.pc

#--------------------------------------------------------------------

%prep
%setup -qn baloo-%{version}
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%find_lang baloo_file
%find_lang baloo_file_extractor
%find_lang balooctl
%find_lang baloosearch
%find_lang balooshow
%find_lang kio_baloosearch
%find_lang kio_tags
%find_lang kio_timeline
