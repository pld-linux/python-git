#
# Conditional build:
%bcond_without	python2	# CPython 2.x module
%bcond_without	python3	# CPython 3.x module
%bcond_with	tests	# unit tests (require git checkout, not archive?)
%bcond_without	doc	# Sphinx documentation

Summary:	Python Git Library
Summary(pl.UTF-8):	Biblioteka Git dla Pythona
Name:		python-git
Version:	2.1.11
Release:	2
License:	BSD
Group:		Development/Languages/Python
#Source0Download: https://github.com/gitpython-developers/GitPython/releases
Source0:	https://github.com/gitpython-developers/GitPython/archive/%{version}/GitPython-%{version}.tar.gz
# Source0-md5:	05e5f6be4887704c8643639c24e4e3c9
URL:		https://pypi.org/project/GitPython/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-ddt >= 1.1.1
BuildRequires:	python-gitdb >= 2.0.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-ddt >= 1.1.1
BuildRequires:	python3-gitdb >= 2.0.0
%endif
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

%package -n python3-git
Summary:	Python Git Library
Summary(pl.UTF-8):	Biblioteka Git dla Pythona
Group:		Development/Languages/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-git
GitPython is a Python library used to interact with git repositories,
high-level like git-porcelain, or low-level like git-plumbing.

It provides abstractions of git objects for easy access of repository
data, and additionally allows you to access the git repository more
directly using either a pure Python implementation, or the faster, but
more resource intensive git command implementation.

%description -n python3-git -l pl.UTF-8
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
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C doc html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/git/test

%py_postclean
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/git/test
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
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
%endif

%if %{with python3}
%files -n python3-git
%defattr(644,root,root,755)
%doc AUTHORS CHANGES LICENSE README.md
%dir %{py3_sitescriptdir}/git
%{py3_sitescriptdir}/git/*.py
%{py3_sitescriptdir}/git/index
%{py3_sitescriptdir}/git/objects
%{py3_sitescriptdir}/git/refs
%{py3_sitescriptdir}/git/repo
%{py3_sitescriptdir}/git/__pycache__
%{py3_sitescriptdir}/GitPython-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc doc/build/html/{_static,*.html,*.js}
%endif
