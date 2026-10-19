"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#EcsUngraceful``."""

from typing_extensions import TypedDict


class EcsUngraceful(TypedDict, closed=True):
    minimum_success_percentage: "int"
    """<p>The minimum success percentage specified for the configuration.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EcsUngraceful) -> dict:
    out: dict = {}
    out["minimumSuccessPercentage"] = value["minimum_success_percentage"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EcsUngraceful:
    out: EcsUngraceful = {}  # type: ignore[typeddict-item]
    if data.get("minimumSuccessPercentage") is not None:
        out["minimum_success_percentage"] = data["minimumSuccessPercentage"]
    else:
        out["minimum_success_percentage"] = 0
    return out
