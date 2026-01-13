#!/usr/bin/env bash
set -euo pipefail

REPO_URL="https://github.com/yves-chevallier/columen.git"
REF="${1:-main}"
DEST_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT="${DEST_DIR}/src/texsmith_template_exam/columen/columen.sty"

tmp_dir="$(mktemp -d)"
cleanup() {
  rm -rf "${tmp_dir}"
}
trap cleanup EXIT

git clone --depth 1 --branch "${REF}" "${REPO_URL}" "${tmp_dir}/columen"

pushd "${tmp_dir}/columen" >/dev/null
  tex columen.ins
  if [[ ! -f columen.sty ]]; then
    echo "columen.sty was not generated." >&2
    exit 1
  fi
popd >/dev/null

install -m 0644 "${tmp_dir}/columen/columen.sty" "${OUTPUT}"
echo "Wrote ${OUTPUT}"
