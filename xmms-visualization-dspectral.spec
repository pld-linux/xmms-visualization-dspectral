Summary:	Dual Spectral Analyzer.
Summary(pl):	Podwójna Analiza Spektralna.
Name:		xmms-visualization-dspectral
Version:	1.2
Release:	2
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://hem.passagen.se/joakime/dspectral-%{version}.tar.gz
URL:		http://hem.passagen.se/joakime/linuxapp.html
Requires:	xmms
BuildRequires:	xmms-devel >= 1.2.3
BuildRequires:	glib-devel >= 1.2.2
BuildRequires:	gtk+-devel >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Dual Spectral Analyzer plugin for XMMS.

%description -l pl
Plugin Podwójnej Analizy Spektralnej.

%prep
%setup -q -n dspectral-%{version}

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/
install -d $RPM_BUILD_ROOT/`%{_bindir}/xmms-config --data-dir`/

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --visualization-plugin-dir`/ \
	XMMS_DATADIR=$RPM_BUILD_ROOT/`%{_bindir}/xmms-config --data-dir`/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{_libdir}/xmms/*/*.so
%{_datadir}/xmms/*
