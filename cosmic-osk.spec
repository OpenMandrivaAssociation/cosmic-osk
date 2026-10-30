%define         appid com.system76.CosmicOSK
Name:           cosmic-osk
Version:        1.11.0
Release:        %{?beta:0.%{beta}.}1
Summary:        COSMIC On-Screen Keyboard
Group:          Desktop/COSMIC
License:        GPL-3.0-only
URL:            https://github.com/pop-os/cosmic-osk
Source0:        https://github.com/pop-os/cosmic-osk/archive/epoch-%{version}%{?beta:-%{beta}}/%{name}-epoch-%{version}%{?beta:-%{beta}}.tar.gz
Source1:        vendor.tar.xz

BuildRequires:  rust-packaging
BuildRequires:  just
BuildRequires:	make
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(xkbcommon)

%description
%{summary}.

%prep
%autosetup -n %{name}-epoch-%{version}%{?beta:-%{beta}} -a1 -p1
mkdir .cargo
cp %{SOURCE2} .cargo/config

%build
just build-release

%install
just rootdir=%{buildroot} prefix=%{_prefix} install

%files
%license LICENSE
%{_bindir}/%{name}
