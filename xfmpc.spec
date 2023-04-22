Summary:	A graphical GTK+ MPD client focusing on low footprint
Summary(pl.UTF-8):	Graficzny klient MPD oparty na GTK+
Name:		xfmpc
Version:	0.3.1
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	http://archive.xfce.org/src/apps/xfmpc/0.3/%{name}-%{version}.tar.bz2
# Source0-md5:	70ee9a750306d9faf8ff51691fd2f157
URL:		http://www.xfce.org/projects/xfmpc/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.38.0
BuildRequires:	gtk+3-devel >= 3.22.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libxfce4ui-devel >= 4.14.0
BuildRequires:	libxfce4util-devel >= 4.14.0
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	xfce4-dev-tools >= 4.14.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical GTK+ MPD client focusing on low footprint.

%description -l pl.UTF-8
Graficzny klient MPD oparty na GTK+.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/locale/{fa_IR,hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/locale/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog IDEAS NEWS README.md THANKS
%attr(755,root,root) %{_bindir}/xfmpc
%{_desktopdir}/xfmpc.desktop
%{_mandir}/man1/xfmpc.1*
