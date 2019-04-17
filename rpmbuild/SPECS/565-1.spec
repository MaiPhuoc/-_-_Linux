Name:          565-1
Version:       1.0
Release:       1%{?dist}
Summary:       Программа студента Mai Tan Phuoc группы 565
Group:         Testing
License:       GPL
URL:           https://github.com/MaiPhuoc/Lab_linux
Source0:       %{name}-%{version}.tar.gz
BuildRequires: /bin/rm, /bin/mkdir, /bin/cp
Requires:      /bin/bash, /usr/bin/date
BuildArch:     noarch

%description
A test package

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_bindir}
install -m 755 565-1.sh %{buildroot}%{_bindir}

%files
%{_bindir}/565-1.sh

%changelog
* Wed Mar 20 2019 <Phuoc>
- Added %{_bindir}/565-1.sh
