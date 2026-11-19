"""Generated from Smithy shape ``com.amazonaws.codedeploy#TimeBasedLinear``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.percentage
    import capo_codedeploy.types.wait_time_in_mins


class TimeBasedLinear(TypedDict, closed=True):
    linear_percentage: "capo_codedeploy.types.percentage.Percentage"
    """<p>The percentage of traffic that is shifted at the start of each increment of a <code>TimeBasedLinear</code> deployment.</p>"""
    linear_interval: "capo_codedeploy.types.wait_time_in_mins.WaitTimeInMins"
    """<p>The number of minutes between each incremental traffic shift of a <code>TimeBasedLinear</code> deployment.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TimeBasedLinear) -> dict:
    out: dict = {}
    out["linearPercentage"] = value.get("linear_percentage", 0)
    out["linearInterval"] = value.get("linear_interval", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> TimeBasedLinear:
    out: TimeBasedLinear = {}  # type: ignore[typeddict-item]
    if data.get("linearPercentage") is not None:
        out["linear_percentage"] = data["linearPercentage"]
    else:
        out["linear_percentage"] = 0
    if data.get("linearInterval") is not None:
        out["linear_interval"] = data["linearInterval"]
    else:
        out["linear_interval"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TimeBasedLinear) -> dict:
    out: dict = {}
    out["linearPercentage"] = value.get("linear_percentage", 0)
    out["linearInterval"] = value.get("linear_interval", 0)
    return out


def deserialize_cbor(data: dict) -> TimeBasedLinear:
    out: TimeBasedLinear = {}  # type: ignore[typeddict-item]
    if data.get("linearPercentage") is not None:
        out["linear_percentage"] = data["linearPercentage"]
    else:
        out["linear_percentage"] = 0
    if data.get("linearInterval") is not None:
        out["linear_interval"] = data["linearInterval"]
    else:
        out["linear_interval"] = 0
    return out
