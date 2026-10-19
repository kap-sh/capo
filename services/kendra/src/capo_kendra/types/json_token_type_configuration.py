"""Generated from Smithy shape ``com.amazonaws.kendra#JsonTokenTypeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_kendra.types.string


class JsonTokenTypeConfiguration(TypedDict, closed=True):
    user_name_attribute_field: "capo_kendra.types.string.String"
    """<p>The user name attribute field.</p>"""
    group_attribute_field: "capo_kendra.types.string.String"
    """<p>The group attribute field.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: JsonTokenTypeConfiguration) -> dict:
    out: dict = {}
    out["UserNameAttributeField"] = value["user_name_attribute_field"]
    out["GroupAttributeField"] = value["group_attribute_field"]
    return out


def deserialize_aws_json_1_1(data: dict) -> JsonTokenTypeConfiguration:
    out: JsonTokenTypeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("UserNameAttributeField") is not None:
        out["user_name_attribute_field"] = data["UserNameAttributeField"]
    else:
        out["user_name_attribute_field"] = ""
    if data.get("GroupAttributeField") is not None:
        out["group_attribute_field"] = data["GroupAttributeField"]
    else:
        out["group_attribute_field"] = ""
    return out
