Name:		listener
Version:	2.0.0
Release:	2
Summary:	A sounds detection program
Group:		Sound
License:	GPL
URL:		https://www.vanheusden.com/listener/
Source:		http://www.vanheusden.com/listener/%{name}-%{version}.tgz
Patch0:		listener-2.0.0-mdv-makefile.patch
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(sndfile)

%description
This program listens for sound. If it detects any, it starts recording
automatically and also automatically stops when things become silent
again.

%prep
%setup -q
%patch0 -p0

%build
%make

%install
%makeinstall_std

%files
%{_bindir}/*
%config(noreplace) %{_sysconfdir}/*
%doc manual.html

