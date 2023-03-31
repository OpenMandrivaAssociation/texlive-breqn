Name:		texlive-breqn
Version:	60881
Release:	2
Summary:	Automatic line breaking of displayed equations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/breqn
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breqn.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breqn.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/breqn.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides solutions to a number of common
difficulties in writing displayed equations and getting
high-quality output. For example, it is a well-known
inconvenience that if an equation must be broken into more than
one line, 'left...right' constructs cannot span lines. The
breqn package makes them work as one would expect whether or
not there is an intervening line break. The single most
ambitious goal of the package, however, is to support automatic
linebreaking of displayed equations. Such linebreaking cannot
be done without substantial changes under the hood in the way
formulae are processed; the code must be watched carefully,
keeping an eye on possible glitches. The bundle also contains
the flexisym and mathstyle packages, which are both designated
as support for breqn.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/breqn
%{_texmfdistdir}/tex/latex/breqn
%doc %{_texmfdistdir}/doc/latex/breqn

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
