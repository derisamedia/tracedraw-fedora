#!/usr/bin/env bash
# Build a Fedora RPM package. Usage: build-rpm.sh <version> <release-dir> [x86_64|aarch64]
set -euo pipefail
RAW_VERSION="$1"
BIN="$(cd "$2" && pwd)"
ARCH="${3:-x86_64}"

case "$ARCH" in
  arm64|aarch64) RPM_ARCH=aarch64 ;;
  *) RPM_ARCH=x86_64 ;;
esac

# RPM Version cannot contain '-'; pre-release suffixes go into Release.
if [[ "$RAW_VERSION" == *-* ]]; then
  RPM_VERSION="${RAW_VERSION%%-*}"
  SUFFIX="${RAW_VERSION#*-}"
  SUFFIX="${SUFFIX//-/.}"
  RPM_RELEASE="0.1.${SUFFIX}"
else
  RPM_VERSION="$RAW_VERSION"
  RPM_RELEASE="1"
fi

ROOT="$(cd "$(dirname "$0")/../.." && pwd)"
TOPDIR="$ROOT/dist/rpmbuild"
rm -rf "$TOPDIR"
mkdir -p "$TOPDIR/BUILD" "$TOPDIR/RPMS" "$TOPDIR/SOURCES" "$TOPDIR/SPECS" "$TOPDIR/SRPMS" "$ROOT/dist"

cp "$BIN/tracedraw" "$BIN/tracedraw-cli" "$TOPDIR/SOURCES/"
cp "$ROOT/packaging/linux/tracedraw.desktop" "$TOPDIR/SOURCES/"
cp "$ROOT/packaging/linux/tracedraw-mime.xml" "$TOPDIR/SOURCES/"
cp "$ROOT/packaging/linux/tracedraw.thumbnailer" "$TOPDIR/SOURCES/"
cp "$ROOT/assets/icon/tracedraw-256.png" "$TOPDIR/SOURCES/"
cp "$ROOT/README.md" "$ROOT/LICENSE-MIT" "$ROOT/LICENSE-APACHE" "$TOPDIR/SOURCES/"
cp "$ROOT/packaging/linux/tracedraw.spec" "$TOPDIR/SPECS/"

rpmbuild -bb \
  --target "$RPM_ARCH" \
  --define "_topdir $TOPDIR" \
  --define "_tracedraw_version $RPM_VERSION" \
  --define "_tracedraw_release $RPM_RELEASE" \
  "$TOPDIR/SPECS/tracedraw.spec"

cp "$TOPDIR"/RPMS/"$RPM_ARCH"/tracedraw-*.rpm "$ROOT/dist/"
rm -rf "$TOPDIR"
