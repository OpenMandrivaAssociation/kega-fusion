%define		oname		Fusion
%define		name		kega-fusion
%define		version		363x

%define		debug_package	%{nil}

Name:		%{name}
Version:	%{version}
Release:	3
Summary:	Sega Genesis/32X/Master System/CD/SG-1000/Pico Emulator
Group:		Emulators
License:	Freeware
URL:		https://www.eidolons-inn.net/tiki-index.php?page=Kega
Source:		%{oname}%{version}.tar.gz
Source1:	%{oname}.png
BuildRequires:	imagemagick
BuildRequires:	upx
ExclusiveArch:	%{ix86}
Obsoletes:	%{oname} <= %{version}
BuildRoot:	%{_tmppath}/%{name}-%{version}-build

%description
Kega Fusion is a Sega SG1000, SC3000, SF7000, Master System, Game Gear,
Genesis/Megadrive, SVP, Pico, SegaCD/MegaCD and 32X emulator.

Requires BIOS ROMs for Sega CD and 32X.

%prep
%setup -q -n %{oname}

%build
upx -d %{oname}

%install
%__rm -rf %{buildroot}
# install section
%__install -D -m 755 %{oname} %{buildroot}%{_bindir}/%{name}

#Icons
%__mkdir_p %{buildroot}%{_datadir}/pixmaps/
%__install -c -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%__mkdir_p %{buildroot}/%{_miconsdir} \
	 %{buildroot}/%{_liconsdir} \
	 %{buildroot}/%{_iconsdir}

%__install -m 644 %{SOURCE1} %{buildroot}/%{_miconsdir}/%{name}.png
%__install -m 644 %{SOURCE1} %{buildroot}/%{_iconsdir}/%{name}.png
%__install -m 644 %{SOURCE1} %{buildroot}/%{_liconsdir}/%{name}.png
convert %{buildroot}%{_miconsdir}/%{name}.png -resize 16x16 %{buildroot}%{_miconsdir}/%{name}.png
convert %{buildroot}%{_iconsdir}/%{name}.png -resize 32x32 %{buildroot}%{_iconsdir}/%{name}.png

# install menu entries
%__mkdir_p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=Sega Genesis/32X/Master System/CD/SG-1000/Pico Emulator
Exec=%{name}
Icon=%{name}
Type=Application
Terminal=false
Categories=X-MandrivaLinux-MoreApplications-Emulators;Emulator;
EOF

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc History.txt Readme.txt
%{_bindir}/%{name}
# desktop integration
%{_iconsdir}/*.png
%{_miconsdir}/*.png
%{_liconsdir}/*.png
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

