def update_version(ver):
    import os

    from sqlalchemy import create_engine
    from sqlalchemy.sql import text

    engine = create_engine("sqlite:///docs.db")
    versions = create_engine("sqlite:///migrations/versions.db")
    curVer = versions.execute("SELECT cur FROM version").fetchone()[0]
    dir_list = os.listdir("migrations")[:-1]
    if ver <= curVer:
        return "Уже стоит более актуальная версия."
    elif len(dir_list) < ver:
        return "Такой версии нет."
    else:
        for i in dir_list[curVer:ver]:
            file = open("migrations/%s" % i, "r")
            sqlText = file.read().split(sep=";\n")
            file.close()
            for line in sqlText:
                engine.execute(text(line))
        versions.execute("UPDATE version SET cur =%s WHERE cur = %s" % (len(dir_list), curVer))
        return "Версия успешно обновлена."


if __name__ == "__main__":
    print(update_version(1))
