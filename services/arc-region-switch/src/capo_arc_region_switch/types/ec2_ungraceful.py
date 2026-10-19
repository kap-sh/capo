"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#Ec2Ungraceful``."""

from typing_extensions import TypedDict


class Ec2Ungraceful(TypedDict, closed=True):
    minimum_success_percentage: "int"
    """<p>The minimum success percentage that you specify for EC2 Auto Scaling groups.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Ec2Ungraceful) -> dict:
    out: dict = {}
    out["minimumSuccessPercentage"] = value["minimum_success_percentage"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Ec2Ungraceful:
    out: Ec2Ungraceful = {}  # type: ignore[typeddict-item]
    if data.get("minimumSuccessPercentage") is not None:
        out["minimum_success_percentage"] = data["minimumSuccessPercentage"]
    else:
        out["minimum_success_percentage"] = 0
    return out
