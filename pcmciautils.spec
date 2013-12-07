Summary:	Tools for the hotpluggable PCMCIA subsystem
Name:		pcmciautils
Version:	018
Release:	3
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
%apply_patches

%build
%make LD=%{__cc} CC=%{__cc} V=1 OPTIMIZATION="%{optflags}" LDFLAGS="%{ldflags}" STRIPCMD=/bin/true

%install
%makeinstall_std

%files
%config(noreplace) %{_sysconfdir}/pcmcia/config.opts
/sbin/lspcmcia
/sbin/pccardctl
/lib/udev/rules.d/60-pcmcia.rules
/lib/udev/pcmcia-check-broken-cis
/lib/udev/pcmcia-socket-startup
%{_mandir}/man*/*

