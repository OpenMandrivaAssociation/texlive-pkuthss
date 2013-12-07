# revision 29797
# category Package
# catalog-ctan /macros/latex/contrib/pkuthss
# catalog-date 2013-04-08 10:17:07 +0200
# catalog-license other-free
# catalog-version 1.4rc3
Name:		texlive-pkuthss
Version:	1.4rc3
Release:	2
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
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-extra.sty
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-gbk.def
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss-utf8.def
%{_texmfdistdir}/tex/latex/pkuthss/pkuthss.cls
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/ChangeLog-upto-1.3.txt
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/ChangeLog.txt
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/Make.bat
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/abstract.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/acknowledge.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/chap1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/chap2.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/chap3.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/copyright.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/encl1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/encl2.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/introduction.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/chap/originauth.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/img/Make.bat
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/img/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/img/pkulogo.eps
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/img/pkuword.eps
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/pkuthss.bib
%doc %{_texmfdistdir}/doc/latex/pkuthss/gbkcrlf/pkuthss.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/pkuthss.pdf
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/ChangeLog-upto-1.3.txt
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/ChangeLog.txt
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/Make.bat
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/abstract.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/acknowledge.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/chap1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/chap2.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/chap3.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/conclusion.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/copyright.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/encl1.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/encl2.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/introduction.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/chap/originauth.tex
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/img/Make.bat
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/img/Makefile
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/img/pkulogo.eps
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/img/pkuword.eps
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/pkuthss.bib
%doc %{_texmfdistdir}/doc/latex/pkuthss/utf8lf/pkuthss.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
