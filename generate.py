import markdown
import json
import glob

def main():
    md_file_list = glob.glob('.\dairy_md\\*.md')
    date_list = [p.split('.\dairy_md\\')[1][:8:] for p in md_file_list]
    for i in range(len(date_list)):
        make_diary_html(date_list, i)
    
    make_index_html()
    
    return True

def make_diary_html(date_list, index):
    date = date_list[index]

    md_path = 'dairy_md\\%s.md'%date
    
    f = open(md_path, 'r', encoding='utf-8-sig')
    sample_text = f.read()
    f.close()
    
    md = markdown.Markdown(extensions=['tables'])
    
    
    
    html_path = 'dairy\\%s.html'%date
    f = open(html_path, 'w', encoding='utf-8-sig')
    

    write_meta_data(f, date)
    
    
    f.write('<article class="markdown-body">\n')

    f.write(md.convert(sample_text))

    f.write('\n<br><br>\n<div class=\"page_link\">')

    if index != 0:
        pre_path = './%s.html'%date_list[index-1]
        f.write('\n<a href=\"%s\"><div class="triangle_left"></div></a>'%pre_path)

    home_path = '../index.html'
    f.write('\n<a href=\"%s\"><div class="square_center"></div></a>'%home_path)

    if index != len(date_list)-1:
        next_path = './%s.html'%date_list[index+1]
        f.write('\n<a href=\"%s\"><div class="triangle_right"></div></a>'%next_path)


    f.write('</div>\n</article>\n</html>')

    f.close()


def write_meta_data(f, date):
    meta_text = '''
    <html>
    <head>
    <meta charset="UTF-8">
    <title>1000plus:%s</title>
    
    <script type="text/x-mathjax-config">
    MathJax.Hub.Config({
      tex2jax: {
        inlineMath: [['$','$'], ['\\(','\\)']],
        processEscapes: true
      },
      CommonHTML: { matchFontHeight: false },
      displayAlign: "left",
      displayIndent: "2em"
    });
    </script>
    
    <script src="https://polyfill.io/v3/polyfill.min.js?features=es6"></script>
    <script async src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.0/MathJax.js?config=TeX-AMS_CHTML"></script>

    <link rel="stylesheet" type="text/css" href="./../github-markdown.css">
    <style>
    .markdown-body {
        font-family: 'Noto Sans JP', sans-serif;
		box-sizing: border-box;
		min-width: 200px;
		max-width: 980px;
		margin: 0 auto;
		padding: 45px;
	}

	@media (max-width: 767px) {
		.markdown-body {
			padding: 15px;
		}
	}
    </style>
    <!-- Favi con -->
    <link rel="shortcut icon" type="image/png" href="s">
    </head>
    '''%date
    
    f.write(meta_text)

    make_index_html()

    return True


def make_index_html():
    index_html = open('index.html', 'w', encoding='utf-8-sig')
    
    meta_text = '''
    <html>
    <head>
    <meta charset="UTF-8">
    <title>1000plus</title>
    <link rel="stylesheet" type="text/css" href="./github-markdown.css">
    <style>
    .markdown-body {
        font-family: 'Noto Sans JP', sans-serif;
		box-sizing: border-box;
		min-width: 200px;
		max-width: 980px;
		margin: 0 auto;
		padding: 45px;
	}

	@media (max-width: 767px) {
		.markdown-body {
			padding: 15px;
		}
	}
    </style>
    <!-- Favi con -->
    <link rel="shortcut icon" type="image/png" href="s">
    </head>
    '''
    index_html.write(meta_text)
    
    index_html.write('<article class="markdown-body">\n')
    index_html.write('<h1>1000plus</h1>')

    
    index_html.write('\n<ul>\n')

    file_list = glob.glob('.\dairy\\*.html')
    count = 0

    for file_path in file_list:
        date = file_path.split('.\dairy\\')[1][:8:]
        year = date[:4:]
        month  = date[4:6:]
        day    = date[6:8]

        index_html.write('\n<li><a href=\"%s\">%s年%s月%s日</a>----Day:%i</li>\n'\
            %(file_path, year, month, day, count))

        count = count + 1

    index_html.write('\n</ul>\n')
    index_html.write('\n</article>\n</html>')
    index_html.close()
    
    return True


if __name__ == '__main__':
    main()