"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeNameAndValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_name
    import capo_clouddirectory.types.typed_attribute_value


class AttributeNameAndValue(TypedDict, closed=True):
    attribute_name: "capo_clouddirectory.types.attribute_name.AttributeName"
    """<p>The attribute name of the typed link.</p>"""
    value: "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    """<p>The value for the typed link.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeNameAndValue) -> dict:
    out: dict = {}
    out["AttributeName"] = value["attribute_name"]
    import capo_clouddirectory.types.typed_attribute_value

    out["Value"] = capo_clouddirectory.types.typed_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> AttributeNameAndValue:
    out: AttributeNameAndValue = {}  # type: ignore[typeddict-item]
    if data.get("AttributeName") is not None:
        out["attribute_name"] = data["AttributeName"]
    else:
        out["attribute_name"] = ""
    if data.get("Value") is not None:
        import capo_clouddirectory.types.typed_attribute_value

        out["value"] = capo_clouddirectory.types.typed_attribute_value.deserialize_json(
            data["Value"]
        )
    else:
        import capo_clouddirectory.types._unknown

        out["value"] = capo_clouddirectory.types._unknown.UnknownUnionMember("")
    return out
