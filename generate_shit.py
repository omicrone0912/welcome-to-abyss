import os

languages = [
    ("Python", "py", "print('hello')"),
    ("JavaScript", "js", "console.log('hello');"),
    ("TypeScript", "ts", "const x: string = 'hello'; console.log(x);"),
    ("Java", "java", "class Main { public static void main(String[] args) { System.out.println(\"hello\"); } }"),
    ("C", "c", "#include <stdio.h>\nint main() { printf(\"hello\\n\"); return 0; }"),
    ("C++", "cpp", "#include <iostream>\nint main() { std::cout << \"hello\" << std::endl; return 0; }"),
    ("C#", "cs", "using System;\nclass Program { static void Main() { Console.WriteLine(\"hello\"); } }"),
    ("Ruby", "rb", "puts 'hello'"),
    ("PHP", "php", "<?php echo 'hello'; ?>"),
    ("Go", "go", "package main\nimport \"fmt\"\nfunc main() { fmt.Println(\"hello\") }"),
    ("Rust", "rs", "fn main() { println!(\"hello\"); }"),
    ("Swift", "swift", "print(\"hello\")"),
    ("Kotlin", "kt", "fun main() { println(\"hello\") }"),
    ("Scala", "scala", "object Main extends App { println(\"hello\") }"),
    ("R", "r", "print(\"hello\")"),
    ("Julia", "jl", "println(\"hello\")"),
    ("Dart", "dart", "void main() { print('hello'); }"),
    ("Lua", "lua", "print('hello')"),
    ("Haskell", "hs", "main = putStrLn \"hello\""),
    ("Clojure", "clj", "(println \"hello\")"),
    ("Elixir", "exs", "IO.puts \"hello\""),
    ("Erlang", "erl", "-module(hello).\n-export([hello_world/0]).\nhello_world() -> io:fwrite(\"hello\\n\")."),
    ("F#", "fs", "printfn \"hello\""),
    ("OCaml", "ml", "print_endline \"hello\""),
    ("Shell", "sh", "echo 'hello'"),
    ("PowerShell", "ps1", "Write-Host 'hello'"),
    ("Batch", "bat", "@echo off\necho hello"),
    ("SQL", "sql", "SELECT 'hello';"),
    ("HTML", "html", "<html><body>hello</body></html>"),
    ("CSS", "css", "body { content: 'hello'; }"),
    ("XML", "xml", "<?xml version=\"1.0\"?><hello>world</hello>"),
    ("JSON", "json", "{\"hello\": \"world\"}"),
    ("YAML", "yml", "hello: world"),
    ("TOML", "toml", "hello = \"world\""),
    ("Markdown", "md", "# hello"),
    ("Assembly", "asm", "section .data\nmsg db 'hello',0"),
    ("Lisp", "lisp", "(print \"hello\")"),
    ("Scheme", "scm", "(display \"hello\") (newline)"),
    ("Prolog", "pro", "main :- write('hello'), nl."),
    ("Ada", "adb", "with Ada.Text_IO; use Ada.Text_IO;\nprocedure Hello is begin Put_Line(\"hello\"); end Hello;"),
    ("Fortran", "f90", "program hello\nprint *, 'hello'\nend program hello"),
    ("COBOL", "cob", "IDENTIFICATION DIVISION.\nPROGRAM-ID. HELLO.\nPROCEDURE DIVISION.\nDISPLAY 'hello'.\nSTOP RUN."),
    ("Pascal", "pas", "program Hello; begin writeln('hello'); end."),
    ("Visual Basic", "vb", "Module Hello\nSub Main()\nConsole.WriteLine(\"hello\")\nEnd Sub\nEnd Module"),
    ("VBScript", "vbs", "WScript.Echo \"hello\""),
    ("ActionScript", "as", "trace(\"hello\");"),
    ("CoffeeScript", "coffee", "console.log 'hello'"),
    ("Elm", "elm", "import Html exposing (text)\nmain = text \"hello\""),
    ("PureScript", "purs", "module Main where\nimport Prelude\nimport Effect.Console (log)\nmain = log \"hello\""),
    ("Reason", "re", "print_endline(\"hello\");"),
    ("Nim", "nim", "echo \"hello\""),
    ("Crystal", "cr", "puts \"hello\""),
    ("Zig", "zig", "const std = @import(\"std\");\npub fn main() void { std.debug.print(\"hello\\n\", .{}); }"),
    ("V", "v", "fn main() { println('hello') }"),
    ("D", "d", "import std.stdio;\nvoid main() { writeln(\"hello\"); }"),
    ("AWK", "awk", "BEGIN { print \"hello\" }"),
    ("Tcl", "tcl", "puts \"hello\""),
    ("Groovy", "groovy", "println 'hello'"),
    ("Perl", "pl", "print \"hello\\n\";"),
    ("Objective-C", "m", "#import <Foundation/Foundation.h>\nint main() { NSLog(@\"hello\"); return 0; }"),
    ("Brainfuck", "bf", "++++++++[>++++[>++>+++>+++>+<<<<-]>+>+>->>+[<]<-]>>.>---.+++++++..+++.>>.<-.<.+++.------.--------.>>+.>++."),
    ("Solidity", "sol", "pragma solidity ^0.8.0;\ncontract Hello { function hello() public pure returns (string memory) { return \"hello\"; } }")
]

base_dir = r"c:\Users\omicrone\Documents\Antigravity\abyss\welcome-to-abyss"

for i, (lang_name, ext, code) in enumerate(languages, 1):
    dir_name = f"うんこ第{i}版"
    dir_path = os.path.join(base_dir, dir_name)
    os.makedirs(dir_path, exist_ok=True)
    file_path = os.path.join(dir_path, f"main.{ext}")
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(code)

print("done")
