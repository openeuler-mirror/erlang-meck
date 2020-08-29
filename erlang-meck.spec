%global realname meck
%global upstream eproxus
Name:		erlang-meck
Version:	0.8.13
Release:	1
BuildArch:	noarch
Summary:	A mocking library for Erlang
License:	ASL 2.0
URL:		https://github.com/eproxus/meck
Source0:	https://github.com/eproxus/meck/archive/%{version}/meck-%{version}.tar.gz
Patch1:		erlang-meck-0001-Workaround-for-Rebar-2.x.patch
BuildRequires:	erlang-hamcrest
BuildRequires:	erlang-rebar
%description
With meck you can easily mock modules in Erlang. Since meck is intended to be
used in testing, you can also perform some basic validations on the mocked
modules, such as making sure no function is called in a way it should not.

%prep
%autosetup -p1 -n meck-%{version}

%build
%{erlang_compile}

%install
%{erlang_install}

%check
%{erlang_test -C test.config}

%files
%license LICENSE
%doc README.md NOTICE
%{erlang_appdir}/

%changelog
* Sat Aug 29 2020 yaokai <yaokai13@huawei.com> - 0.8.13-1
- package init
