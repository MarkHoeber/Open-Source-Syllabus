import sphinx_rtd_theme
import sphinx_bootstrap_theme


extensions = []

templates_path = ['_templates']

source_suffix = '.rst'

master_doc = 'index'

project = u'Tools and Technologies for Technical Writers'
copyright = u'2016, Mark Hoeber'
author = u'Mark Hoeber'

exclude_patterns = []

pygments_style = 'sphinx'


todo_include_todos = True




html_theme = 'bootstrap'
html_theme_path = sphinx_bootstrap_theme.get_html_theme_path()

html_theme_options = {

  'navbar_site_name': "Syllabus",
  'navbar_pagenav_name': "Lesson",
  'source_link_position': "footer",

  #'bootswatch_theme': "Sandstone"
}


