Name:           ly-git
Version:        git
Release:        1%{?dist}
Summary:        A TUI display manager

License:        WTFPL
URL:            https://github.com/fairyglade/ly
Source0:        ly/

BuildRequires:  make automake gcc gcc-c++ kernel-devel pam-devel libxcb-devel
Requires:       pam
%description
A TUI display manager


%prep
%autosetup


%build
%make_build make


%install 
%make_install make install installsystemd


%files
%license add-license-file-here
%doc add-docs-here



%changelog
* Thu Sep 08 2022 orowith2os <93224879+orowith2os@users.noreply.github.com>
- 
