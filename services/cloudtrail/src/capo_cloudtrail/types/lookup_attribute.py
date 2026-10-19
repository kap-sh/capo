"""Generated from Smithy shape ``com.amazonaws.cloudtrail#LookupAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.lookup_attribute_key
    import capo_cloudtrail.types.lookup_attribute_value


class LookupAttribute(TypedDict, closed=True):
    attribute_key: "capo_cloudtrail.types.lookup_attribute_key.LookupAttributeKey"
    """<p>Specifies an attribute on which to filter the events returned.</p>"""
    attribute_value: "capo_cloudtrail.types.lookup_attribute_value.LookupAttributeValue"
    r"""<p>Specifies a value for the specified <code>AttributeKey</code>.</p> <p>The maximum length for the <code>AttributeValue</code> is 2000 characters. The following characters ('<code>_</code>', '<code> </code>', '<code>,</code>', '<code>\\n</code>') count as two characters towards the 2000 character limit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LookupAttribute) -> dict:
    out: dict = {}
    import capo_cloudtrail.types.lookup_attribute_key

    out["AttributeKey"] = (
        capo_cloudtrail.types.lookup_attribute_key.serialize_aws_json_1_1(
            value["attribute_key"]
        )
    )
    out["AttributeValue"] = value["attribute_value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LookupAttribute:
    out: LookupAttribute = {}  # type: ignore[typeddict-item]
    if data.get("AttributeKey") is not None:
        import capo_cloudtrail.types.lookup_attribute_key

        out["attribute_key"] = (
            capo_cloudtrail.types.lookup_attribute_key.deserialize_aws_json_1_1(
                data["AttributeKey"]
            )
        )
    else:
        import typing

        out["attribute_key"] = typing.cast(
            "capo_cloudtrail.types.lookup_attribute_key.LookupAttributeKey", ""
        )
    if data.get("AttributeValue") is not None:
        out["attribute_value"] = data["AttributeValue"]
    else:
        out["attribute_value"] = ""
    return out
