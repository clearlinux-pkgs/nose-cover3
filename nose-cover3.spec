#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-cover3
Version  : 0.1.0
Release  : 11
URL      : https://pypi.python.org/packages/source/n/nose-cover3/nose-cover3-0.1.0.tar.gz
Source0  : https://pypi.python.org/packages/source/n/nose-cover3/nose-cover3-0.1.0.tar.gz
Summary  : Coverage 3.x support for Nose
Group    : Development/Tools
License  : LGPL-2.1
Requires: nose-cover3-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
================================
Coverage 3.x support for Nose.
================================

%package python
Summary: python components for the nose-cover3 package.
Group: Default

%description python
python components for the nose-cover3 package.


%prep
%setup -q -n nose-cover3-0.1.0

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
