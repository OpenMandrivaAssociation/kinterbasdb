%define name	kinterbasdb
%define version	3.2
%define release	%mkrel 7
%define cflags -std=c99 $RPM_OPT_FLAGS

Summary:	A Python DB-API 2.0 compliant interface to Firebird
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		Databases
Source0:	%{name}-%{version}.src.tar.bz2
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://kinterbasdb.sourceforge.net/
Requires:	python-egenix-mx-base
#Requires:	firebird
%py_requires -d
BuildRequires:	firebird-devel

%description
KInterbasDB is a Python extension package that implements Python Database API
2.0-compliant support for the open source relational database Firebird and some
versions of its proprietary cousin Borland® Interbase®.
In addition to the minimal feature set of the standard Python DB API,
KInterbasDB also exposes nearly the entire native client API of the database
engine.

%prep
%setup -q -n %{name}-%{version}

%build
env CFLAGS="%{cflags}" /usr/bin/python setup.py build

%install
rm -rf %{buildroot}
%_bindir/python setup.py install --root=%{buildroot}
cd %{buildroot}%{python_sitearch}
%_bindir/python -c "import kinterbasdb"

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README PKG-INFO
%doc docs
%{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}-%{version}-py*.egg-info
%{py_sitedir}/%{name}/docs


