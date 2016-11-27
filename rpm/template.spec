Name:           ros-kinetic-pid
Version:        0.0.20
Release:        0%{?dist}
Summary:        ROS pid package

Group:          Development/Libraries
License:        BSD
URL:            http://wiki.ros.org/pid
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-kinetic-diagnostic-updater
Requires:       ros-kinetic-dynamic-reconfigure
Requires:       ros-kinetic-message-runtime
Requires:       ros-kinetic-roscpp
Requires:       ros-kinetic-std-msgs
BuildRequires:  ros-kinetic-catkin
BuildRequires:  ros-kinetic-diagnostic-updater
BuildRequires:  ros-kinetic-dynamic-reconfigure
BuildRequires:  ros-kinetic-message-generation
BuildRequires:  ros-kinetic-roscpp
BuildRequires:  ros-kinetic-std-msgs

%description
Launch a PID control node.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/kinetic" \
        -DCMAKE_PREFIX_PATH="/opt/ros/kinetic" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/kinetic/setup.sh" ]; then . "/opt/ros/kinetic/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/kinetic

%changelog
* Sun Nov 27 2016 Andy Zelenak <andyz@utexas.edu> - 0.0.20-0
- Autogenerated by Bloom

* Fri Oct 28 2016 Andy Zelenak <andyz@utexas.edu> - 0.0.19-0
- Autogenerated by Bloom

* Fri Oct 21 2016 Andy Zelenak <andyz@utexas.edu> - 0.0.18-0
- Autogenerated by Bloom

* Mon Aug 22 2016 Andy Zelenak <andyz@utexas.edu> - 0.0.17-0
- Autogenerated by Bloom

* Fri Aug 19 2016 Andy Zelenak <andyz@utexas.edu> - 0.0.16-0
- Autogenerated by Bloom

* Tue Jun 14 2016 Andy Zelenak <andyz@utexas.edu> - 0.0.15-0
- Autogenerated by Bloom

