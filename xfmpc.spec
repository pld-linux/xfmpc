Summary:	A graphical GTK+ MPD client focusing on low footprint
Summary(pl.UTF-8):	Graficzny klient MPD oparty na GTK+
Name:		xfmpc
Version:	0.4.0
Release:	1
License:	GPL v2
Group:		X11/Applications/Sound
Source0:	https://archive.xfce.org/src/apps/xfmpc/0.4/%{name}-%{version}.tar.xz
# Source0-md5:	cbc6df32455d105c0da4ba3376f3bfe4
URL:		https://www.xfce.org/projects/xfmpc/
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.66.0
BuildRequires:	gtk+3-devel >= 3.24.0
BuildRequires:	libmpd-devel >= 0.15.0
BuildRequires:	libxfce4ui-devel >= 4.18.0
BuildRequires:	libxfce4util-devel >= 4.18.0
BuildRequires:	meson >= 0.54.0
BuildRequires:	ninja
BuildRequires:	pkgconfig >= 1:0.9.0
BuildRequires:	vala >= 0.14.0
BuildRequires:	vala-libxfce4ui >= 4.18.0
BuildRequires:	xfce4-dev-tools >= 4.18.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A graphical GTK+ MPD client focusing on low footprint.

%description -l pl.UTF-8
Graficzny klient MPD oparty na GTK+.

%prep
%setup -q

%build
%meson
%meson_build

%install
rm -rf $RPM_BUILD_ROOT

%meson_install

%{__rm} -r $RPM_BUILD_ROOT%{_localedir}/{fa_IR,hye,ie,ur_PK}
%{__mv} $RPM_BUILD_ROOT%{_localedir}/{hy_AM,hy}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS IDEAS NEWS README.md THANKS
%attr(755,root,root) %{_bindir}/xfmpc
%{_desktopdir}/xfmpc.desktop
%{_mandir}/man1/xfmpc.1*
