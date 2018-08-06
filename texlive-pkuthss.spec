Name:		texlive-pkuthss
Version:	1.8.0
Release:	1
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
%{_texmfdistdir}/tex/latex/pkuthss
%doc %{_texmfdistdir}/doc/latex/pkuthss

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
