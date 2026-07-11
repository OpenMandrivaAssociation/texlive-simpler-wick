%global tl_name simpler-wick
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0.0
Release:	%{tl_revision}.1
Summary:	Simpler Wick contractions
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/simpler-wick
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpler-wick.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simpler-wick.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
In every quantum field theory course, there will be a chapter about
Wick's theorem and how it can be used to convert a very large product of
many creation and annihilation operators into something more tractable
and normal ordered. The contractions are denoted with a square bracket
over the operators which are being contracted, which used to be rather
annoying to typeset in LaTeX as the only other package available was
simplewick, which is rather unwieldy. This package provides a simpler
syntax for Wick contractions.

