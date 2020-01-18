%if 0%{?rhel} != 0 && 0%{?rhel} <= 6
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%endif

Name:           python-yubico
Version:        1.2.3
Release:        1%{?dist}
Summary:        Pure-python library for interacting with Yubikeys

License:        BSD
URL:            https://github.com/Yubico/python-yubico
Source0:        https://github.com/Yubico/python-yubico/archive/%{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python-setuptools
%if 0%{?rhel} == 0 || 0%{?rhel} >= 7
BuildRequires:  python-nose
BuildRequires:  pyusb
%endif
Requires:       pyusb

%description
Pure-python library for interacting with Yubikeys

%prep
%setup -q -n %{name}-%{name}-%{version}


%build
sed -i 's|setup_requires=|tests_require=|' setup.py
%{__python2} setup.py build


%install
%{__python2} setup.py install -O1 --skip-build --root $RPM_BUILD_ROOT


%files
%doc COPYING NEWS README
%{python2_sitelib}/*

%if 0%{?rhel} == 0 || 0%{?rhel} >= 7
%check
# Exclude tests that require a physical yubikey attached.
nosetests -e test_challenge_response -e test_serial -e test_status
%endif

%changelog
* Mon Mar 23 2015 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.3-1
- Upstream 1.2.3
- Require pyusb during building when running tests

* Mon Jun 23 2014 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-3
- Enable build on EL6.

* Sat Jun 21 2014 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-2
- Run upstream tests during build.

* Thu Jun 19 2014 Nathaniel McCallum <npmccallum@redhat.com> - 1.2.1-1
- Initial release.
