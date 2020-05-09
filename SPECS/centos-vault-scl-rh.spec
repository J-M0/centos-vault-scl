Name:           centos-vault-scl-rh
Version:        0.2
Release:        1%{?dist}
Summary:        Software collections from the CentOS SCLo SIG vault (upstream scl only)

License:        MIT
Source0:        CentOS-Vault-SCLo-scl-rh.repo

BuildArch:      noarch

Requires:       centos-release-scl-rh

%description
yum Configs for removed Software Collections as delivered via the CentOS SCLo SIG.

%prep

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Vault-SCLo-scl-rh.repo


%files
%defattr(-,root,root)
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Vault-SCLo-scl-rh.repo


%changelog
