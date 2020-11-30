Name: eotk_bbc
Version: 0.1.%{?buildnum:%{buildnum}}
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: BBC Onion
Source0: src.tar.gz
Requires: ws-onion-openresty, nginx, awscli, python-boto3, git, curl, gcc, libevent-devel, openssl-devel, pcre-devel, openresty, tor

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Alec Muffet's EOTK, baked by the BBC

%prep
%setup -T -c all



mkdir -p %{buildroot}/%{_bindir}

mkdir -p %{buildroot}/%{_libdir}





%build
%define _unpackaged_files_terminate_build 0

%install

tar -xzf %{SOURCE0} -C %{buildroot}
install -m 755 -d build-centos-8.2.2004.sh %{buildroot}/%{_libdir}

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

%postun:


%clean
rm -rf %{buildroot}

%files
%defattr(644, nginx, nginx, 755)
%defattr(-,root,root,-)
%{_libdir}

/eotk/README.md
/eotk/eotk
/eotk/demo.d
/eotk/docs.d
/eotk/lib.d
/eotk/opt.d
/eotk/tools.d
/eotk/templates.d

