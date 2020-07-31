Name: onion
Version: 0.1.%{?buildnum:%{buildnum}}
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: BBC Onion
Source0: src.tar.gz
Requires: nginx, awscli, python-boto3

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Alec Muffet's EOTK, baked by the BBC

%prep
%setup -T -c all

%build

%install
tar -C %{buildroot} -xzf %{SOURCE0}

%pre

getent group nginx >/dev/null || groupadd -r nginx
getent passwd nginx >/dev/null || \
    useradd -r -g nginx -G nginx -d / -s /sbin/nologin \
    -c "nginx service" nginx


getent group nginx >/dev/null || groupadd -r nginx
getent passwd nginx >/dev/null || \
    useradd -r -g nginx -G nginx -d / -s /sbin/nologin \
    -c "nginx service" nginx

%preun

%post

%postun


%clean
rm -rf %{buildroot}

%files
%defattr(644, nginx, nginx, 755)
README.md
