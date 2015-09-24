.PHONY: compile clean test install

compile: HelloWorld

HelloWorld: HelloWorld.c HelloWorld.h
	@echo '*** Building...'
	gcc -o $@ $<

clean:
	@echo '*** Cleaning...'
	rm -f HelloWorld

test: compile
	@echo '*** Testing...'
	[ "`./HelloWorld`" = 'Hello, World!' ]

install:
	@echo '*** Installing...'
	install -m 755 -d $(DESTDIR)/usr/bin
	install -m 755 HelloWorld $(DESTDIR)/usr/bin/
