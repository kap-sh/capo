"""Generated from Smithy shape ``com.amazonaws.bedrockagent#MetadataAttributeValue``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agent.types.metadata_value_type
    import capo_bedrock_agent.types.number_value
    import capo_bedrock_agent.types.string_list_value
    import capo_bedrock_agent.types.string_value


class MetadataAttributeValue(TypedDict, closed=True):
    type: "capo_bedrock_agent.types.metadata_value_type.MetadataValueType"
    """<p>The type of the metadata attribute.</p>"""
    number_value: NotRequired["capo_bedrock_agent.types.number_value.NumberValue"]
    """<p>The value of the numeric metadata attribute.</p>"""
    boolean_value: NotRequired["bool"]
    """<p>The value of the Boolean metadata attribute.</p>"""
    string_value: NotRequired["capo_bedrock_agent.types.string_value.StringValue"]
    """<p>The value of the string metadata attribute.</p>"""
    string_list_value: NotRequired[
        "capo_bedrock_agent.types.string_list_value.StringListValue"
    ]
    """<p>An array of strings that define the value of the metadata attribute.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataAttributeValue) -> dict:
    out: dict = {}
    import capo_bedrock_agent.types.metadata_value_type

    out["type"] = capo_bedrock_agent.types.metadata_value_type.serialize_json(
        value["type"]
    )
    if "number_value" in value:
        out["numberValue"] = (
            "NaN"
            if value["number_value"] != value["number_value"]
            else "Infinity"
            if value["number_value"] == float("inf")
            else "-Infinity"
            if value["number_value"] == float("-inf")
            else value["number_value"]
        )
    if "boolean_value" in value:
        out["booleanValue"] = value["boolean_value"]
    if "string_value" in value:
        out["stringValue"] = value["string_value"]
    if "string_list_value" in value:
        import capo_bedrock_agent.types.string_list_value

        out["stringListValue"] = (
            capo_bedrock_agent.types.string_list_value.serialize_json(
                value["string_list_value"]
            )
        )
    return out


def deserialize_json(data: dict) -> MetadataAttributeValue:
    out: MetadataAttributeValue = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock_agent.types.metadata_value_type

        out["type"] = capo_bedrock_agent.types.metadata_value_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_bedrock_agent.types.metadata_value_type.MetadataValueType", ""
        )
    if data.get("numberValue") is not None:
        out["number_value"] = float(data["numberValue"])
    if data.get("booleanValue") is not None:
        out["boolean_value"] = data["booleanValue"]
    if data.get("stringValue") is not None:
        out["string_value"] = data["stringValue"]
    if data.get("stringListValue") is not None:
        import capo_bedrock_agent.types.string_list_value

        out["string_list_value"] = (
            capo_bedrock_agent.types.string_list_value.deserialize_json(
                data["stringListValue"]
            )
        )
    return out


def redact_sensitive(value: MetadataAttributeValue) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "number_value" in value:
        out["number_value"] = "*** Sensitive Data Redacted ***"
    if "string_value" in value:
        out["string_value"] = "*** Sensitive Data Redacted ***"
    if "string_list_value" in value:
        import capo_bedrock_agent.types.string_list_value

        out["string_list_value"] = (
            capo_bedrock_agent.types.string_list_value.redact_sensitive(
                value["string_list_value"]
            )
        )
    return out
