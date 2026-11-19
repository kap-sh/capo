"""Generated from Smithy shape ``com.amazonaws.codedeploy#TimeBasedCanary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.percentage
    import capo_codedeploy.types.wait_time_in_mins


class TimeBasedCanary(TypedDict, closed=True):
    canary_percentage: "capo_codedeploy.types.percentage.Percentage"
    """<p>The percentage of traffic to shift in the first increment of a <code>TimeBasedCanary</code> deployment.</p>"""
    canary_interval: "capo_codedeploy.types.wait_time_in_mins.WaitTimeInMins"
    """<p>The number of minutes between the first and second traffic shifts of a <code>TimeBasedCanary</code> deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeBasedCanary) -> dict:
    out: dict = {}
    out["canaryPercentage"] = value.get("canary_percentage", 0)
    out["canaryInterval"] = value.get("canary_interval", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeBasedCanary:
    out: TimeBasedCanary = {}  # type: ignore[typeddict-item]
    if data.get("canaryPercentage") is not None:
        out["canary_percentage"] = data["canaryPercentage"]
    else:
        out["canary_percentage"] = 0
    if data.get("canaryInterval") is not None:
        out["canary_interval"] = data["canaryInterval"]
    else:
        out["canary_interval"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TimeBasedCanary) -> dict:
    out: dict = {}
    out["canaryPercentage"] = value.get("canary_percentage", 0)
    out["canaryInterval"] = value.get("canary_interval", 0)
    return out


def deserialize_cbor(data: dict) -> TimeBasedCanary:
    out: TimeBasedCanary = {}  # type: ignore[typeddict-item]
    if data.get("canaryPercentage") is not None:
        out["canary_percentage"] = data["canaryPercentage"]
    else:
        out["canary_percentage"] = 0
    if data.get("canaryInterval") is not None:
        out["canary_interval"] = data["canaryInterval"]
    else:
        out["canary_interval"] = 0
    return out
