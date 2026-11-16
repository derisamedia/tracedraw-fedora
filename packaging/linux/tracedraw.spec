%global debug_package %{nil}
%global _build_id_links none

Name:           tracedraw
Version:        %{_tracedraw_version}
Release:        %{_tracedraw_release}%{?dist}
Summary:        Open-source vector illustration editor
License:        MIT OR Apache-2.0
URL:            https://github.com/tracedraw/tracedraw

Recommends:     gtk3
Recommends:     libX11
Recommends:     libXcursor
Recommends:     libXi
Recommends:     libXrandr
Recommends:     libwayland-client
Recommends:     libxkbcommon
Recommends:     libxkbcommon-x11
Recommends:     mesa-libGL
Recommends:     vulkan-loader

%description
Open-source vector illustration editor with a classic desktop workflow and a .cdr reader.

%install
install -D -m 0755 "%{_sourcedir}/tracedraw" "%{buildroot}%{_bindir}/tracedraw"
install -D -m 0755 "%{_sourcedir}/tracedraw-cli" "%{buildroot}%{_bindir}/tracedraw-cli"
install -D -m 0644 "%{_sourcedir}/tracedraw.desktop" "%{buildroot}%{_datadir}/applications/tracedraw.desktop"
install -D -m 0644 "%{_sourcedir}/tracedraw-mime.xml" "%{buildroot}%{_datadir}/mime/packages/tracedraw.xml"
install -D -m 0644 "%{_sourcedir}/tracedraw.thumbnailer" "%{buildroot}%{_datadir}/thumbnailers/tracedraw.thumbnailer"
install -D -m 0644 "%{_sourcedir}/tracedraw-256.png" "%{buildroot}%{_datadir}/icons/hicolor/256x256/apps/tracedraw.png"
install -D -m 0644 "%{_sourcedir}/README.md" "%{buildroot}%{_docdir}/tracedraw/README"
install -D -m 0644 "%{_sourcedir}/LICENSE-MIT" "%{buildroot}%{_licensedir}/tracedraw/LICENSE-MIT"
install -D -m 0644 "%{_sourcedir}/LICENSE-APACHE" "%{buildroot}%{_licensedir}/tracedraw/LICENSE-APACHE"

%files
%{_bindir}/tracedraw
%{_bindir}/tracedraw-cli
%{_datadir}/applications/tracedraw.desktop
%{_datadir}/mime/packages/tracedraw.xml
%{_datadir}/thumbnailers/tracedraw.thumbnailer
%{_datadir}/icons/hicolor/256x256/apps/tracedraw.png
%{_docdir}/tracedraw/README
%license %{_licensedir}/tracedraw/LICENSE-MIT
%license %{_licensedir}/tracedraw/LICENSE-APACHE
