Name:		replxx
Version:	0.0.4
Release:	1%{?dist}
Summary:	Readline and libedit replacement library

Group:		System Environment/Libraries
License:	BSD
URL:		https://github.com/AmokHuginnsson/replxx
Source0:	https://github.com/AmokHuginnsson/replxx/archive/refs/tags/%{name}-%{version}.tar.gz

BuildRequires:	cmake
BuildRequires:	gcc

%description
A small, portable GNU readline replacement for Linux, Windows and
MacOS which is capable of handling UTF-8 characters. Unlike GNU
readline, which is GPL, this library uses a BSD license and can be
used in any kind of program.

%package devel
Summary:        Development files for replxx
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for the replxx library.

%prep
%setup -q


%build
%cmake .
%make_build


%install
%make_install


%check
ctest -V %{?_smp_mflags}

%files
%license LICENSE.md
%{_libdir}/*.so
%{_libdir}/*.so.*

%files devel
%doc README.md
%{_includedir}/*.h
%{_includedir}/*.hxx
%{_datadir}/cmake/%{name}/*.cmake

%changelog

