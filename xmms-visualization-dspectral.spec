Summary:	Dual Spectral Analyzer
Summary(pl):	Podwójna Analiza Spektralna
Name:		xmms-visualization-dspectral
Version:	1.2.1
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
Source0:	http://www.shell.linux.se/bm/f/dspectral-v%{version}.tar.gz
# Source0-md5:	8500a7ad53841d90dfec852c080b7fd7
URL:		http://www.shell.linux.se/bm/index.php
BuildRequires:	xmms-devel >= 1.2.3
Requires:	xmms
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _xmms_plugin_dir        %(xmms-config --visualization-plugin-dir)
%define		_xmms_data_dir		%(xmms-config --data-dir)

%description
Dual Spectral Analyzer plugin for XMMS.

%description -l pl
Plugin Podwójnej Analizy Spektralnej.

%prep
%setup -q -n dspectral-v%{version}

%build
%{__make} OPT="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_xmms_plugin_dir},%{_xmms_data_dir}}

%{__make} install \
	INSTALL-DIR=$RPM_BUILD_ROOT%{_xmms_plugin_dir} \
	XMMS_DATADIR=$RPM_BUILD_ROOT%{_xmms_data_dir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change* README
%attr(755,root,root) %{_xmms_plugin_dir}/*.so
%{_xmms_data_dir}/*
