" Geru confs
setlocal textwidth=130
setlocal colorcolumn=130

" Check the code
if filereadable('Makefile')
    inoremap <F5> <ESC>!make\ quick-lint
    nnoremap <F5> !make\ quick-lint
    vnoremap <F5> !make\ quick-lint
endif

if filereadable('development.ini')
    if executable('pshell')
        inoremap <S-F5> <ESC>!pshell\ development.ini
        nnoremap <S-F5> !pshell\ development.ini
        vnoremap <S-F5> !pshell\ development.ini
        inoremap <C-F5> <ESC>!pshell\ development.ini
        nnoremap <C-F5> !pshell\ development.ini
        vnoremap <C-F5> !pshell\ development.ini
    endif
endif


" Nosetest function under the cursor
if executable('nosetests')
    inoremap <F6> <ESC>!nosetests\ <cword>
    nnoremap <F6> !nosetests\ <cword>
    vnoremap <F6> !nosetests\ <cword>
endif
    
" S-F6 run all tests
if filereadable('Makefile')
    if executable('nosetests')
        inoremap <S-F6> <ESC>!make\ quick-test
        nnoremap <S-F6> !make\ quick-test
        vnoremap <S-F6> !make\ quick-test
        inoremap <C-F6> <ESC>!make\ quick-test
        nnoremap <C-F6> !make\ quick-test
        vnoremap <C-F6> !make\ quick-test
    endif
endif
