#! bin/bash

# $1 nome da gramatica | $2 primeira regra da gramatica

[ ! -e error ] || rm error

cd "antlr"

files=0
error=0

#for filename in ../tests/*;
#for filename in ../tests/ok/*;
for filename in ../tests/erro/*;
do
    if [[ !(-d $filename) ]]
    then
        files=$((files+1))

        test="$(java org.antlr.v4.gui.TestRig $1 $2 $filename 2>&1 >>../error)" 
    
        if [ "$test" \> 0 ]
        then
            echo -e "$filename:\n$test\n" >>../error
            error=$((error+1))
        fi
    fi

done

echo -e "Foram testados $files arquivos."
echo -e "$error falharam e $((files-error)) estão corretos."

