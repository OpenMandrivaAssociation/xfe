Summary:	MS-Explorer-like minimalist file manager for X
Name:		xfe
Version:	1.45
Release:	1
License:	GPLv2+
Group:		File tools
Url:		http://roland65.free.fr/xfe
Source0:	http://downloads.sourceforge.net/xfe/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xft)
BuildRequires:	pkgconfig(xrandr)
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(xcb)
BuildRequires:	pkgconfig(xcb-aux)
BuildRequires:	pkgconfig(xcb-event)
BuildRequires:	pkgconfig(x11-xcb)
BuildRequires:	pkgconfig(fox)
BuildRequires:	intltool

%description
X File Explorer (Xfe) is an MS-Explorer like file manager for X.
It is based on the popular, but discontinued, X Win Commander,
originally developed by Maxim Baranov.

Xfe aims to be the file manager of choice for all light thinking Unix addicts!

%prep
%setup -q

%build
#export CXXFLAGS="-O2  -I/usr/include/fox-1.6 -DHAVE_XFT_H -DSTARTUP_NOTIFICATION"
#export LDFLAGS="-lX11 -lfreetype -lz -lXft"

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


%changelog
* Mon Apr 09 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.32.5-1
+ Revision: 790007
- update to 1.32.5
- use upstream xfe.desktop
- fix xfp.desktop

* Thu Nov 17 2011 Alexander Khrukin <akhrukin@mandriva.org> 1.32.4-1
+ Revision: 731203
- version update

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.19.2-4mdv2011.0
+ Revision: 615676
- the mass rebuild of 2010.1 packages

* Sun May 02 2010 Funda Wang <fwang@mandriva.org> 1.19.2-3mdv2010.1
+ Revision: 541529
- fix build with gcc 44

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Aug 03 2008 Frederik Himpe <fhimpe@mandriva.org> 1.19.2-1mdv2009.0
+ Revision: 261986
- update to new version 1.19.2

* Thu Jul 10 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.19.1-1mdv2009.0
+ Revision: 233529
- update to new version 1.19.1

* Mon Jun 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.19-1mdv2009.0
+ Revision: 219403
- update to new version 1.19

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Thu Jun 05 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 1.18-1mdv2009.0
+ Revision: 215216
- fix file list
- update to new version 1.18
- add missing buildrequires
- new version
- new library policy
- compile with posix thread suport

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Apr 18 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.99-1mdv2008.0
+ Revision: 14817
- new version


* Sat Feb 10 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.98-1mdv2007.0
+ Revision: 118801
- add doc files
- new version
- fix buildrequires
- add missing file

* Tue Jan 30 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.88-1mdv2007.1
+ Revision: 115565
- Import xfe

