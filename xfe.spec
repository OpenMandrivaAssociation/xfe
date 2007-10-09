Summary:	Yet another file browser
Name:		xfe
Version:	1.04
Release:	%mkrel 1
License:	GPLv2+
Group:		File tools
Url:		http://roland65.free.fr/xfe
Source0:	http://downloads.sourceforge.net/xfe/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop
BuildRequires:	libpng-devel
BuildRequires:	fox1.6-devel
BuildRequires:	libxft-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
X File Explorer (Xfe) is an MS-Explorer like file manager for X.
It is based on the popular, but discontinued, X Win Commander,
originally developed by Maxim Baranov.

Xfe aims to be the file manager of choice for all light thinking Unix addicts!

%prep
%setup -q

%build
%configure2_5x \
	--disable-rpath \
	--enable-release \
	--enable-threads=posix \
	--without-included-gettext \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--sysconfdir=%{_sysconfdir}

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std rcdir=%{_sysconfdir}/%{name}
install -D %{SOURCE1} %{buildroot}%{_datadir}/applications/xfe.desktop

%find_lang %{name}

%post
%{update_menus}

%postun
%{clean_menus}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING README TODO ChangeLog
%{_bindir}/xf*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/xferc
%{_datadir}/applications/xfe.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/%{name}/icons/xfe-theme/*.png
%{_datadir}/%{name}/icons/xfce-theme/*.png
%{_datadir}/%{name}/icons/gnome-theme/*.png
%{_datadir}/%{name}/icons/gnomeblue-theme/*.png
%{_datadir}/%{name}/icons/windows-theme/*.png
%{_mandir}/man1/*
