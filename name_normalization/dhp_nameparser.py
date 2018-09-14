from name_normalization import config
from model.req_parser_model import MemberName_schema, MemberName

suff = config.suffixs.split("*")

def name_normalization(org_name):
    name = org_name.upper()
    for suffix in suff:
        if suffix in name:
            name = name.replace(suffix, " ")
    for special_char in config.special_chars:
        if special_char in name:
            name = name.replace(special_char, "")
    if name == org_name.upper():
        status = 'UNCHANGED'
    else:
        status = "CHANGED"
    return MemberName_schema().dump(MemberName(name=name, status=status)).data
