#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-sphinx
Version  : 5.1.1
Release  : 187
URL      : https://files.pythonhosted.org/packages/3a/30/ac07935542607c876f3fcee1c1ab043d253332567009994a1bf71d9b55cd/Sphinx-5.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/3a/30/ac07935542607c876f3fcee1c1ab043d253332567009994a1bf71d9b55cd/Sphinx-5.1.1.tar.gz
Summary  : Python documentation generator
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx-bin = %{version}-%{release}
Requires: pypi-sphinx-license = %{version}-%{release}
Requires: pypi-sphinx-python = %{version}-%{release}
Requires: pypi-sphinx-python3 = %{version}-%{release}
Requires: pypi(alabaster)
Requires: pypi(imagesize)
Requires: pypi(requests)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinxcontrib_websupport)
Requires: pypi-docutils
BuildRequires : buildreq-distutils3
BuildRequires : pypi(alabaster)
BuildRequires : pypi(babel)
BuildRequires : pypi(docutils)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(packaging)
BuildRequires : pypi(py)
BuildRequires : pypi(pygments)
BuildRequires : pypi(requests)
BuildRequires : pypi(snowballstemmer)
BuildRequires : pypi(sphinxcontrib_applehelp)
BuildRequires : pypi(sphinxcontrib_devhelp)
BuildRequires : pypi(sphinxcontrib_htmlhelp)
BuildRequires : pypi(sphinxcontrib_jsmath)
BuildRequires : pypi(sphinxcontrib_qthelp)
BuildRequires : pypi(sphinxcontrib_serializinghtml)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
========
Sphinx
========
.. image:: https://img.shields.io/pypi/v/sphinx.svg
:target: https://pypi.org/project/Sphinx/
:alt: Package on PyPI

%package bin
Summary: bin components for the pypi-sphinx package.
Group: Binaries
Requires: pypi-sphinx-license = %{version}-%{release}

%description bin
bin components for the pypi-sphinx package.


%package license
Summary: license components for the pypi-sphinx package.
Group: Default

%description license
license components for the pypi-sphinx package.


%package python
Summary: python components for the pypi-sphinx package.
Group: Default
Requires: pypi-sphinx-python3 = %{version}-%{release}

%description python
python components for the pypi-sphinx package.


%package python3
Summary: python3 components for the pypi-sphinx package.
Group: Default
Requires: python3-core
Provides: pypi(sphinx)
Requires: pypi(alabaster)
Requires: pypi(babel)
Requires: pypi(docutils)
Requires: pypi(imagesize)
Requires: pypi(jinja2)
Requires: pypi(packaging)
Requires: pypi(pygments)
Requires: pypi(requests)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinxcontrib_applehelp)
Requires: pypi(sphinxcontrib_devhelp)
Requires: pypi(sphinxcontrib_htmlhelp)
Requires: pypi(sphinxcontrib_jsmath)
Requires: pypi(sphinxcontrib_qthelp)
Requires: pypi(sphinxcontrib_serializinghtml)

%description python3
python3 components for the pypi-sphinx package.


%prep
%setup -q -n Sphinx-5.1.1
cd %{_builddir}/Sphinx-5.1.1
pushd ..
cp -a Sphinx-5.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1658942716
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . docutils
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . docutils
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-sphinx
cp %{_builddir}/Sphinx-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-sphinx/56a684b1be3bc361790ffa2bcf39d0a140b4ac2b
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} docutils
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/sphinx-apidoc
/usr/bin/sphinx-autogen
/usr/bin/sphinx-build
/usr/bin/sphinx-quickstart

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-sphinx/56a684b1be3bc361790ffa2bcf39d0a140b4ac2b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
