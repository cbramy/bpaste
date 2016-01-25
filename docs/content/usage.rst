Overview
========

The bpaste tool has two main commands `upload` and `list`, their purpose and
use is described in the below sections.::

  usage: bpaste [-h] [-v] {upload,list} ...

  optional arguments:
    -h, --help     show this help message and exit
    -v, --version  displays the version of this program

  subcommands:
    {upload,list}
      upload       upload the provided file's content to http://www.bpaste.net
      list         displays the list of supported languages

Submitting code snippet
=======================

The main command of the bpaste tool is `upload` and it allows you to submit
a code file to the bpaste.net website, defining if necessary the language for
syntax highlighting and the expiry duration for the snippet.

Once the upload has been completed successfully the URL to the new code snippet
is directly copied into the user's clipboard and is really for use.::

  usage: bpaste upload [-h] [-l LANG] [-e EXPIRE] file

  positional arguments:
    file                  full path to the file to be bpasted

  optional arguments:
    -h, --help            show this help message and exit
    -l LANG, --lang LANG  language of the code to be bpasted (default: python3)
    -e EXPIRE, --expire EXPIRE
                          expiry period for the code snippet (default: 1 day)

As detailed in the tool's help, the upload command takes one mandatory parameter
and two optional one, as described below:

* **file**: is the file of code (or not) that you want to upload as code snippet
  to the bpaste.net website. This parameter is mandatory as it is the content
  for the code snippet, it would not make any sense to not submit any code.
* *-l*, *--lang*: by default the chosen language for the snippet is defined to
  `python3`, however you can upload any support language, in which case you can
  use this parameter to chose another language. Check the `list` command details
  below to find the list of supported languages.
* *-e*, *--expire*: by default the code snippet lifetime (the amount of time
  after which it will be removed from the website) is set to *one day*. You can
  change it using the *-e* parameter and an adequate duration option as listed
  below:
  * *1day*
  * *1week*
  * *1month*
  * *never*

*Note. Please note that bpaste.net does not provide any way to remove the code
snippet you have submitted, and only an email to the owner can possibly end
up removing the submitted code snippet.*

Examples:

Upload the mycode.py file with the default expiry duration (one day) and the
default language (Python 3):::

  bpaste upload mycode.py

Upload the mycode.py file with default language (Python 3) and an expiry
duration of one week:::

  bpaste upload mycode.py -e 1week
  bpaste upload mycode.py --expire 1week

Upload the mycode.java file with the default expiry duration (one day) and
the language syntax highligting set to the Java language:::

  bpaste upload mycode.java -l java
  bpaste upload mycode.java --lang java

Upload the mycode.pl file so that it never expires (the code snippet will not be
removed from the website!) and choose the Perl highlighting syntax:::

  bpaste upload mycode.pl -e never -l perl
  bpaste upload mycode.pl --expire never -l perl
  bpaste upload mycode.pl -e never --lang perl
  bpaste upload mycode.pl --expire never --lang perl

Listing supported languages
===========================

The `list` command print out the list of all languages supported for syntax
highlight on the bpaste.net website. The `list` command does not have any
useful options as of now:::

  usage: bpaste list [-h]

  optional arguments:
    -h, --help  show this help message and exit


For your reference the list of supported languages at this point of time is
displayed below:

