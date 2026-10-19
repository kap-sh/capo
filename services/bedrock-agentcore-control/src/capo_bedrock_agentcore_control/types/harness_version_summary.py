"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessVersionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.harness_arn
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_status
    import capo_bedrock_agentcore_control.types.harness_version


class HarnessVersionSummary(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness.</p>"""
    harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness.</p>"""
    arn: "capo_bedrock_agentcore_control.types.harness_arn.HarnessArn"
    """<p>The ARN of the harness.</p>"""
    harness_version: (
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    )
    """<p>The version of the harness that this summary describes.</p>"""
    status: "capo_bedrock_agentcore_control.types.harness_status.HarnessStatus"
    """<p>The status of this harness version.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this harness version was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when this harness version was last updated.</p>"""
    failure_reason: NotRequired["str"]
    """<p>Reason why the create or update operation for this harness version failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessVersionSummary) -> dict:
    out: dict = {}
    out["harnessId"] = value["harness_id"]
    out["harnessName"] = value["harness_name"]
    out["arn"] = value["arn"]
    out["harnessVersion"] = value["harness_version"]
    import capo_bedrock_agentcore_control.types.harness_status

    out["status"] = capo_bedrock_agentcore_control.types.harness_status.serialize_json(
        value["status"]
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["createdAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["created_at"]
        )
    )
    import capo_bedrock_agentcore_control.types.date_timestamp

    out["updatedAt"] = (
        capo_bedrock_agentcore_control.types.date_timestamp.serialize_json(
            value["updated_at"]
        )
    )
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> HarnessVersionSummary:
    out: HarnessVersionSummary = {}  # type: ignore[typeddict-item]
    if data.get("harnessId") is not None:
        out["harness_id"] = data["harnessId"]
    else:
        out["harness_id"] = ""
    if data.get("harnessName") is not None:
        out["harness_name"] = data["harnessName"]
    else:
        out["harness_name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("harnessVersion") is not None:
        out["harness_version"] = data["harnessVersion"]
    else:
        out["harness_version"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.harness_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.harness_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.harness_status.HarnessStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["created_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_bedrock_agentcore_control.types.date_timestamp

        out["updated_at"] = (
            capo_bedrock_agentcore_control.types.date_timestamp.deserialize_json(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
