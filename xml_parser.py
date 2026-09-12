from xml.etree import ElementTree as ET

# XXE vulnerability: parsing untrusted XML payload without entity restriction
def parse_user_xml(xml_payload: str):
    root = ET.fromstring(xml_payload)
    return {"tag": root.tag, "text": root.text}
