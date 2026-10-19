"""Generated from Smithy shape ``com.amazonaws.identitystore#UniqueAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_identitystore.types.attribute_path
    import capo_identitystore.types.attribute_value


class UniqueAttribute(TypedDict, closed=True):
    attribute_path: "capo_identitystore.types.attribute_path.AttributePath"
    """<p>A string representation of the path to a given attribute or sub-attribute. Supports JMESPath.</p>"""
    attribute_value: "capo_identitystore.types.attribute_value.AttributeValue"
    """<p>The value of the attribute. This is a <code>Document</code> type. This type is not supported by Java V1, Go V1, and older versions of the CLI.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UniqueAttribute) -> dict:
    out: dict = {}
    out["AttributePath"] = value["attribute_path"]
    out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UniqueAttribute:
    out: UniqueAttribute = {}  # type: ignore[typeddict-item]
    if data.get("AttributePath") is not None:
        out["attribute_path"] = data["AttributePath"]
    else:
        out["attribute_path"] = ""
    if data.get("AttributeValue") is not None:
        out["attribute_value"] = data["AttributeValue"]
    else:
        out["attribute_value"] = None
    return out
