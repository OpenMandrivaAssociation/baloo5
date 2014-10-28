%define major %(echo %{version} |cut -d. -f1-3)

Summary:	Baloo is a framework for searching and managing metadata
Name:		baloo5
Version:	5.1.0.1
Release:	1
License:	GPLv2+
Group:		Graphical desktop/KDE
Url:		https://www.kde.org/
Source0:	ftp://ftp.kde.org/pub/kde/stable/plasma/%{major}/src/baloo-%{version}.tar.xz
BuildRequires:	xapian-devel
BuildRequires:	pkgconfig(akonadi)
BuildRequires:	pkgconfig(QJson)
BuildRequires:	ninja
BuildRequires:	qmake5
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5FileMetaData)
BuildRequires:	kfilemetadata5-devel
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5DBus)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Sql)
BuildRequires:	cmake(Qt5)
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
BuildRequires:	cmake(KF5KDELibs4Support)
BuildRequires:	cmake(KF5FileMetaData)
# (tpg) https://issues.openmandriva.org/show_bug.cgi?id=865
Requires:	qt5-database-plugin-sqlite

%description
Baloo is a framework for searching and managing metadata.

%files -f akonadi_baloo_indexer.lang,baloo_file.lang,baloo_file_extractor.lang,baloo_naturalqueryparser.lang,balooctl.lang,baloosearch.lang,balooshow.lang,kcm_baloofile.lang,kio_baloosearch.lang,kio_tags.lang,kio_timeline.lang
%{_sysconfdir}/dbus-1/system.d/org.kde.baloo.filewatch.conf
%{_sysconfdir}/xdg/autostart/baloo_file.desktop
%{_bindir}/baloo_file
%{_bindir}/baloo_file_cleaner
%{_bindir}/baloo_file_extractor
%{_bindir}/balooctl
%{_bindir}/baloosearch
%{_bindir}/balooshow
%{_datadir}/dbus-1/interfaces/org.kde.baloo.file.indexer.xml
%{_datadir}/dbus-1/system-services/org.kde.baloo.filewatch.service
%{_datadir}/icons/hicolor/*/*/baloo.png
%{_datadir}/polkit-1/actions/org.kde.baloo.filewatch.policy
%{_libdir}/libexec/kauth/kde_baloo_filewatch_raiselimit
%{_libdir}/plugins/kcm_baloofile.so
%{_libdir}/plugins/kded_baloosearch_kio.so
%dir %{_libdir}/plugins/kf5/baloo
%{_libdir}/plugins/kf5/baloo/calendarsearchstore.so
%{_libdir}/plugins/kf5/baloo/contactsearchstore.so
%{_libdir}/plugins/kf5/baloo/emailsearchstore.so
%{_libdir}/plugins/kf5/baloo/filesearchstore.so
%{_libdir}/plugins/kf5/baloo/notesearchstore.so
%{_libdir}/plugins/kf5/kio/baloosearch.so
%{_libdir}/plugins/kf5/kio/tags.so
%{_libdir}/plugins/kf5/kio/timeline.so
%{_datadir}/kservices5/baloosearch.protocol
%{_datadir}/kservices5/kcm_baloofile.desktop
%{_datadir}/kservices5/tags.protocol
%{_datadir}/kservices5/timeline.protocol
%{_datadir}/kservices5/kded/baloosearchfolderupdater.desktop
%{_libdir}/qml/org/kde/baloo

#----------------------------------------------------------------------------

%define baloocore_major 1
%define libbaloocore %mklibname KF5BalooCore %{baloocore_major}

%package -n %{libbaloocore}
Summary:	Baloo Core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libbaloocore}
Baloo Core library

The core library of the Baloo file indexing service.

%files -n %{libbaloocore}
%{_libdir}/libKF5BalooCore.so.%{baloocore_major}*
%{_libdir}/libKF5BalooCore.so.%{major}

#----------------------------------------------------------------------------

%define baloofiles_major 1
%define libbaloofiles %mklibname KF5BalooFiles %{baloofiles_major}

%package -n %{libbaloofiles}
Summary:	Shared library for Baloo
Group:		System/Libraries

%description -n %{libbaloofiles}
The Baloo file handling library, a part of the Baloo indexing framework

%files -n %{libbaloofiles}
%{_libdir}/libKF5BalooFiles.so.%{baloofiles_major}*
%{_libdir}/libKF5BalooFiles.so.%{major}

#----------------------------------------------------------------------------

%define baloonqp_major 1
%define libbaloonqp %mklibname KF5BalooNaturalQueryParser %{baloonqp_major}

%package -n %{libbaloonqp}
Summary:	Shared library for Baloo
Group:		System/Libraries

%description -n %{libbaloonqp}
The Baloo natural query parser library, a part of the Baloo indexing framework

%files -n %{libbaloonqp}
%{_libdir}/libKF5BalooNaturalQueryParser.so.%{baloonqp_major}*
%{_libdir}/libKF5BalooNaturalQueryParser.so.%{major}


#----------------------------------------------------------------------------

%define balooxapian_major 1
%define libbalooxapian %mklibname KF5BalooXapian %{balooxapian_major}

%package -n %{libbalooxapian}
Summary:	Xapian backend for Baloo
Group:		System/Libraries

%description -n %{libbalooxapian}
Xapian backend for the Baloo indexing framework

%files -n %{libbalooxapian}
%{_libdir}/libKF5BalooXapian.so.%{balooxapian_major}*
%{_libdir}/libKF5BalooXapian.so.%{major}

#----------------------------------------------------------------------------

%define devbaloo %mklibname baloo5 -d

%package -n %{devbaloo}
Summary:	Development files for Baloo
Group:		Development/KDE and Qt
Requires:	%{libbalooxapian} = %{EVRD}
Requires:	%{libbaloofiles} = %{EVRD}
Requires:	%{libbaloocore} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{devbaloo}
This package contains header files needed if you wish to build applications
based on Baloo.

%files -n %{devbaloo}
%{_includedir}/KF5/Baloo/
%{_includedir}/KF5/baloo_version.h
%{_libdir}/*.so
%{_libdir}/cmake/KF5Baloo

#--------------------------------------------------------------------

%prep
%setup -qn baloo-%{major}

%build
%cmake -G Ninja
ninja

%install
DESTDIR="%{buildroot}" ninja -C build install
%find_lang akonadi_baloo_indexer
%find_lang baloo_file
%find_lang baloo_file_extractor
%find_lang baloo_naturalqueryparser
%find_lang balooctl
%find_lang baloosearch
%find_lang balooshow
%find_lang kcm_baloofile
%find_lang kio_baloosearch
%find_lang kio_tags
%find_lang kio_timeline
