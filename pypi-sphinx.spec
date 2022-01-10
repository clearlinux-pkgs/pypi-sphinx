#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x102C2C17498D6B9E (i.tkomiya@gmail.com)
#
Name     : pypi-sphinx
Version  : 4.3.2
Release  : 178
URL      : https://files.pythonhosted.org/packages/5f/70/83589844bd82a5de3a748757fb39b2440435716e6a295827b13967dfa97f/Sphinx-4.3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/5f/70/83589844bd82a5de3a748757fb39b2440435716e6a295827b13967dfa97f/Sphinx-4.3.2.tar.gz
Source1  : https://files.pythonhosted.org/packages/5f/70/83589844bd82a5de3a748757fb39b2440435716e6a295827b13967dfa97f/Sphinx-4.3.2.tar.gz.asc
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
BuildRequires : pypi(alabaster)
BuildRequires : pypi(babel)
BuildRequires : pypi(docutils)
BuildRequires : pypi(imagesize)
BuildRequires : pypi(jinja2)
BuildRequires : pypi(packaging)
BuildRequires : pypi(py)
BuildRequires : pypi(pygments)
BuildRequires : pypi(requests)
BuildRequires : pypi(setuptools)
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
Requires: pypi(setuptools)
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
%setup -q -n Sphinx-4.3.2
cd %{_builddir}/Sphinx-4.3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641842289
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

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
pypi-dep-fix.py %{buildroot} docutils
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

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
