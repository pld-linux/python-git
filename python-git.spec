%define 	module	git
Summary:	Python Git Library
Name:		python-%{module}
Version:	0.3.2.1
Release:	1
License:	BSD
Group:		Development/Languages
Source0:	http://pypi.python.org/packages/source/G/GitPython/GitPython-%{version}.tar.gz
# Source0-md5:	a8e8d3875d71c09993d078527d8c327e
URL:		http://pypi.python.org/pypi/GitPython/
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-gitdb
Obsoletes:	GitPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GitPython is a Python library used to interact with Git repositories.

GitPython provides object model access to your git repository. Once
you have created a repository object, you can traverse it to find
parent commit(s), trees, blobs, etc.

GitPython is a port of the grit library in Ruby created by Tom
Preston-Werner and Chris Wanstrath.

%prep
%setup -q -n GitPython-%{version}.%{subver}

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES LICENSE AUTHORS
%dir %{py_sitescriptdir}/git
%{py_sitescriptdir}/git/*.py[co]
%dir %{py_sitescriptdir}/git/index
%{py_sitescriptdir}/git/index/*.py[co]
%dir %{py_sitescriptdir}/git/objects
%{py_sitescriptdir}/git/objects/*.py[co]
%dir %{py_sitescriptdir}/git/objects/submodule
%{py_sitescriptdir}/git/objects/submodule/*.py[co]
%dir %{py_sitescriptdir}/git/refs
%{py_sitescriptdir}/git/refs/*.py[co]
%dir %{py_sitescriptdir}/git/repo
%{py_sitescriptdir}/git/repo/*.py[co]
%dir %{py_sitescriptdir}/git/test
%{py_sitescriptdir}/git/test/*.py[co]
%dir %{py_sitescriptdir}/git/test/fixtures
%{py_sitescriptdir}/git/test/fixtures/*
%dir %{py_sitescriptdir}/git/test/lib
%{py_sitescriptdir}/git/test/lib/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/GitPython-%{version}*.egg-info
%endif
