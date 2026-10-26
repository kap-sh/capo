"""Generated from Smithy shape ``com.amazonaws.qapps#DocumentAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.document_attribute_key
    import capo_qapps.types.document_attribute_value


class DocumentAttribute(TypedDict, closed=True):
    name: "capo_qapps.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier for the attribute.</p>"""
    value: "capo_qapps.types.document_attribute_value.DocumentAttributeValue"
    """<p>The value of the attribute. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DocumentAttribute) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_qapps.types.document_attribute_value

    out["value"] = capo_qapps.types.document_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> DocumentAttribute:
    out: DocumentAttribute = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("value") is not None:
        import capo_qapps.types.document_attribute_value

        out["value"] = capo_qapps.types.document_attribute_value.deserialize_json(
            data["value"]
        )
    else:
        out["value"] = {"$unknown": {"name": ""}}
    return out
