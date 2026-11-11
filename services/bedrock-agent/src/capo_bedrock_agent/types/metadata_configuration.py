"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.field_type
    import capo_bedrock_agent.types.metadata_key_name
    import capo_bedrock_agent.types.searchable_status


class MetadataConfiguration(TypedDict, closed=True):
    name: "capo_bedrock_agent.types.metadata_key_name.MetadataKeyName"
    """<p>The name of the custom metadata field.</p>"""
    type: "capo_bedrock_agent.types.field_type.FieldType"
    """<p>The data type of the custom metadata field. Valid values are <code>STRING</code> and <code>STRING_LIST</code>.</p>"""
    searchability: "capo_bedrock_agent.types.searchable_status.SearchableStatus"
    """<p>Specifies whether the custom metadata field is searchable. Valid values:</p> <ul> <li> <p> <code>ENABLED</code> – The field is searchable.</p> </li> <li> <p> <code>DISABLED</code> – The field is not searchable.</p> </li> </ul>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataConfiguration) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_bedrock_agent.types.field_type

    out["type"] = capo_bedrock_agent.types.field_type.serialize_json(value["type"])
    import capo_bedrock_agent.types.searchable_status

    out["searchability"] = capo_bedrock_agent.types.searchable_status.serialize_json(
        value["searchability"]
    )
    return out


def deserialize_json(data: dict) -> MetadataConfiguration:
    out: MetadataConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_bedrock_agent.types.field_type

        out["type"] = capo_bedrock_agent.types.field_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_bedrock_agent.types.field_type.FieldType", "")
    if data.get("searchability") is not None:
        import capo_bedrock_agent.types.searchable_status

        out["searchability"] = (
            capo_bedrock_agent.types.searchable_status.deserialize_json(
                data["searchability"]
            )
        )
    else:
        import typing

        out["searchability"] = typing.cast(
            "capo_bedrock_agent.types.searchable_status.SearchableStatus", ""
        )
    return out


def redact_sensitive(value: MetadataConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    return out
