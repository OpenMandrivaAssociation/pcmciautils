Summary:	Tools for the hotpluggable PCMCIA subsystem
Name:		pcmciautils
Version:	018
Release:	15
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.kernel.org/pub/linux/utils/kernel/pcmcia/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		makefile_fix.patch
BuildRequires:	byacc
BuildRequires:	flex
BuildRequires:	sysfsutils-devel

%description
PCMCIAutils contains hotplug scripts and initialization tools
necessary to allow the PCMCIA subsystem to behave (almost) as every
other hotpluggable bus system (e.g. USB, IEEE1394).

Please note that the kernel support for this new feature is only
present since 2.6.13-rc1.

%prep
%setup -q
%autopatch -p1

%build
%make LD=%{__cc} CC=%{__cc} YACC=byacc V=1 OPTIMIZATION="%{optflags}" LDFLAGS="%{ldflags}" STRIPCMD=true prefix=%{_prefix} sbindir=%{_bindir} mandir=%{_mandir} etcdir=%{_sysconfdir}

%install
%make_install prefix=%{_prefix} sbindir=%{_bindir} mandir=%{_mandir} etcdir=%{_sysconfdir}

%files
%config(noreplace) %{_sysconfdir}/pcmcia/config.opts
%{_bindir}/lspcmcia
%{_bindir}/pccardctl
%{_prefix}/lib/udev/rules.d/60-pcmcia.rules
%{_prefix}/lib/udev/pcmcia-check-broken-cis
%{_prefix}/lib/udev/pcmcia-socket-startup
%{_mandir}/man*/*

