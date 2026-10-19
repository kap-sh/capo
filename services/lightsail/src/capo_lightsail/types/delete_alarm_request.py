"""Generated from Smithy shape ``com.amazonaws.lightsail#DeleteAlarmRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.resource_name


class DeleteAlarmRequest(TypedDict, closed=True):
    alarm_name: "capo_lightsail.types.resource_name.ResourceName"
    """<p>The name of the alarm to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteAlarmRequest) -> dict:
    out: dict = {}
    out["alarmName"] = value["alarm_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteAlarmRequest:
    out: DeleteAlarmRequest = {}  # type: ignore[typeddict-item]
    if data.get("alarmName") is not None:
        out["alarm_name"] = data["alarmName"]
    else:
        out["alarm_name"] = ""
    return out
