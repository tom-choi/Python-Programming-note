import re
CDATA_CONTENT_PATTERN = r'<!\[CDATA\[.*?\]\]>'
TAG_CONTENT_PATTERN = r'<([A-Z]{1,9})>[^<]*</\1>'

def isValid(code: str) -> bool:
    i = 1
    code = re.sub(CDATA_CONTENT_PATTERN, "#", code)
    print("第" + str(i) + "次: "+ code)
    i += 1
    for _ in range(code.count('</')):
        code = re.sub(TAG_CONTENT_PATTERN, "#", code)
        print("第" + str(i) + "次: "+ code)
        i += 1
    return code == "#"

isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>")
isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>")
isValid("<A>  <B> </A>   </B>")