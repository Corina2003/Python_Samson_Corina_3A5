#The build_xml_element function receives the following parameters: tag, content, and key-value elements given as name-parameters. Build and return a string that represents the corresponding XML element. Example: build_xml_element ("a", "Hello there", href =" http://python.org ", _class =" my-link ", id= " someid ") returns the string = "<a href="http://python.org "_class = " my-link " id = " someid "> Hello there </a>"
def build_xml_element(tag, content, **attributes):
    attribute_str = ""

    for key, value in attributes.items():
        attribute_str += f' {key}="{value}"'

    xml_element = f"<{tag}{attribute_str}>{content}</{tag}>"
    return xml_element

result = build_xml_element("a", "Hello there", href="http://python.org", _class="my-link", id="someid")
print(result)
