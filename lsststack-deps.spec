Summary:	LSST Stack core OS provided dependencies
Name:		lsststack-deps
Version:	1.0.1
Release:	1
License:	MIT/GPLv3+
Url:		https://github.com/lsst
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Requires:	bison
Requires:	blas
Requires:	bzip2
Requires:	bzip2-devel
Requires:	cmake
Requires:	curl
Requires:	flex
Requires:	fontconfig
Requires:	freetype-devel
Requires:	gcc-c++
Requires:	gcc-gfortran
Requires:	gettext
Requires:	git
Requires:	glib2-devel
Requires:	java-1.8.0-openjdk
Requires:	libcurl-devel
Requires:	libuuid-devel
Requires:	libXext
Requires:	libXrender
Requires:	libXt-devel
Requires:	make
Requires:	ncurses-devel
Requires:	openssl-devel
Requires:	patch
Requires:	perl
Requires:	perl-ExtUtils-MakeMaker
Requires:	readline-devel
Requires:	tar
Requires:	zlib-devel
%{?el5:Requires: devtoolset-3-gcc}
%{?el5:Requires: devtoolset-3-gcc-c++}


%description
Pulls in core OS provided packages required for building the LSST Stack as
documented at https://confluence.lsstcorp.org/display/LSWUG/Prerequisites.

# XXX an empty files section is required or the "meta" package will not be
# generated.
%files

%changelog
* Wed Jan 14 2015 Joshua Hoblitt <jhoblitt@cpan.org> 1.0.1-1
- new package built with tito

* Tue Jan 13 2015 jhoblitt@lsst.org
- first working version
