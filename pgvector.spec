# Match postgresql modules: no LTO, allow unresolved server symbols
%define _disable_lto 1
%global _disable_ld_no_undefined 1

Name:		pgvector
Version:	0.8.7
Release:	1
Source0:	https://github.com/pgvector/pgvector/archive/refs/tags/v%{version}.tar.gz
Summary:	Vector similarity search extension for PostgreSQL
URL:		https://github.com/pgvector/pgvector
License:	MIT
Group:		Servers
BuildRequires:	make
BuildRequires:	pkgconfig(libpq)
Requires:	postgresql-server

%description
Vector similarity search extension for PostgreSQL

%package devel
Summary:	Development files for the PostgreSQL vector similarity search extension
Requires:	%{name} = %{EVRD}
Requires:	pkgconfig(libpq)

%description devel
Development files for the PostgreSQL vector similarity search extension

%prep
%autosetup -p1

%conf

%build
%make_build OPTFLAGS="%{optflags}"

%install
%make_install

%files
%{_libdir}/postgresql/vector.so
%{_libdir}/postgresql/bitcode/vector*
%{_datadir}/postgresql/extension/vector*.sql
%{_datadir}/postgresql/extension/vector.control

%files devel
%{_includedir}/postgresql/server/extension/vector
