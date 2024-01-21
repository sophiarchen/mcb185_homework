#Authors: Sophia Chen, Devin Fan
gunzip -c dictionary.gz | grep "r" | grep -E "[zoniacr]{4,}" | grep -v "[qwetyupsdfghjklxvbm]" | wc