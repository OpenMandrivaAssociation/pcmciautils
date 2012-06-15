Summary:	Tools for the hotpluggable PCMCIA subsystem
Name:		pcmciautils
Version:	018
Release:	1
Source0:	%{name}-%{version}.tar.bz2
Patch0:		pcmciautils-015-parallel.patch
Patch1:		pcmciautils-015-libudevdir.patch
License:	GPLv2
Group:		System/Kernel and hardware
Url:		http://www.kernel.org/pub/linux/utils/kernel/pcmcia/
BuildRequires:	byacc
BuildRequires:	sysfsutils-devel
BuildRequires:	flex
%rename		pcmcia-cs

%description
PCMCIAutils contains hotplug scripts and initialization tools
necessary to allow the PCMCIA subsystem to behave (almost) as every
other hotpluggable bus system (e.g. USB, IEEE1394).

Please note that the kernel support for this new feature is only
present since 2.6.13-rc1.

%prep
%setup -q
%patch0 -p1 -b .parallel~
%patch1 -p1 -b .libudevdir~

%build
%make V=1 OPTIMIZATION="%{optflags}" LDFLAGS="%{ldflags}"

%install
%makeinstall_std

%files
%config(noreplace) %{_sysconfdir}/pcmcia/config.opts
%{_sysconfdir}/udev/rules.d/60-pcmcia.rules
/sbin/lspcmcia
/sbin/pccardctl
/lib/udev/pcmcia-check-broken-cis
/lib/udev/pcmcia-socket-startup
%{_mandir}/man*/*
