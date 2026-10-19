"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.harness_arn
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_status
    import capo_bedrock_agentcore_control.types.harness_version


class HarnessSummary(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness.</p>"""
    harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness.</p>"""
    arn: "capo_bedrock_agentcore_control.types.harness_arn.HarnessArn"
    """<p>The ARN of the harness.</p>"""
    status: "capo_bedrock_agentcore_control.types.harness_status.HarnessStatus"
    """<p>The current status of the harness.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the harness was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the harness was last updated.</p>"""
    harness_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>The latest version of the harness.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessSummary) -> dict:
    out: dict = {}
    out["harnessId"] = value["harness_id"]
    out["harnessName"] = value["harness_name"]
    out["arn"] = value["arn"]
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
    if "harness_version" in value:
        out["harnessVersion"] = value["harness_version"]
    return out


def deserialize_json(data: dict) -> HarnessSummary:
    out: HarnessSummary = {}  # type: ignore[typeddict-item]
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
    if data.get("harnessVersion") is not None:
        out["harness_version"] = data["harnessVersion"]
    return out
