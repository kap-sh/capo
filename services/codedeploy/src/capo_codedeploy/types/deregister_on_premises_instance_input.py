"""Generated from Smithy shape ``com.amazonaws.codedeploy#DeregisterOnPremisesInstanceInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.instance_name


class DeregisterOnPremisesInstanceInput(TypedDict, closed=True):
    instance_name: "capo_codedeploy.types.instance_name.InstanceName"
    """<p>The name of the on-premises instance to deregister.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeregisterOnPremisesInstanceInput) -> dict:
    out: dict = {}
    out["instanceName"] = value["instance_name"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeregisterOnPremisesInstanceInput:
    out: DeregisterOnPremisesInstanceInput = {}  # type: ignore[typeddict-item]
    if data.get("instanceName") is not None:
        out["instance_name"] = data["instanceName"]
    else:
        out["instance_name"] = ""
    return out
