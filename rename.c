#include <stdio.h>

/*
    ファイルの名前を変更する。

    oldName: 変更するファイルの名前
    newName: 変更後のファイルの名前
    戻り値:  成功したら 0以外、失敗したら 0
*/
int renameFile(const char* oldName, const char* newName)
{
    return !(rename(oldName, newName));
}

int main(void)
{
    if (renameFile("Mcsv5.py", "reMcsv1.py")) {
        puts("名前を変更しました。");
    }
    else {
        puts("名前の変更に失敗しました。");
    }

    return 0;
}
