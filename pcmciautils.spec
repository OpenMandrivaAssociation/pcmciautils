Summary: Tools for the hotpluggable PCMCIA subsystem
Name: pcmciautils
Version: 015
Release: %mkrel 1
Source0: %{name}-%{version}.tar.bz2
Patch0:	 pcmciautils-015-parallel.patch
License: GPL
Group: System/Kernel and hardware
Url: http://www.kernel.org/pub/linux/utils/kernel/pcmcia/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: byacc
BuildRequires: libsysfs-devel
BuildRequires: flex
Provides:     pcmcia-cs
Obsoletes:     pcmcia-cs
Conflicts:	drakxtools-backend < 10.4.33-1mdv2007.0

%description
PCMCIAutils contains hotplug scripts and initialization tools
necessary to allow the PCMCIA subsystem to behave (almost) as every
other hotpluggable bus system (e.g. USB, IEEE1394).

Please note that the kernel support for this new feature is only
present since 2.6.13-rc1.

%prep
%setup -q
%patch0 -p1 -b .parallel

%build
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

# write /etc/modprobe.preload.d/pcmcia file on migration from old pcmcia-cs
%triggerpostun -p /usr/bin/perl -- pcmcia-cs, %{name} < 014-3mdv2007.0
use lib qw(/usr/lib/libDrakX);
use harddrake::autoconf;
use detect_devices;
my $controller = detect_devices::pcmcia_controller_probe();
harddrake::autoconf::pcmcia($controller && $controller->{driver});

%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/pcmcia/config.opts
%{_sysconfdir}/udev/rules.d/60-pcmcia.rules
/sbin/lspcmcia
/sbin/pccardctl
/sbin/pcmcia-check-broken-cis
/sbin/pcmcia-socket-startup
%{_mandir}/man*/*
