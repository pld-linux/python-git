#
# Conditional build:
%bcond_with	tests	# unit tests (require git checkout, not archive?)
%bcond_without	doc	# Sphinx documentation

Summary:	Python Git Library
Summary(pl.UTF-8):	Biblioteka Git dla Pythona
Name:		python-git
Version:	2.1.15
Release:	1
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/gitpython-developers/GitPython/releases
Source0:	https://github.com/gitpython-developers/GitPython/archive/%{version}/GitPython-%{version}.tar.gz
# Source0-md5:	e6dfd0204f5b626f69ae904a2e392c91
URL:		https://pypi.org/project/GitPython/
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-ddt >= 1.1.1
BuildRequires:	python-gitdb >= 2.0.0
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%{?with_doc:BuildRequires:	sphinx-pdg}
Requires:	python-modules >= 1:2.7
Obsoletes:	GitPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GitPython is a Python library used to interact with git repositories,
high-level like git-porcelain, or low-level like git-plumbing.

It provides abstractions of git objects for easy access of repository
data, and additionally allows you to access the git repository more
directly using either a pure Python implementation, or the faster, but
more resource intensive git command implementation.

%description -l pl.UTF-8
GitPython to biblioteka Pythona służąca do pracy z repozytoriami gita,
wysokopoziomowo, jak git-porcelain lub niskopoziomowo, jak
git-plumbing.

Biblioteka udostępnia abstrakcje obiektów gita, zapewniając łatwy
dostęp do danych repozytorium, a ponadto pozwala na dostęp do
repozytorium bardziej bezpośrednio albo przy użyciu czysto pythonowej
implementacji, albo szybciej, ale z większym zużyciem zasobów, przy
użyciu implementacji poleceń gita.

%package apidocs
Summary:	API documentation for GitPython library
Summary(pl.UTF-8):	Dokumentacja API biblioteki GitPython
Group:		Documentation

%description apidocs
API documentation for GitPython library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki GitPython.

%prep
%setup -q -n GitPython-%{version}

%build
%py_build %{?with_tests:test}

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/git/test

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.md
%dir %{py_sitescriptdir}/git
%{py_sitescriptdir}/git/*.py[co]
%{py_sitescriptdir}/git/index
%{py_sitescriptdir}/git/objects
%{py_sitescriptdir}/git/refs
%{py_sitescriptdir}/git/repo
%{py_sitescriptdir}/GitPython-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,*.html,*.js}
%endif
