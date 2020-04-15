import sys
import glob

md_file_list = glob.glob('.\diary_md\\*.md')
date_list = [p.split('.\diary_md\\')[1][:8:] for p in md_file_list]


md_path = md_file_list[0]
date=str(date_list[0])

f = open(md_path, 'r', encoding='utf-8-sig')
sample_text = f.read()
f.close()


N = len(md_file_list)

for i in range(N):
    md_path = md_file_list[i]
    date=str(date_list[i])
    
    year = date[:4:]
    month = date[4:6:]
    day = date[6::]

    date_ja  = '%s年%s月%s日'%(year, month, day)
    date_index = '%s-%s-%s'%(year, month, day)
    add_text = 'Title: %s\n'%date_ja\
               + 'Date: %s\n'%date_index\
               + 'Category: Nikki\n'\
               + 'Tags: \n'\
               + 'Slug: %s\n'%date\
               + 'Authors: takala4\n'\
               + 'Day: %i\n\n\n'%i
    
    f = open(md_path, 'r', encoding='utf-8-sig')
    sample_text = f.read()
    f.close()
    
    f = open('content\\%s.md'%date, 'w', encoding='utf-8-sig')
    write_text = add_text + '\n\n'.join(sample_text.split('\n\n')[1::])
    write_text = write_text.replace('![]', '![image]')
    f.write(write_text)
    f.close()