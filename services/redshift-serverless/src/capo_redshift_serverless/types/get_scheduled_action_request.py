"""Generated from Smithy shape ``com.amazonaws.redshiftserverless#GetScheduledActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_redshift_serverless.types.scheduled_action_name


class GetScheduledActionRequest(TypedDict, closed=True):
    scheduled_action_name: (
        "capo_redshift_serverless.types.scheduled_action_name.ScheduledActionName"
    )
    """<p>The name of the scheduled action.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetScheduledActionRequest) -> dict:
    out: dict = {}
    out["scheduledActionName"] = value["scheduled_action_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetScheduledActionRequest:
    out: GetScheduledActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("scheduledActionName") is not None:
        out["scheduled_action_name"] = data["scheduledActionName"]
    else:
        out["scheduled_action_name"] = ""
    return out
