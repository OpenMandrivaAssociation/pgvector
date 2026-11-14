%define pg_ver %(if rpm -q postgresql-devel &>/dev/null; then rpm -q --qf '%%{version}' postgresql-devel; else echo -n 19.0; fi)
%define pg_major %(echo %{pg_ver} |cut -d. -f1)
%define pg_next_major %(echo $((%{pg_major}+1)))

Name:		pgvector
Version:	0.8.7
Release:	2
Source0:	https://github.com/pgvector/pgvector/archive/refs/tags/v%{version}.tar.gz
Summary:	Vector similarity search extension for PostgreSQL
URL:		https://github.com/pgvector/pgvector
License:	MIT
Group:		Servers
BuildRequires:	make
BuildRequires:	pkgconfig(libpq)
# While libpq API usually remains stable across major releases,
# the plugin ABI often doesn't -- let's make sure we rebuild
# when we update PostgreSQL.
Requires:	(postgresql-server >= %{pg_major} with postgresql-server < %{pg_next_major})

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
