"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#RedactionConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.custom_data_identifier_list
    import capo_bedrock_agentcore.types.redaction_identifier_list


class RedactionConfiguration(TypedDict, closed=True):
    identifiers: NotRequired[
        "capo_bedrock_agentcore.types.redaction_identifier_list.RedactionIdentifierList"
    ]
    """<p>The managed data identifiers to apply. These match the CloudWatch Logs managed data identifiers.</p>"""
    custom_data_identifiers: NotRequired[
        "capo_bedrock_agentcore.types.custom_data_identifier_list.CustomDataIdentifierList"
    ]
    """<p>Custom data identifiers to apply, up to 10. You can use custom identifiers without any managed identifiers.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RedactionConfiguration) -> dict:
    out: dict = {}
    if "identifiers" in value:
        import capo_bedrock_agentcore.types.redaction_identifier_list

        out["identifiers"] = (
            capo_bedrock_agentcore.types.redaction_identifier_list.serialize_json(
                value["identifiers"]
            )
        )
    if "custom_data_identifiers" in value:
        import capo_bedrock_agentcore.types.custom_data_identifier_list

        out["customDataIdentifiers"] = (
            capo_bedrock_agentcore.types.custom_data_identifier_list.serialize_json(
                value["custom_data_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> RedactionConfiguration:
    out: RedactionConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_bedrock_agentcore.types.redaction_identifier_list

        out["identifiers"] = (
            capo_bedrock_agentcore.types.redaction_identifier_list.deserialize_json(
                data["identifiers"]
            )
        )
    if data.get("customDataIdentifiers") is not None:
        import capo_bedrock_agentcore.types.custom_data_identifier_list

        out["custom_data_identifiers"] = (
            capo_bedrock_agentcore.types.custom_data_identifier_list.deserialize_json(
                data["customDataIdentifiers"]
            )
        )
    return out
