"""Generated from Smithy shape ``com.amazonaws.kendra#DocumentAttribute``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_kendra.errors import DeserializationError

if TYPE_CHECKING:
    import capo_kendra.types.document_attribute_key
    import capo_kendra.types.document_attribute_value


class DocumentAttribute(TypedDict, closed=True):
    key: "capo_kendra.types.document_attribute_key.DocumentAttributeKey"
    """<p>The identifier for the attribute.</p>"""
    value: "capo_kendra.types.document_attribute_value.DocumentAttributeValue"
    """<p>The value of the attribute.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DocumentAttribute) -> dict:
    out: dict = {}
    out["Key"] = value["key"]
    import capo_kendra.types.document_attribute_value

    out["Value"] = capo_kendra.types.document_attribute_value.serialize_aws_json_1_1(
        value["value"]
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> DocumentAttribute:
    out: DocumentAttribute = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        out["key"] = data["Key"]
    else:
        out["key"] = ""
    if data.get("Value") is not None:
        import capo_kendra.types.document_attribute_value

        out["value"] = (
            capo_kendra.types.document_attribute_value.deserialize_aws_json_1_1(
                data["Value"]
            )
        )
    else:
        raise DeserializationError("DocumentAttribute.value required")
    return out
