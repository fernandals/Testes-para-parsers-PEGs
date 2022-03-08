grammar Expr;		

//prog	:	(attr | expr NEWLINE)* ;

//prog 	: 	(expr NEWLINE | attr)* ;

//prog	:	(attr)*	
//		|	(expr NEWLINE)*	
//		;

prog	:	(expr NEWLINE | ID '=' expr NEWLINE)* ;

//prog	: ( ID '=' expr NEWLINE)* ;

attr	:	ID '=' expr NEWLINE;
expr	:	expr ('*'|'/') expr
    	|	expr ('+'|'-') expr
    	|	INT
    	|	ID
    	|	'(' expr ')'
    	;
ID		: [a-z]+ ;
NEWLINE : [\r\n] ;
INT     : [0-9]+ ;
