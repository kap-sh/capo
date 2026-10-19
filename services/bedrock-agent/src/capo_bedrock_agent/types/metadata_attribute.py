"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataAttribute``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_agent.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agent.types.key
    import capo_bedrock_agent.types.metadata_attribute_value


class MetadataAttribute(TypedDict, closed=True):
    key: "capo_bedrock_agent.types.key.Key"
    """<p>The key of the metadata attribute.</p>"""
    value: "capo_bedrock_agent.types.metadata_attribute_value.MetadataAttributeValue"
    """<p>Contains the value of the metadata attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttribute) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_bedrock_agent.types.metadata_attribute_value

    out["value"] = capo_bedrock_agent.types.metadata_attribute_value.serialize_json(
        value["value"]
    )
    return out


def deserialize_json(data: dict) -> MetadataAttribute:
    out: MetadataAttribute = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("value") is not None:
        import capo_bedrock_agent.types.metadata_attribute_value

        out["value"] = (
            capo_bedrock_agent.types.metadata_attribute_value.deserialize_json(
                data["value"]
            )
        )
    else:
        raise DeserializationError("MetadataAttribute.value required")
    return out


def redact_sensitive(value: MetadataAttribute) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "key" in value:
        out["key"] = "*** Sensitive Data Redacted ***"
    if "value" in value:
        import capo_bedrock_agent.types.metadata_attribute_value

        out["value"] = (
            capo_bedrock_agent.types.metadata_attribute_value.redact_sensitive(
                value["value"]
            )
        )
    return out
