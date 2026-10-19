"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#ListBlueprintsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprints
    import capo_bedrock_data_automation.types.next_token


class ListBlueprintsResponse(TypedDict, closed=True):
    blueprints: "capo_bedrock_data_automation.types.blueprints.Blueprints"
    next_token: NotRequired["capo_bedrock_data_automation.types.next_token.NextToken"]


# --- restJson1 ser/de ---
def serialize_json(value: ListBlueprintsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_data_automation.types.blueprints

    out["blueprints"] = capo_bedrock_data_automation.types.blueprints.serialize_json(
        value["blueprints"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListBlueprintsResponse:
    out: ListBlueprintsResponse = {}  # type: ignore[typeddict-item]
    if data.get("blueprints") is not None:
        import capo_bedrock_data_automation.types.blueprints

        out["blueprints"] = (
            capo_bedrock_data_automation.types.blueprints.deserialize_json(
                data["blueprints"]
            )
        )
    else:
        out["blueprints"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListBlueprintsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blueprints" in value:
        import capo_bedrock_data_automation.types.blueprints

        out["blueprints"] = (
            capo_bedrock_data_automation.types.blueprints.redact_sensitive(
                value["blueprints"]
            )
        )
    return out
