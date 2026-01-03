#!/bin/bash -e

DIR="pixelfonts"
CROSS="mpy-cross"


if ! command -v "$CROSS" &> /dev/null; then
    echo "Error: Required utility '$CROSS' not found in PATH or not executable"
    exit 1
fi

bytecode_version=$("$CROSS" --version | sed 's/.*emitting mpy \(v[0-9]\).*/\1/')
echo "Using $CROSS emitting bytecode $bytecode_version"

clean() {
    echo "Cleaning up .mpy, .pyc and generated package-mpy files"
    find "$DIR" -name \*.mpy -delete
    find "$DIR" -name \*.pyc -delete
    rm -vf package-mpy-*.json
}

compile() {
    local src_file="$1"
    local out_file="${src_file%.py}.mpy"
    echo "Compiling $src_file -> $out_file"
    "$CROSS" -o "$out_file" "$src_file"
}

compile_all() {
    find "$DIR" -name \*.py | while read -r file; do
        compile "$file"
    done
}

package_mpy() {
    local package_json="package.json"
    if [ ! -f "$package_json" ]; then
        echo "Error: $package_json not found in current directory"
        exit 1
    fi
    local out_file="package-mpy-$bytecode_version.json"
    echo "Generating $out_file"
    sed  's/\.py/\.mpy/g' < "$package_json" > "$out_file"
}

all() {
    # set -x
    clean
    compile_all
    package_mpy
}

usage() {
    echo "Usage: $0 [action]"
    echo ""
    echo "Actions:"
    echo "  all          - Clean, compile all files, and generate package (default)"
    echo "  clean        - Remove .mpy files and package-mpy-*.json files"
    echo "  compile_all  - Compile all .py files to .mpy"
    echo "  package_mpy  - Generate package-mpy-*.json from package.json"
    echo ""
}

# Parse command line arguments
ACTION="${1:-all}"

case "$ACTION" in
    clean|compile_all|package_mpy|all)
        "$ACTION"
        ;;
    help|--help|-h)
        usage
        ;;
    *)
        echo "Error: Unknown action '$ACTION'"
        echo ""
        usage
        exit 1
        ;;
esac