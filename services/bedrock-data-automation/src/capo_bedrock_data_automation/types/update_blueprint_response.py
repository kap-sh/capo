"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#UpdateBlueprintResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_bedrock_data_automation.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint


class UpdateBlueprintResponse(TypedDict, closed=True):
    blueprint: "capo_bedrock_data_automation.types.blueprint.Blueprint"


# --- restJson1 ser/de ---
def serialize_json(value: UpdateBlueprintResponse) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.blueprint

    out["blueprint"] = capo_bedrock_data_automation.types.blueprint.serialize_json(
        value["blueprint"]
    )
    return out


def deserialize_json(data: dict) -> UpdateBlueprintResponse:
    out: UpdateBlueprintResponse = {}  # type: ignore[typeddict-item]
    if data.get("blueprint") is not None:
        import capo_bedrock_data_automation.types.blueprint

        out["blueprint"] = (
            capo_bedrock_data_automation.types.blueprint.deserialize_json(
                data["blueprint"]
            )
        )
    else:
        raise DeserializationError("UpdateBlueprintResponse.blueprint required")
    return out


def redact_sensitive(value: UpdateBlueprintResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blueprint" in value:
        import capo_bedrock_data_automation.types.blueprint

        out["blueprint"] = (
            capo_bedrock_data_automation.types.blueprint.redact_sensitive(
                value["blueprint"]
            )
        )
    return out
