import os
import re

import requests

GITHUB_TOKEN = os.environ["GITHUB_TOKEN"]
USERNAME = "Lemn4t"

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

BADGES = {
    "C": "https://img.shields.io/badge/C-555555?style=for-the-badge&logo=c&logoColor=white&labelColor=111111",
    "C++": "https://img.shields.io/badge/C++-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white&labelColor=111111",
    "Rust": "https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white&labelColor=111111",
    "Assembly": "https://img.shields.io/badge/Assembly-525252?style=for-the-badge&logo=assemblyscript&logoColor=white&labelColor=111111",
    "Zig": "https://img.shields.io/badge/Zig-F7A41D?style=for-the-badge&logo=zig&logoColor=white&labelColor=111111",
    "Nim": "https://img.shields.io/badge/Nim-FFE953?style=for-the-badge&logo=nim&logoColor=black&labelColor=111111",
    "D": "https://img.shields.io/badge/D-B03931?style=for-the-badge&logo=d&logoColor=white&labelColor=111111",
    "Python": "https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=111111",
    "Ruby": "https://img.shields.io/badge/Ruby-CC342D?style=for-the-badge&logo=ruby&logoColor=white&labelColor=111111",
    "Perl": "https://img.shields.io/badge/Perl-39457E?style=for-the-badge&logo=perl&logoColor=white&labelColor=111111",
    "Lua": "https://img.shields.io/badge/Lua-2C2D72?style=for-the-badge&logo=lua&logoColor=white&labelColor=111111",
    "PHP": "https://img.shields.io/badge/PHP-777BB4?style=for-the-badge&logo=php&logoColor=white&labelColor=111111",
    "Java": "https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white&labelColor=111111",
    "Kotlin": "https://img.shields.io/badge/Kotlin-7F52FF?style=for-the-badge&logo=kotlin&logoColor=white&labelColor=111111",
    "Scala": "https://img.shields.io/badge/Scala-DC322F?style=for-the-badge&logo=scala&logoColor=white&labelColor=111111",
    "Groovy": "https://img.shields.io/badge/Groovy-4298B8?style=for-the-badge&logo=apachegroovy&logoColor=white&labelColor=111111",
    "Clojure": "https://img.shields.io/badge/Clojure-5881D8?style=for-the-badge&logo=clojure&logoColor=white&labelColor=111111",
    "C#": "https://img.shields.io/badge/C%23-512BD4?style=for-the-badge&logo=csharp&logoColor=white&labelColor=111111",
    "F#": "https://img.shields.io/badge/F%23-378BBA?style=for-the-badge&logo=fsharp&logoColor=white&labelColor=111111",
    "Visual Basic .NET": "https://img.shields.io/badge/VB.NET-512BD4?style=for-the-badge&logo=dotnet&logoColor=white&labelColor=111111",
    "JavaScript": "https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black&labelColor=111111",
    "TypeScript": "https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white&labelColor=111111",
    "CoffeeScript": "https://img.shields.io/badge/CoffeeScript-2F2625?style=for-the-badge&logo=coffeescript&logoColor=white&labelColor=111111",
    "HTML": "https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white&labelColor=111111",
    "CSS": "https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white&labelColor=111111",
    "SCSS": "https://img.shields.io/badge/SCSS-CC6699?style=for-the-badge&logo=sass&logoColor=white&labelColor=111111",
    "Sass": "https://img.shields.io/badge/Sass-CC6699?style=for-the-badge&logo=sass&logoColor=white&labelColor=111111",
    "Less": "https://img.shields.io/badge/Less-1D365D?style=for-the-badge&logo=less&logoColor=white&labelColor=111111",
    "Go": "https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white&labelColor=111111",
    "Swift": "https://img.shields.io/badge/Swift-F05138?style=for-the-badge&logo=swift&logoColor=white&labelColor=111111",
    "Objective-C": "https://img.shields.io/badge/Objective--C-7A7A7A?style=for-the-badge&logo=apple&logoColor=white&labelColor=111111",
    "Objective-C++": "https://img.shields.io/badge/Obj--C++-7A7A7A?style=for-the-badge&logo=apple&logoColor=white&labelColor=111111",
    "Dart": "https://img.shields.io/badge/Dart-0175C2?style=for-the-badge&logo=dart&logoColor=white&labelColor=111111",
    "Haskell": "https://img.shields.io/badge/Haskell-5D4F85?style=for-the-badge&logo=haskell&logoColor=white&labelColor=111111",
    "Elixir": "https://img.shields.io/badge/Elixir-4B275F?style=for-the-badge&logo=elixir&logoColor=white&labelColor=111111",
    "Erlang": "https://img.shields.io/badge/Erlang-A90533?style=for-the-badge&logo=erlang&logoColor=white&labelColor=111111",
    "OCaml": "https://img.shields.io/badge/OCaml-EC6813?style=for-the-badge&logo=ocaml&logoColor=white&labelColor=111111",
    "Elm": "https://img.shields.io/badge/Elm-60B5CC?style=for-the-badge&logo=elm&logoColor=white&labelColor=111111",
    "Reason": "https://img.shields.io/badge/Reason-DD4B39?style=for-the-badge&logo=reason&logoColor=white&labelColor=111111",
    "R": "https://img.shields.io/badge/R-276DC3?style=for-the-badge&logo=r&logoColor=white&labelColor=111111",
    "Julia": "https://img.shields.io/badge/Julia-9558B2?style=for-the-badge&logo=julia&logoColor=white&labelColor=111111",
    "MATLAB": "https://img.shields.io/badge/MATLAB-0076A8?style=for-the-badge&logo=mathworks&logoColor=white&labelColor=111111",
    "Jupyter Notebook": "https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white&labelColor=111111",
    "Shell": "https://img.shields.io/badge/Shell-4EAA25?style=for-the-badge&logo=gnu-bash&logoColor=white&labelColor=111111",
    "PowerShell": "https://img.shields.io/badge/PowerShell-5391FE?style=for-the-badge&logo=powershell&logoColor=white&labelColor=111111",
    "Batchfile": "https://img.shields.io/badge/Batch-4D4D4D?style=for-the-badge&logo=windows&logoColor=white&labelColor=111111",
    "CMake": "https://img.shields.io/badge/CMake-064F8C?style=for-the-badge&logo=cmake&logoColor=white&labelColor=111111",
    "Makefile": "https://img.shields.io/badge/Make-6D00CC?style=for-the-badge&logo=cmake&logoColor=white&labelColor=111111",
    "Dockerfile": "https://img.shields.io/badge/Dockerfile-2496ED?style=for-the-badge&logo=docker&logoColor=white&labelColor=111111",
    "Nix": "https://img.shields.io/badge/Nix-5277C3?style=for-the-badge&logo=nixos&logoColor=white&labelColor=111111",
    "Solidity": "https://img.shields.io/badge/Solidity-363636?style=for-the-badge&logo=solidity&logoColor=white&labelColor=111111",
    "V": "https://img.shields.io/badge/V-4F87C5?style=for-the-badge&logo=v&logoColor=white&labelColor=111111",
    "Vala": "https://img.shields.io/badge/Vala-7239B3?style=for-the-badge&logo=vala&logoColor=white&labelColor=111111",
    "Crystal": "https://img.shields.io/badge/Crystal-000000?style=for-the-badge&logo=crystal&logoColor=white&labelColor=111111",
    "Tcl": "https://img.shields.io/badge/Tcl-E4842B?style=for-the-badge&logo=tcl&logoColor=white&labelColor=111111",
    "Raku": "https://img.shields.io/badge/Raku-000000?style=for-the-badge&logo=raku&logoColor=white&labelColor=111111",
    "Haxe": "https://img.shields.io/badge/Haxe-EA8220?style=for-the-badge&logo=haxe&logoColor=white&labelColor=111111",
    "QML": "https://img.shields.io/badge/QML-44CD51?style=for-the-badge&logo=qt&logoColor=white&labelColor=111111",
    "GLSL": "https://img.shields.io/badge/GLSL-5586A4?style=for-the-badge&logo=opengl&logoColor=white&labelColor=111111",
    "HLSL": "https://img.shields.io/badge/HLSL-7F7F7F?style=for-the-badge&logo=microsoft&logoColor=white&labelColor=111111",
    "ShaderLab": "https://img.shields.io/badge/ShaderLab-222C37?style=for-the-badge&logo=unity&logoColor=white&labelColor=111111",
    "GDScript": "https://img.shields.io/badge/GDScript-478CBF?style=for-the-badge&logo=godotengine&logoColor=white&labelColor=111111",
    "Verilog": "https://img.shields.io/badge/Verilog-AC2B4B?style=for-the-badge&logo=xilinx&logoColor=white&labelColor=111111",
    "VHDL": "https://img.shields.io/badge/VHDL-543978?style=for-the-badge&logo=amd&logoColor=white&labelColor=111111",
    "SystemVerilog": "https://img.shields.io/badge/SystemVerilog-AC2B4B?style=for-the-badge&logo=xilinx&logoColor=white&labelColor=111111",
    "Cython": "https://img.shields.io/badge/Cython-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=111111",
}


