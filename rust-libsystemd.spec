# Generated by rust2rpm 10
%bcond_without check
%global debug_package %{nil}

%global crate libsystemd

Name:           rust-%{crate}
Version:        0.1.0
Release:        6%{?dist}
Summary:        Pure-Rust client library to interact with systemd

# Upstream license specification: MIT/Apache-2.0
# https://github.com/lucab/libsystemd-rs/pull/23
License:        MIT or ASL 2.0
URL:            https://crates.io/crates/libsystemd
Source:         %{crates_source}
# Initial patched metadata
# * Update quickcheck to 0.9, https://github.com/lucab/libsystemd-rs/pull/26
# * Update nix to 0.14, https://github.com/lucab/libsystemd-rs/pull/22
Patch0:         libsystemd-fix-metadata.diff

ExclusiveArch:  %{rust_arches}
%if %{__cargo_skip_build}
BuildArch:      noarch
%endif

BuildRequires:  rust-packaging

%global _description %{expand:
Pure-Rust client library to interact with systemd.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages
which use "%{crate}" crate.

%files          devel
%doc README.md
%{cargo_registry}/%{crate}-%{version}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages
which use "default" feature of "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{cargo_registry}/%{crate}-%{version}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version_no_tilde} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
* Thu Jan 30 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Fri Sep 13 20:57:31 CEST 2019 Robert-André Mauchin <zebob.m@gmail.com> - 0.1.0-5
- Update quickcheck to 0.9

* Fri Jul 26 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jun 27 17:37:46 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-3
- Regenerate

* Mon Jun 10 12:53:00 UTC 2019 Robert Fairley <rfairley@redhat.com> - 0.1.0-2
- Add license files

* Sun Jun 09 18:06:08 CEST 2019 Igor Gnatenko <ignatenkobrain@fedoraproject.org> - 0.1.0-1
- Initial package
