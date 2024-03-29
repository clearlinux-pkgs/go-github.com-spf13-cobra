#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : go-github.com-spf13-cobra
Version  : v0.0.3
Release  : 2
URL      : https://proxy.golang.org/github.com/spf13/cobra/@v/list
Source0  : https://proxy.golang.org/github.com/spf13/cobra/@v/list
Source1  : https://proxy.golang.org/github.com/spf13/cobra/@v/v0.0.3.info
Source2  : https://proxy.golang.org/github.com/spf13/cobra/@v/v0.0.3.mod
Source3  : https://proxy.golang.org/github.com/spf13/cobra/@v/v0.0.3.zip
Summary  : No detailed summary available
Group    : Development/Tools
License  : AGPL-3.0 Apache-2.0 BSD-3-Clause-Clear GPL-2.0 GPL-3.0 LGPL-3.0 MIT
Requires: go-github.com-spf13-cobra-data = %{version}-%{release}
BuildRequires : buildreq-golang

%description
![cobra logo](https://cloud.githubusercontent.com/assets/173412/10886352/ad566232-814f-11e5-9cd0-aa101788c117.png)

%package data
Summary: data components for the go-github.com-spf13-cobra package.
Group: Data

%description data
data components for the go-github.com-spf13-cobra package.


%prep

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/usr/share/goproxy/github.com/spf13/cobra/@v
# Create list file using packaged versions
echo v0.0.3 >> %{buildroot}/usr/share/goproxy/github.com/spf13/cobra/@v/list
install -m 0644 %{SOURCE1} %{buildroot}/usr/share/goproxy/github.com/spf13/cobra/@v/v0.0.3.info
install -m 0644 %{SOURCE2} %{buildroot}/usr/share/goproxy/github.com/spf13/cobra/@v/v0.0.3.mod
install -m 0644 %{SOURCE3} %{buildroot}/usr/share/goproxy/github.com/spf13/cobra/@v/v0.0.3.zip


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/goproxy/github.com/spf13/cobra/@v/list
/usr/share/goproxy/github.com/spf13/cobra/@v/v0.0.3.info
/usr/share/goproxy/github.com/spf13/cobra/@v/v0.0.3.mod
/usr/share/goproxy/github.com/spf13/cobra/@v/v0.0.3.zip
