"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterManagedInstanceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.managed_instance_id


class DeregisterManagedInstanceRequest(TypedDict, closed=True):
    instance_id: "capo_ssm.types.managed_instance_id.ManagedInstanceId"
    """<p>The ID assigned to the managed node when you registered it using the activation process. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterManagedInstanceRequest) -> dict:
    out: dict = {}
    out["InstanceId"] = value["instance_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterManagedInstanceRequest:
    out: DeregisterManagedInstanceRequest = {}  # type: ignore[typeddict-item]
    if data.get("InstanceId") is not None:
        out["instance_id"] = data["InstanceId"]
    else:
        out["instance_id"] = ""
    return out
