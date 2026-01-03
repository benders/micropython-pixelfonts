#!/bin/bash -e

cmd="mpy-cross"
if ! command -v "$cmd" &> /dev/null; then
    echo "Error: Required utility '$cmd' not found in PATH or not executable"
    exit 1
fi

bytecode_version=$("$cmd" --version | sed 's/.*emitting mpy \(v[0-9]\).*/\1/')
echo "Using $cmd emitting bytecode $bytecode_version"

clean() {
    echo "Cleaning up .mpy and generated package-mpy files"
    find "$dir" -name \*.mpy -delete
    rm -vf package-mpy-*.json
}

compile() {
    local src_file="$1"
    local out_file="${src_file%.py}.mpy"
    echo "Compiling $src_file -> $out_file"
    "$cmd" -o "$out_file" "$src_file"
}

compile_all() {
    find "$dir" -name \*.py | while read -r file; do
        compile "$file"
    done
}

generate_package_mpy() {
    local package_json="package.json"
    if [ ! -f "$package_json" ]; then
        echo "Error: $package_json not found in current directory"
        exit 1
    fi
    local out_file="package-mpy-$bytecode_version.json"
    echo "Generating $out_file"
    sed  's/\.py/\.mpy/g' < "$package_json" > "$out_file"
}

dir="pixelfonts"
# set -x
clean
compile_all
generate_package_mpy