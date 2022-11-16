Name:		texlive-simpler-wick
Version:	39074
Release:	1
Summary:	Simpler Wick contractions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simpler-wick
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpler-wick.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simpler-wick.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
In every quantum field theory course, there will be a chapter
about Wick's theorem and how it can be used to convert a very
large product of many creation and annihilation operators into
something more tractable and normal ordered. The contractions
are denoted with a square bracket over the operators which are
being contracted, which used to be rather annoying to typeset
in LaTeX as the only other package available was simplewick,
which is rather unwieldy. This package provides a simpler
syntax for Wick contractions.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/simpler-wick
%doc %{_texmfdistdir}/doc/latex/simpler-wick

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
