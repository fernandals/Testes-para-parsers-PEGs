grammar test;
id3:	id1 | id2;
id2:	I2 LETTER+
   ;
id1:	I1 LETTER 
   |	I1 LETTER id1
   ; 
   
I2:	'2';
I1:	'1'; 
LETTER:	[a-z] ;	
