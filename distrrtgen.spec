Summary:	Distributed rainbow table generation client
Summary(pl):	Klient projektu rozproszonego generowaia tablic rainbow
Name:		distrrtgen
Version:	2.0
Release:	0.1
License:	As-is
Group:		Applications
Source0:	http://www.freerainbowtables.com/distrrtgen/client/%{name}-%{version}-src.zip
# Source0-md5:	f9c342cd4d822911352cfa066c5d1a42
URL:		http://www.freerainbowtables.com/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DistrRTgen is a Distributed Rainbow Table Generation client. The goal
was to enable community to contribute to the generation of Rainbow
Tables as much or as little as suited them, and without having to
create whole particular tables. Distributed computing makes this
possible.

%description -l pl
DistrRTgen to klient projektu Distributed rainbow Table Generation.
Celem jest u³atwienie spo³eczno¶ci sposóbów na wsparcie projektu
poprzez generowanie tablic rainbow w sposób im wygodny, bez potrzeby
tworzenia kompletnych tablic. Liczenie rozproszone sprawia, ¿e jest to
mo¿liwe.

%prep
%setup -q -c

%build
%{__make} \
	CXX="%{__cxx}" \
	CXXFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install %{name} $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc disclaimer.txt README.txt distrrtgen.conf charset.txt
%attr(755,root,root) %{_bindir}/*
