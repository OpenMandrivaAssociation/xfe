Summary:	Yet another file browser
Name:		xfe
Version:	1.18
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

%if %mdkversion < 200900
%post
%{update_menus}
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS README TODO ChangeLog
%{_bindir}/xf*
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/%{name}/xferc
%{_datadir}/applications/xfe.desktop
%{_datadir}/pixmaps/*.png
%{_datadir}/%{name}/icons
%{_mandir}/man1/*
