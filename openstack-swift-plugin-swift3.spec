%{!?upstream_version: %global upstream_version %{version}%{?milestone}}
Name:		openstack-swift-plugin-swift3
Version:	1.12
Release:	1%{?dist}
Summary:	The swift3 plugin for Openstack Swift

License:	ASL 2.0
URL:		https://github.com/openstack/swift3
Source0:	https://tarballs.openstack.org/swift3/swift3-%{upstream_version}.tar.gz

BuildArch:	noarch
BuildRequires:	python2-devel
BuildRequires:	python2-pbr
BuildRequires:	python2-setuptools

Requires:	openstack-swift >= 2.14.0
Requires:   python-lxml
Requires:   python2-requests
Requires:   python2-six >= 1.9.0

%description
The swift3 plugin permits accessing Openstack Swift via the
Amazon S3 API.

%prep
%setup -q -n swift3-%{upstream_version}

%build
%{__python2} setup.py build

%install
rm -rf %{buildroot}
%{__python2} setup.py install -O1 --skip-build --root %{buildroot}

%files
%defattr(-,root,root,-)
%license LICENSE
%{python2_sitelib}/swift3-*.egg-info/
%{python2_sitelib}/swift3/
%doc AUTHORS README.md

%changelog
* Wed Feb 21 2018 RDO <dev@lists.rdoproject.org> 1.12-1
- Update to 1.12

