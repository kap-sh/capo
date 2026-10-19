"""Generated from Smithy shape ``com.amazonaws.bedrockdataautomation#BlueprintSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_data_automation.types.blueprint_arn
    import capo_bedrock_data_automation.types.blueprint_name
    import capo_bedrock_data_automation.types.blueprint_stage
    import capo_bedrock_data_automation.types.blueprint_version
    import capo_bedrock_data_automation.types.date_timestamp


class BlueprintSummary(TypedDict, closed=True):
    blueprint_arn: "capo_bedrock_data_automation.types.blueprint_arn.BlueprintArn"
    blueprint_version: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_version.BlueprintVersion"
    ]
    blueprint_stage: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_stage.BlueprintStage"
    ]
    blueprint_name: NotRequired[
        "capo_bedrock_data_automation.types.blueprint_name.BlueprintName"
    ]
    creation_time: "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    last_modified_time: NotRequired[
        "capo_bedrock_data_automation.types.date_timestamp.DateTimestamp"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: BlueprintSummary) -> dict:
    out: dict = {}
    out["blueprintArn"] = value["blueprint_arn"]
    if "blueprint_version" in value:
        out["blueprintVersion"] = value["blueprint_version"]
    if "blueprint_stage" in value:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprintStage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.serialize_json(
                value["blueprint_stage"]
            )
        )
    if "blueprint_name" in value:
        out["blueprintName"] = value["blueprint_name"]
    import capo_bedrock_data_automation.types.date_timestamp

    out["creationTime"] = (
        capo_bedrock_data_automation.types.date_timestamp.serialize_json(
            value["creation_time"]
        )
    )
    if "last_modified_time" in value:
        import capo_bedrock_data_automation.types.date_timestamp

        out["lastModifiedTime"] = (
            capo_bedrock_data_automation.types.date_timestamp.serialize_json(
                value["last_modified_time"]
            )
        )
    return out


def deserialize_json(data: dict) -> BlueprintSummary:
    out: BlueprintSummary = {}  # type: ignore[typeddict-item]
    if data.get("blueprintArn") is not None:
        out["blueprint_arn"] = data["blueprintArn"]
    else:
        out["blueprint_arn"] = ""
    if data.get("blueprintVersion") is not None:
        out["blueprint_version"] = data["blueprintVersion"]
    if data.get("blueprintStage") is not None:
        import capo_bedrock_data_automation.types.blueprint_stage

        out["blueprint_stage"] = (
            capo_bedrock_data_automation.types.blueprint_stage.deserialize_json(
                data["blueprintStage"]
            )
        )
    if data.get("blueprintName") is not None:
        out["blueprint_name"] = data["blueprintName"]
    if data.get("creationTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["creation_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["creationTime"]
            )
        )
    else:
        import datetime

        out["creation_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("lastModifiedTime") is not None:
        import capo_bedrock_data_automation.types.date_timestamp

        out["last_modified_time"] = (
            capo_bedrock_data_automation.types.date_timestamp.deserialize_json(
                data["lastModifiedTime"]
            )
        )
    return out


def redact_sensitive(value: BlueprintSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "blueprint_name" in value:
        out["blueprint_name"] = "*** Sensitive Data Redacted ***"
    return out