========================= ========================= ========================= ========================= =========================
abap                      antlr                     antlr-as                  antlr-csharp              antlr-cpp
antlr-java                antlr-objc                antlr-perl                antlr-python              antlr-ruby
apl                       as                        as3                       ada                       agda
alloy                     at                        apacheconf                applescript               aspectj
asy                       autoit                    awk                       bbcode                    bugs
basemake                  bash                      console                   bat                       befunge
blitzbasic                blitzmax                  boo                       brainfuck                 bro
c                         csharp                    cpp                       cbmbas                    cfengine3
cmake                     cobol                     cobolfree                 css                       css+django
css+genshitext            css+lasso                 css+mako                  css+myghty                css+php
css+erb                   css+smarty                css+mozpreproc            cuda                      ceylon
chai                      chapel                    cheetah                   cirru                     clay
clojure                   clojurescript             coffee-script             cfc                       cfm
common-lisp               coq                       croc                      cryptol                   cypher
cython                    d                         dtd                       dpatch                    dart
control                   sourceslist               delphi                    diff                      django
docker                    duel                      dylan                     dylan-console             dylan-lid
ebnf                      ecl                       erb                       eiffel                    elixir
iex                       ragel-em                  erlang                    erl                       evoque
fsharp                    factor                    fancy                     fan                       felix
fortran                   foxpro                    gap                       gas                       glsl
genshi                    genshitext                pot                       cucumber                  gnuplot
go                        golo                      gooddata-cl               gosu                      gst
groff                     groovy                    html                      html+cheetah              html+django
html+evoque               html+genshi               html+handlebars           html+lasso                html+mako
html+myghty               html+php                  html+smarty               html+twig                 html+velocity
http                      haml                      handlebars                haskell                   hx
haxeml                    hylang                    hybris                    idl                       ini
irc                       idris                     igor                      inform6                   i6t
inform7                   io                        ioke                      isabelle                  jags
json                      jsonld                    jade                      jasmin                    java
jsp                       js                        js+cheetah                js+django                 js+genshitext
js+lasso                  js+mako                   js+myghty                 js+php                    js+erb
js+smarty                 javascript+mozpreproc     julia                     jlcon                     kal
kconfig                   koka                      kotlin                    llvm                      lsl
lasso                     lean                      lighty                    limbo                     lagda
lcry                      lhs                       lidr                      live-script               logos
logtalk                   lua                       maql                      moocode                   mql
mxml                      make                      mako                      mask                      mason
mathematica               matlab                    matlabsession             minid                     modelica
modula2                   trac-wiki                 monkey                    moon                      mscgen
mupad                     mysql                     myghty                    nasm                      nsis
nemerle                   newlisp                   newspeak                  nginx                     nimrod
nit                       nixos                     numpy                     ocaml                     objective-c
objective-c++             objective-j               octave                    ooc                       opa
openedge                  php                       plpgsql                   pov                       pan
pawn                      perl                      perl6                     pig                       pike
postscript                postgresql                psql                      powershell                prolog
properties                protobuf                  puppet                    pypylog                   python
python3                   py3tb                     pytb                      pycon                     qbasic
qml                       rconsole                  rebol                     rhtml                     spec
rql                       rsl                       racket                    ragel                     ragel-c
ragel-cpp                 ragel-d                   ragel-java                ragel-objc                ragel-ruby
raw                       rd                        red                       redcode                   resource
rexx                      robotframework            rb                        rbcon                     rust
splus                     scss                      sparql                    sql                       swig
sass                      scala                     ssp                       scaml                     scheme
scilab                    shell-session             slim                      smali                     smalltalk
smarty                    snobol                    sp                        squidconf                 stan
sml                       swift                     tads3                     tcl                       tcsh
tex                       tea                       text                      todotxt                   treetop
twig                      ts                        urbiscript                vb.net                    vctreestatus
vgl                       vala                      velocity                  vim                       xml
xml+cheetah               xml+django                xml+evoque                xml+lasso                 xml+mako
xml+myghty                xml+php                   xml+erb                   xml+smarty                xml+velocity
xquery                    xslt                      xul+mozpreproc            xtend                     yaml
yaml+jinja                zephir                    aspx-cs                   aspx-vb                   ahk
c-objdump                 ca65                      cfs                       cpp-objdump               d-objdump
dg                        ec                        liquid                    mozhashpreproc            mozpercentpreproc
nesc                      objdump                   objdump-nasm              rst                       registry
sqlite3                   systemverilog             verilog                   vhdl                      text
========================= ========================= ========================= ========================= =========================
