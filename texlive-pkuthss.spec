# revision 33464
# category Package
# catalog-ctan /macros/latex/contrib/pkuthss
# catalog-date 2014-04-16 20:04:38 +0200
# catalog-license other-free
# catalog-version 1.5.2
Name:		texlive-pkuthss
Version:	1.5.2
Release:	4
Summary:	LaTeX template for dissertations in Peking University
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pkuthss
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkuthss.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pkuthss.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides a simple, clear and flexible LaTeX
template for dissertations in Peking University.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/pkuthss/pkulogo.eps
%{_texmfdistdir}/tex/latex/pkuthss/pkulogo.pdf
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-extra.sty
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-gbk.def
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-utf8.def
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss.cls
%{_texmfdistdir}/tex/latex/pkuthss/pkuword.eps
%{_texmfdistdir}/tex/latex/pkuthss/pkuword.pdf
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/Make.bat
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/abstract.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/acknowledge.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/chap1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/copyright.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/encl1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/introduction.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/chap/originauth.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/thesis.bib
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-gbk/thesis.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/Make.bat
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/abstract.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/acknowledge.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/chap1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/copyright.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/encl1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/introduction.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/chap/originauth.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/thesis.bib
%doc %{_texmfdistdir}/doc/latex/pkuthss/example-utf8/thesis.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/example.pdf
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/ChangeLog-upto-1.3.txt
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/ChangeLog.txt
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/abstract.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/acknowledge.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/chap1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/chap2.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/chap3.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/copyright.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/encl1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/introduction.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/chap/originauth.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/pkuthss.bib
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme-src/pkuthss.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/readme.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
