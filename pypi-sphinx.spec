#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: pyproject
#
Name     : pypi-sphinx
Version  : 7.2.4
Release  : 210
URL      : https://files.pythonhosted.org/packages/a8/6a/c4cb054ac1a96cf5990b4b397e3ddd81f0cb7a3122cd98b4ec57adfb0f23/sphinx-7.2.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/a8/6a/c4cb054ac1a96cf5990b4b397e3ddd81f0cb7a3122cd98b4ec57adfb0f23/sphinx-7.2.4.tar.gz
Summary  : Python documentation generator
Group    : Development/Tools
License  : MIT
Requires: pypi-sphinx-bin = %{version}-%{release}
Requires: pypi-sphinx-python = %{version}-%{release}
Requires: pypi-sphinx-python3 = %{version}-%{release}
Requires: pypi(alabaster)
Requires: pypi(imagesize)
Requires: pypi(requests)
Requires: pypi(snowballstemmer)
Requires: pypi(sphinxcontrib_websupport)
Requires: pypi-docutils
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

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

%description bin
bin components for the pypi-sphinx package.


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
%setup -q -n sphinx-7.2.4
cd %{_builddir}/sphinx-7.2.4
pushd ..
cp -a sphinx-7.2.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693254043
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
pypi-dep-fix.py . docutils
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pypi-dep-fix.py . docutils
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
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
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
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

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
