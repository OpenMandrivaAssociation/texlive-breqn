%global tl_name breqn
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.98l
Release:	%{tl_revision}.1
Summary:	Automatic line breaking of displayed equations
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/breqn
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breqn.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breqn.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/breqn.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides solutions to a number of common difficulties in
writing displayed equations and getting high-quality output. For
example, it is a well-known inconvenience that if an equation must be
broken into more than one line, 'left...right' constructs cannot span
lines. The breqn package makes them work as one would expect whether or
not there is an intervening line break. The single most ambitious goal
of the package, however, is to support automatic linebreaking of
displayed equations. Such linebreaking cannot be done without
substantial changes under the hood in the way formulae are processed;
the code must be watched carefully, keeping an eye on possible glitches.
The bundle also contains the flexisym and mathstyle packages, which are
both designated as support for breqn.

