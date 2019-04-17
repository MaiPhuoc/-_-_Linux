Name:       c-565-1
Version:    1.0
Release:    1%{?dist}
Summary:    Программа студента Phuoc группы 565
Group:      Testing
License:    GPL
URL:        https://github.com/MaiPhuoc/Lab_linux
Source:     %{name}-%{version}.tar.gz
BuildRequires: gcc

%description
A test package

%prep
%setup -q

%build
gcc -O2 -o c-565-1 c-565-1-1.0.c

%install
mkdir -p %{buildroot}%{_bindir}
cp c-565-1 %{buildroot}%{_bindir}

%files
%{_bindir}/c-565-1

%changelog
* Wed Mar 25 2019 <Mai>
- Added %{_bindir}/c-565-1
