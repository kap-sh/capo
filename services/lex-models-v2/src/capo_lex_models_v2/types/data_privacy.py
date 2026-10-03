"""Generated from Smithy shape ``com.amazonaws.lexmodelsv2#DataPrivacy``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lex_models_v2.types.child_directed


class DataPrivacy(TypedDict, closed=True):
    child_directed: "capo_lex_models_v2.types.child_directed.ChildDirected"
    """<p>For each Amazon Lex bot created with the Amazon Lex Model Building Service, you must specify whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to the Children's Online Privacy Protection Act (COPPA) by specifying <code>true</code> or <code>false</code> in the <code>childDirected</code> field. By specifying <code>true</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. By specifying <code>false</code> in the <code>childDirected</code> field, you confirm that your use of Amazon Lex <b>is not</b> related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. You may not specify a default value for the <code>childDirected</code> field that does not accurately reflect whether your use of Amazon Lex is related to a website, program, or other application that is directed or targeted, in whole or in part, to children under age 13 and subject to COPPA. If your use of Amazon Lex relates to a website, program, or other application that is directed in whole or in part, to children under age 13, you must obtain any required verifiable parental consent under COPPA. For information regarding the use of Amazon Lex in connection with websites, programs, or other applications that are directed or targeted, in whole or in part, to children under age 13, see the <a href="http://aws.amazon.com/lex/faqs#data-security">Amazon Lex FAQ</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataPrivacy) -> dict:
    out: dict = {}
    out["childDirected"] = value.get("child_directed", False)
    return out


def deserialize_json(data: dict) -> DataPrivacy:
    out: DataPrivacy = {}  # type: ignore[typeddict-item]
    if data.get("childDirected") is not None:
        out["child_directed"] = data["childDirected"]
    else:
        out["child_directed"] = False
    return out
