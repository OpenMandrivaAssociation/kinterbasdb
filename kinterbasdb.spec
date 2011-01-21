%define name	kinterbasdb
%define version	3.3.0
%define release	%mkrel 1

Summary:	A Python DB-API 2.0 compliant interface to Firebird
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		Databases
Source0:	%{name}-%{version}.tar.bz2
Patch0:		kinterbasdb-3.3.0-link-m.patch
Group:		Development/Python
BuildRoot:	%{_tmppath}/%{name}-buildroot
URL:		http://www.firebirdsql.org/
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
%patch0 -p0

%build
CFLAGS="%{optflags}" /usr/bin/python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README PKG-INFO
%doc docs
%{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}-%{version}-py*.egg-info
