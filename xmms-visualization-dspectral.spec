Summary:	Dual Spectral Analyzer
Summary(pl.UTF-8):	Podwójna Analiza Spektralna
Name:		xmms-visualization-dspectral
Version:	1.2.1
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dspectral-v%{version}.tar.gz
# Source0-md5:	8500a7ad53841d90dfec852c080b7fd7
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	rpmbuild(macros) >= 1.125
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dual Spectral Analyzer plugin for XMMS.

%description -l pl.UTF-8
Wtyczka Podwójnej Analizy Spektralnej dla XMMS-a.

%prep
%setup -q -n dspectral-v%{version}

%build
%{__make} \
	OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{xmms_visualization_plugindir},%{xmms_datadir}}

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT%{xmms_visualization_plugindir} \
	XMMS_DATADIR=$RPM_BUILD_ROOT%{xmms_datadir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{xmms_visualization_plugindir}/*.so
%{xmms_datadir}/*
