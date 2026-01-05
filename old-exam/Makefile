DOCKER=docker run -v "$$(pwd):/srv" -w=/srv nowox/latex:2.0
SRC=$(wildcard assets/*.c)
EXECS=$(SRC:.c=.out)
CFLAGS=-Wall -Wextra -Werror -std=c11 -pedantic -O3 -g

all: release 

config.tex: config.m.tex config.yml parse-yml.py
	python ./parse-yml.py config.yml > $@ < $^

exam.pdf: exam.tex FORCE | config.tex code
	latexmk --shell-escape -pdf -jobname=$(basename $@) $<

solution.pdf: exam.tex FORCE | config.tex code
	latexmk --shell-escape -pdf -jobname=$(basename $@) -pdflatex='xelatex %O "\PassOptionsToClass{answers}{exam}\input{%S}"' $<

%.out: %.c
	cc $(CFLAGS) -o $@ $<

code: $(EXECS)

refcard.pdf:
	wget https://github.com/heig-tin-info/refcard/releases/download/2.7.1/refcard.pdf

release: refcard.pdf exam.pdf solution.pdf 
	mkdir -p release
	cp refcard.pdf $@
	cp exam.pdf solution.pdf $@

assembly: exam.pdf | refcard.pdf
	qpdf --empty --pages $< 1-2,r2-r1 -- cover.pdf
	qpdf --empty --pages $< 3-4 -- p1.pdf
	qpdf --empty --pages $< 5-6 -- p2.pdf
	qpdf --empty --pages $< 7-8 -- p3.pdf
	qpdf --empty --pages $< 9-12 -- p4.pdf
	cp cover.pdf release
	cp p*.pdf release

clean:
	$(RM) config.tex
	latexmk -C
	$(RM) *.aux *.fdb_latexmk *.fls *.log *.out *.exitCode
	$(RM) solution.pdf
	$(RM) *.pdf
	$(RM) *.pgf *.stderr *.stdout *.sh
	$(RM) *.dpth *.md5 *.auxlock
	$(RM) -rf release
FORCE:

.PHONY: clean all
