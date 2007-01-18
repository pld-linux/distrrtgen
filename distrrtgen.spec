Summary:	Distributed rainbow table generation client
Summary(pl):	Klient projektu rozproszonego generowania tablic rainbow
Name:		distrrtgen
Version:	2.1
Release:	0.1
License:	As-is
Group:		Applications
Source0:	http://www.freerainbowtables.com/distrrtgen/client/%{name}-%{version}-src.zip
# Source0-md5:	f1320b2569200d5377af205cbdd9773f
Patch0:		%{name}-Makefile.patch
URL:		http://www.freerainbowtables.com/
BuildRequires:	libstdc++-devel
BuildRequires:	openssl-devel
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DistrRTgen is a Distributed Rainbow Table Generation client. The goal
was to enable community to contribute to the generation of Rainbow
Tables as much or as little as suited them, and without having to
create whole particular tables. Distributed computing makes this
possible.

%description -l pl
DistrRTgen to klient projektu Distributed Rainbow Table Generation.
Celem jest u³atwienie spo³eczno¶ci sposobów na wsparcie projektu
poprzez generowanie tablic rainbow w sposób im wygodny, bez potrzeby
tworzenia kompletnych tablic. Liczenie rozproszone sprawia, ¿e jest to
mo¿liwe.

%prep
%setup -q -c
%patch0 -p1

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
