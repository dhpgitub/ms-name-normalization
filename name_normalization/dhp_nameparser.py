from name_normalization import config
from model.req_parser_model import MemberName_schema, MemberName

def name_normalization(org_name):
    name = org_name.upper()
    for special_char in config.special_chars:
        if special_char in name:
            name = name.replace(special_char, "")
    for suffixe in config.suffixes:
        if suffixe in name:
            name = name.replace(suffixe, "")
    if name == org_name.upper():
        status = 'UNCHANGED'
    else:
        status = "CHANGED"
    return MemberName_schema().dump(MemberName(name=name, status=status)).data
