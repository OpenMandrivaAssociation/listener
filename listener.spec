Name: listener
Version: 2.0.0
Release: %mkrel 0
Summary: listener is a sounds detection program
Group: Sound
License: GPL
URL: http://www.vanheusden.com/listener/
Source: http://www.vanheusden.com/listener/%name-%version.tgz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}
Patch0: listener-2.0.0-mdv-makefile.patch
# BuildPreReq: kernel-headers-common
# Automatically added by buildreq on Fri Mar 12 2004
# BuildRequires: libncurses-devel libsndfile-devel libtinfo-devel
BuildRequires: libncurses-devel libsndfile-devel
Requires: libncurses libsndfile

%description
This program listens for sound. If it detects any, it starts recording
automatically and also automatically stops when things become silent
again.

%prep
%setup -q
%patch0 -p0
# -F10 -p1

%build
%make

%install
%make DESTDIR=%{buildroot} install

%clean
[ "%{buildroot}" != '/' ] && rm -rf %{buildroot}

%files
%_bindir/*
%config(noreplace) %{_sysconfdir}/*
%doc manual.html
