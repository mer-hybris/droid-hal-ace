# These and other macros are documented in dhd/droid-hal-device.inc

%define device ace
%define vendor htc

%define vendor_pretty HTC
%define device_pretty Desire HD

%define local_hadk_build_project   1

%define installable_zip 1
#define enable_kernel_update 0

# Entries migrated from the old rpm/droid-hal-ace.spec
%define straggler_files \
/selinux_version \
/service_contexts
%{nil}

%include rpm/dhd/droid-hal-device.inc
