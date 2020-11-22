Name: onion
Version: 0.1.%{?buildnum:%{buildnum}}
Release: 1%{?dist}
Group: Application/Web
License: Internal BBC use only
Summary: BBC Onion
Source0: src.tar.gz
Requires: nginx, awscli, python-boto3, git, curl, gcc, libevent-devel, openssl-devel, pcre-devel, openresty, tor

BuildRoot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildArch: noarch

%description
Alec Muffet's EOTK, baked by the BBC

%prep
%setup -T -c all



git clone git://github.com/yaoweibin/ngx_http_substitutions_filter_module.git


./configure --add-module= %{buildroot}/ngx_http_substitutions_filter_module



mkdir -p %{buildroot}/%{_bindir}

mkdir -p %{buildroot}/%{_libdir}/%{name}





%build

%install
tar -C %{buildroot} -xzf %{SOURCE0}
install -m 755 -d build-centos-8.2.2004.sh %{buildroot}/%{_libdir}/%{name}

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
%defattr(-,root,root,-)
%dir %{_libdir}/%{name}
/
%{_bindir}/%{name}/

/tmp/README.md
/tmp/eotk
/tmp/demo.d
/tmp/docs.d
/tmp/lib.d
/tmp/opt.d
/tmp/tools.d
/tmp/templates.d
