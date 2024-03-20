import glob
import json
import os.path
import random
import re
import traceback

repo = "D:/code/github/ArknightsData"
lang = "en-US"

docter = "博士" if lang == "zh-CN" else "Docter"
regexp_dialog = "\[name=\"(?P<role>[^\]]+)\"\]\s*(?P<content>.+)"
regexp_option = "\[Decision\(options=\"(?P<options>.+)\", values="
regexp_subtitle = "\[Subtitle\(text=\"“*(?P<content>[^\"“”]+”*)\","


def replace_var(string):
    # return string
    return re.sub(r"(Dr\.)*\{@nickname}(博士)*", "Doctor", string)


def parse():
    out_samples = []
    files_dict = {}
    files = list(glob.iglob(os.path.join(repo, f"{lang}/gamedata/story/obt/main/*")))
    files += list(glob.iglob(os.path.join(repo, f"{lang}/gamedata/story/obt/memory/*")))
    files += list(glob.iglob(os.path.join(repo, f"{lang}/gamedata/story/activities/*/*.txt")))
    for file in files:
        filename = file.split("story/")[-1]
        files_dict[filename] = {
            "content_file": file,
            "info_file": file.replace("story/", "story/[uc]info/")
        }

    for filename, file_dict in files_dict.items():
        text = ""
        conversation = []
        with open(file_dict["content_file"], "r", encoding="utf-8") as f:
            characters = set()
            for line in f:
                m = re.search(regexp_dialog, line)
                if m:
                    characters.add(m['role'])
                    conversation.append({"role": m['role'], "content": replace_var(m['content'])})
                    continue
                m = re.search(regexp_option, line)
                if m:
                    conversation.append({"role": docter, "content": replace_var(random.choice(m['options'].split(';'))), "type": "option"})
                    continue
                m = re.search(regexp_subtitle, line)
                if m:
                    conversation.append({"role": "", "content": replace_var(m['content'])})
                    continue
        if conversation:
            try:
                with open(file_dict["info_file"], "r", encoding="utf-8") as f:
                    context = f.read().strip()
                    out_samples.append({
                        "context": context,
                        "conversation": conversation,
                        "meta": {
                            "source": filename,
                            "characters": list(characters)
                        }
                    })
            except:
                print(traceback.format_exc())
    return out_samples


if __name__ == '__main__':
    samples = parse()
    with open(f"data/story_{lang}.jsonl", "w", encoding="utf-8") as f:
        for sample in samples:
            print(json.dumps(sample, ensure_ascii=False), file=f)