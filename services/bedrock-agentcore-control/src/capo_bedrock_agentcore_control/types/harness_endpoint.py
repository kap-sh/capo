"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#HarnessEndpoint``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.date_timestamp
    import capo_bedrock_agentcore_control.types.harness_endpoint_arn
    import capo_bedrock_agentcore_control.types.harness_endpoint_description
    import capo_bedrock_agentcore_control.types.harness_endpoint_name
    import capo_bedrock_agentcore_control.types.harness_endpoint_status
    import capo_bedrock_agentcore_control.types.harness_id
    import capo_bedrock_agentcore_control.types.harness_name
    import capo_bedrock_agentcore_control.types.harness_version


class HarnessEndpoint(TypedDict, closed=True):
    harness_id: "capo_bedrock_agentcore_control.types.harness_id.HarnessId"
    """<p>The ID of the harness that the endpoint belongs to.</p>"""
    harness_name: "capo_bedrock_agentcore_control.types.harness_name.HarnessName"
    """<p>The name of the harness that the endpoint belongs to.</p>"""
    endpoint_name: (
        "capo_bedrock_agentcore_control.types.harness_endpoint_name.HarnessEndpointName"
    )
    """<p>The name of the endpoint.</p>"""
    arn: "capo_bedrock_agentcore_control.types.harness_endpoint_arn.HarnessEndpointArn"
    """<p>The ARN of the endpoint.</p>"""
    status: "capo_bedrock_agentcore_control.types.harness_endpoint_status.HarnessEndpointStatus"
    """<p>The status of the endpoint.</p>"""
    created_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the endpoint was created.</p>"""
    updated_at: "capo_bedrock_agentcore_control.types.date_timestamp.DateTimestamp"
    """<p>The timestamp when the endpoint was last updated.</p>"""
    live_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>The harness version that the endpoint is currently serving.</p>"""
    target_version: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_version.HarnessVersion"
    ]
    """<p>The harness version that the endpoint points to. While an update is in progress, this can differ from the live version until the endpoint finishes transitioning.</p>"""
    description: NotRequired[
        "capo_bedrock_agentcore_control.types.harness_endpoint_description.HarnessEndpointDescription"
    ]
    """<p>The description of the endpoint.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason the endpoint's last create or update operation failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: HarnessEndpoint) -> dict:
    out: dict = {}
    out["harnessId"] = value["harness_id"]
    out["harnessName"] = value["harness_name"]
    out["endpointName"] = value["endpoint_name"]
    out["arn"] = value["arn"]
    import capo_bedrock_agentcore_control.types.harness_endpoint_status

    out["status"] = (
        capo_bedrock_agentcore_control.types.harness_endpoint_status.serialize_json(
            value["status"]
        )
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
    if "live_version" in value:
        out["liveVersion"] = value["live_version"]
    if "target_version" in value:
        out["targetVersion"] = value["target_version"]
    if "description" in value:
        out["description"] = value["description"]
    if "failure_reason" in value:
        out["failureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> HarnessEndpoint:
    out: HarnessEndpoint = {}  # type: ignore[typeddict-item]
    if data.get("harnessId") is not None:
        out["harness_id"] = data["harnessId"]
    else:
        out["harness_id"] = ""
    if data.get("harnessName") is not None:
        out["harness_name"] = data["harnessName"]
    else:
        out["harness_name"] = ""
    if data.get("endpointName") is not None:
        out["endpoint_name"] = data["endpointName"]
    else:
        out["endpoint_name"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("status") is not None:
        import capo_bedrock_agentcore_control.types.harness_endpoint_status

        out["status"] = (
            capo_bedrock_agentcore_control.types.harness_endpoint_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_bedrock_agentcore_control.types.harness_endpoint_status.HarnessEndpointStatus",
            "",
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
    if data.get("liveVersion") is not None:
        out["live_version"] = data["liveVersion"]
    if data.get("targetVersion") is not None:
        out["target_version"] = data["targetVersion"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("failureReason") is not None:
        out["failure_reason"] = data["failureReason"]
    return out
