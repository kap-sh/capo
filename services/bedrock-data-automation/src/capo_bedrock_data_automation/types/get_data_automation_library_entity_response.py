"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#GetDataAutomationLibraryEntityResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.entity_details


class GetDataAutomationLibraryEntityResponse(TypedDict, closed=True):
    entity: NotRequired[
        "capo_bedrock_data_automation.types.entity_details.EntityDetails"
    ]
    """Detailed information about the entity"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataAutomationLibraryEntityResponse) -> dict:
    out: dict = {}
    if "entity" in value:
        import capo_bedrock_data_automation.types.entity_details

        out["entity"] = (
            capo_bedrock_data_automation.types.entity_details.serialize_json(
                value["entity"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetDataAutomationLibraryEntityResponse:
    out: GetDataAutomationLibraryEntityResponse = {}  # type: ignore[typeddict-item]
    if data.get("entity") is not None:
        import capo_bedrock_data_automation.types.entity_details

        out["entity"] = (
            capo_bedrock_data_automation.types.entity_details.deserialize_json(
                data["entity"]
            )
        )
    return out


def redact_sensitive(value: GetDataAutomationLibraryEntityResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "entity" in value:
        import capo_bedrock_data_automation.types.entity_details

        out["entity"] = (
            capo_bedrock_data_automation.types.entity_details.redact_sensitive(
                value["entity"]
            )
        )
    return out
