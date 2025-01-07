import os

from markdowntohtmlnode import markdown_to_html_node
from parentnode import ParentNode
from extracttitle import extract_title


def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_path_reader = file.read()
    with open(template_path) as file:
        template_path_reader = file.read()
    converted_html_string = markdown_to_html_node(from_path_reader).to_html()
    title = extract_title(from_path_reader)
    replaced_title_template = template_path_reader.replace(r"{{ Title }}", title)
    replaced_content_template = replaced_title_template.replace(r"{{ Content }}", converted_html_string)
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(dest_path, "w") as file:
        file.write(replaced_content_template)
    
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    contents = os.listdir(dir_path_content)
    print(f"contents are {contents}")
    for obj in contents:
        obj_src_path = os.path.join(dir_path_content, obj)
        if os.path.isfile(obj_src_path) and obj.endswith(".md"):
            html_obj = obj[:-3] + ".html"
            html_obj_dst_path = os.path.join(dest_dir_path, html_obj)
            generate_page(obj_src_path, template_path, html_obj_dst_path)
        elif os.path.isdir(obj_src_path):
            obj_dst_path = os.path.join(dest_dir_path, obj)
            generate_pages_recursive(obj_src_path, template_path, obj_dst_path)