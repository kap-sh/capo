"""Generated from Smithy shape ``com.amazonaws.clouddirectory#AttributeKeyAndValue``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_clouddirectory.errors import DeserializationError

if TYPE_CHECKING:
    import capo_clouddirectory.types.attribute_key
    import capo_clouddirectory.types.typed_attribute_value


class AttributeKeyAndValue(TypedDict, closed=True):
    key: "capo_clouddirectory.types.attribute_key.AttributeKey"
    """<p>The key of the attribute.</p>"""
    value: "capo_clouddirectory.types.typed_attribute_value.TypedAttributeValue"
    """<p>The value of the attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AttributeKeyAndValue) -> dict:
    out: dict = {}
    import capo_clouddirectory.types.attribute_key

    out["Key"] = capo_clouddirectory.types.attribute_key.serialize_json(value["key"])
    import capo_clouddirectory.types.typed_attribute_value

    out["Value"] = capo_clouddirectory.types.typed_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> AttributeKeyAndValue:
    out: AttributeKeyAndValue = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_clouddirectory.types.attribute_key

        out["key"] = capo_clouddirectory.types.attribute_key.deserialize_json(
            data["Key"]
        )
    else:
        raise DeserializationError("AttributeKeyAndValue.key required")
    if data.get("Value") is not None:
        import capo_clouddirectory.types.typed_attribute_value

        out["value"] = capo_clouddirectory.types.typed_attribute_value.deserialize_json(
            data["Value"]
        )
    else:
        import capo_clouddirectory.types._unknown

        out["value"] = capo_clouddirectory.types._unknown.UnknownUnionMember("")
    return out
