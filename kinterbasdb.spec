%define name	kinterbasdb
%define version	3.3.0
%define release	2

Summary:	A Python DB-API 2.0 compliant interface to Firebird
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	BSD style
Group:		Databases
Source0:	%{name}-%{version}.tar.bz2
Patch0:		kinterbasdb-3.3.0-link-m.patch
Patch1:		kinterbasdb-3.3.0-db-fix.patch
Group:		Development/Python
URL:		http://www.firebirdsql.org/
Requires:	python-egenix-mx-base
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
%patch1 -p0

%build
CFLAGS="%{optflags}" /usr/bin/python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%doc README PKG-INFO
%doc docs
%{py_platsitedir}/%{name}
%{py_platsitedir}/%{name}-%{version}-py*.egg-info


