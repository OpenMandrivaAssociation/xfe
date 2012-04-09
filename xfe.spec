Summary:	MS-Explorer-like minimalist file manager for X
Name:		xfe
Version:	1.32.5
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://roland65.free.fr/xfe
Source0:	http://downloads.sourceforge.net/xfe/%{name}-%{version}.tar.gz
Patch0:		xfe-1.32.2-missing_Xlib_h.patch
Patch1:		xfe-1.32.5-mdv-xfp_desktop.patch
BuildRequires:	libpng-devel
BuildRequires:	fox1.6-devel
BuildRequires:	libxft-devel
BuildRequires:	intltool

%description
X File Explorer (Xfe) is an MS-Explorer like file manager for X.
It is based on the popular, but discontinued, X Win Commander,
originally developed by Maxim Baranov.

Xfe aims to be the file manager of choice for all light thinking Unix addicts!

%prep
%setup -q
%patch0 -p0
%patch1 -p1

%build
export CXXFLAGS="-O2  -I/usr/include/fox-1.6 -DHAVE_XFT_H -DSTARTUP_NOTIFICATION"
export LDFLAGS="-lX11 -lfreetype -lz -lXft"

%configure2_5x \
	--disable-rpath \
	--enable-release \
	--enable-threads=posix \
	--without-included-gettext

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std rcdir=%{_sysconfdir}/%{name}

%find_lang %{name}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README TODO ChangeLog
%{_bindir}/xf*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/xferc
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/pixmaps/*.xpm
%{_datadir}/%{name}/icons
%{_mandir}/man1/*
