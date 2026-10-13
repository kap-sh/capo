"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#InputConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.inline_payload
    import capo_bedrock_data_automation.types.s3_object


class InputConfiguration(TypedDict, closed=True):
    s3_object: NotRequired["capo_bedrock_data_automation.types.s3_object.S3Object"]
    """S3 object"""
    inline_payload: NotRequired[
        "capo_bedrock_data_automation.types.inline_payload.InlinePayload"
    ]
    """Input Payload"""


# --- restJson1 ser/de ---
def serialize_json(value: InputConfiguration) -> dict:
    out: dict = {}
    if "s3_object" in value:
        import capo_bedrock_data_automation.types.s3_object

        out["s3Object"] = capo_bedrock_data_automation.types.s3_object.serialize_json(
            value["s3_object"]
        )
    if "inline_payload" in value:
        import capo_bedrock_data_automation.types.inline_payload

        out["inlinePayload"] = (
            capo_bedrock_data_automation.types.inline_payload.serialize_json(
                value["inline_payload"]
            )
        )
    return out


def deserialize_json(data: dict) -> InputConfiguration:
    out: InputConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("s3Object") is not None:
        import capo_bedrock_data_automation.types.s3_object

        out["s3_object"] = (
            capo_bedrock_data_automation.types.s3_object.deserialize_json(
                data["s3Object"]
            )
        )
    if data.get("inlinePayload") is not None:
        import capo_bedrock_data_automation.types.inline_payload

        out["inline_payload"] = (
            capo_bedrock_data_automation.types.inline_payload.deserialize_json(
                data["inlinePayload"]
            )
        )
    return out


def redact_sensitive(value: InputConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "inline_payload" in value:
        import capo_bedrock_data_automation.types.inline_payload

        out["inline_payload"] = (
            capo_bedrock_data_automation.types.inline_payload.redact_sensitive(
                value["inline_payload"]
            )
        )
    return out
