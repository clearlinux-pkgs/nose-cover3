#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nose-cover3
Version  : 0.1.0
Release  : 20
URL      : https://files.pythonhosted.org/packages/f0/17/8c55242e86830a006bbaa0463f4a1da44f332ef7cd5a402f459c8dbaaf84/nose-cover3-0.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/17/8c55242e86830a006bbaa0463f4a1da44f332ef7cd5a402f459c8dbaaf84/nose-cover3-0.1.0.tar.gz
Summary  : Coverage 3.x support for Nose
Group    : Development/Tools
License  : LGPL-2.1
Requires: nose-cover3-python3
Requires: nose-cover3-license
Requires: nose-cover3-python
BuildRequires : buildreq-distutils3
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Coverage 3.x support for Nose.
        ================================

%package license
Summary: license components for the nose-cover3 package.
Group: Default

%description license
license components for the nose-cover3 package.


%package python
Summary: python components for the nose-cover3 package.
Group: Default
Requires: nose-cover3-python3

%description python
python components for the nose-cover3 package.


%package python3
Summary: python3 components for the nose-cover3 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the nose-cover3 package.


%prep
%setup -q -n nose-cover3-0.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532382829
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/nose-cover3
cp LICENSE %{buildroot}/usr/share/doc/nose-cover3/LICENSE
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/doc/nose-cover3/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
