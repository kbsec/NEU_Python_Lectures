# make slides and add to markdown

import os

# the slides are generated using reveal.js
nb_string = "jupyter nbconvert {notebook} --to slides "
lecture_base = '# [Lecture {num}:](/Lecture_slides/{slide}) \n'
notebooks = [i for i in os.listdir(".") if i.endswith(".ipynb")]
slide_comment = "[comment]:LECTURE_SLIDES"
README = "../README.md"
def make_slides_and_move(file_names):
    slide_names = [nb.replace("ipynb", 'slides.html') for nb in file_names]
    cmd = nb_string.format(notebook=' '.join(file_names))
    os.system(cmd)
    print(cmd)
    for sl in slide_names:
        print("[!] Made slides for {}".format(sl))
        os.rename("./" + sl, '../Lecture_slides/'+sl)


if __name__ == '__main__':
    print("[*] Creating  all Slide Shows")
    make_slides_and_move(notebooks)
    with open(README, 'r') as f:
        z = f.read().split(slide_comment)
        f.close()
    lectures = sorted([i for i in os.listdir("../Lecture_slides/") if i.endswith(".html")])
    lecture_info = ''
    for i in range(len(lectures)):
        lecture_info += lecture_base.format(num=i+1, slide=lectures[i])
    z_new = z[0]  + slide_comment + '\n\n' + lecture_info + '\n' + slide_comment + z[2]
    with open(README, 'w+') as f:
        f.write(z_new)
        print("[!] Wrote New Markdown")
