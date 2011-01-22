%define 	module	git
%define		subver	beta1
%define		rel		1
Summary:	Python Git Library
Name:		python-%{module}
Version:	0.2.0
Release:	0.%{subver}.%{rel}
License:	BSD
Group:		Development/Languages
URL:		http://pypi.python.org/pypi/GitPython/
Source0:	http://pypi.python.org/packages/source/G/GitPython/GitPython-%{version}-%{subver}.tar.gz
# Source0-md5:	88a5972c28917d1c32ec28f358f620df
BuildRequires:	python-devel
BuildRequires:	python-modules
BuildRequires:	python-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
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
%setup -q -n GitPython-%{version}-%{subver}

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
%doc README CHANGES LICENSE AUTHORS
%dir %{py_sitescriptdir}/git
%{py_sitescriptdir}/git/*.py[co]
%dir %{py_sitescriptdir}/git/objects
%{py_sitescriptdir}/git/objects/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/GitPython-%{version}*.egg-info
%endif