#! bin/bash

# $1 nome da gramática | $2 primeira regra da gramática | $3 seleção da pasta testada (1, 2, 3)

[ ! -e error ] || rm error

cd "antlr"

files=0
error=0
direct=" "

if [[ $3 -eq 2 ]]
then
    direct="../tests/ok/*"
elif [[ $3 -eq 3 ]]
then 
    direct="../tests/erro/*"
else
    direct="../tests/*"
fi

for filename in $direct;
do
    if [[ !(-d $filename) ]]
    then
        files=$((files+1))

        #test="$(java org.antlr.v4.gui.TestRig $1 $2 $filename 2>&1 >>../error)" 
   
        test="$(grun $1 $2 $filename 2>&1 >>../error)"

        if [ "$test" \> 0 ]
        then
            echo -e "$filename:\n$test\n" >>../error
            error=$((error+1))
        fi
    fi

done

echo -e "Foram testados $files arquivos na pasta $direct."
echo -e "$error falharam e $((files-error)) estão corretos."

