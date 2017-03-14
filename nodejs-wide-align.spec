%{?scl:%scl_package nodejs-wide-align}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

%global enable_tests 0
%global npm_name wide-align

Name:       %{?scl_prefix}nodejs-%{npm_name}
Version:    1.1.0
Release:    3%{?dist}
Summary:    A wide-character aware text alignment function for use on the console or with fixed width fonts
License:    ISC
URL:        https://github.com/iarna/wide-align
Source0:    http://registry.npmjs.org/%{npm_name}/-/%{npm_name}-%{version}.tgz
BuildRequires: %{?scl_prefix}nodejs-devel
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

%description
A wide-character aware text alignment function for use on the console or with fixed width fonts.

%prep
%setup -q -n package

rm -rf node_modules

%build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{npm_name}
cp -pfr align.js package.json %{buildroot}%{nodejs_sitelib}/%{npm_name}
# If any binaries are included, symlink them to bindir here


%nodejs_symlink_deps

%if 0%{?enable_tests}
%check
#not running tests in RHSCL
%endif

%files
%{nodejs_sitelib}/%{npm_name}

%doc LICENSE
%doc README.md

%changelog
* Wed Jan 18 2017 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-3
- Don't copy test dir

* Tue Sep 20 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 1.1.0-2
- Initial build

