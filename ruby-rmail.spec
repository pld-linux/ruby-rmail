%define	ruby_archdir	%(ruby -r rbconfig -e 'print Config::CONFIG["archdir"]')
%define ruby_rubylibdir %(ruby -r rbconfig -e 'print Config::CONFIG["rubylibdir"]')
Summary:	RubyMail mail library
Summary(pl):	RubyMail - biblioteka do obs�ugi poczty
Name:		ruby-RMail
Version:	0.17
Release:	2
License:	GPL
Group:		Development/Languages
%define tarname rubymail
Source0:	http://www.lickey.com/rubymail/download/%{tarname}-%{version}.tar.gz
# Source0-md5:	68ed70492541086b4bf17e8e75857e2e
Patch0:	ruby-RMail-newlines.patch
URL:		http://www.lickey.com/rubymail/
BuildRequires:	ruby
BuildRequires:	ruby-devel
Requires:	ruby
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mail handling module for Ruby.

%description -l pl
Modu� dla j�zyka Ruby obs�uguj�cy poczt�.

%prep
%setup -q -n %{tarname}-%{version}
%patch0 -p1

%build
ruby install.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}

rdoc -o rdoc/ --main README README NEWS NOTES TODO THANKS lib/* guide/* --title "%{name} %{version}" --inline-source

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{ruby_rubylibdir}

ruby install.rb install --prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc rdoc/*
%{ruby_rubylibdir}/rmail
%{ruby_rubylibdir}/rmail.rb
