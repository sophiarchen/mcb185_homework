echo "Name: Sophia Chen"
echo "Linux User Name: $USER"

gunzip -c dictionary.gz | grep "a" | grep -E "[muocfta]{4,}" | grep -v "[^muocfta]" | wc
gunzip -c dictionary.gz | grep "b" | grep -E "[tairnlb]{4,}" | grep -v "[^tairnlb]" | wc
gunzip -c dictionary.gz | grep "c" | grep -E "[maodinc]{4,}" | grep -v "[^maodinc]" | wc
gunzip -c dictionary.gz | grep "z" | grep -E "[anoigrz]{4,}" | grep -v "[^anoigrz]" | wc