def get_languages():
    languages = set()
    page = 1

    while True:
        url = f"https://api.github.com/users/{USERNAME}/repos?per_page=100&page={page}"
        resp = requests.get(url, headers=headers)
        repos = resp.json()

        if not repos:
            break

        for repo in repos:
            # Пропускаем форки
            if repo.get("fork", False):
                continue

            lang = repo.get("language")
            if lang:
                languages.add(lang)

        page += 1

    return sorted(languages)


def update_readme(languages):
    with open("README.md", "r") as f:
        readme = f.read()

    badges_html = '<p align="center">\n'
    for lang in languages:
        if lang in BADGES:
            badges_html += f'  <img src="{BADGES[lang]}" />\n'
        else:
            badges_html += f'  <img src="https://img.shields.io/badge/{lang}-333333?style=for-the-badge&logo={lang.lower()}&logoColor=white&labelColor=111111" />\n'
    badges_html += "</p>"

    pattern = r"<!-- START_LANGUAGES -->.*?<!-- END_LANGUAGES -->"
    replacement = f"<!-- START_LANGUAGES -->\n{badges_html}\n<!-- END_LANGUAGES -->"

    updated_readme = re.sub(pattern, replacement, readme, flags=re.DOTALL)

    with open("README.md", "w") as f:
        f.write(updated_readme)

    print(f"Updated languages: {', '.join(languages)}")


if __name__ == "__main__":
    languages = get_languages()
    update_readme(languages)
