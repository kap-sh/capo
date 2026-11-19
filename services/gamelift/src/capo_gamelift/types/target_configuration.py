"""Generated from Smithy shape ``com.amazonaws.gamelift#TargetConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.double


class TargetConfiguration(TypedDict, closed=True):
    target_value: NotRequired["capo_gamelift.types.double.Double"]
    """<p>Desired value to use with a target-based scaling policy. The value must be relevant for whatever metric the scaling policy is using. For example, in a policy using the metric PercentAvailableGameSessions, the target value should be the preferred size of the fleet's buffer (the percent of capacity that should be idle and ready for new game sessions).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetConfiguration) -> dict:
    out: dict = {}
    if "target_value" in value:
        out["TargetValue"] = (
            "NaN"
            if value["target_value"] != value["target_value"]
            else "Infinity"
            if value["target_value"] == float("inf")
            else "-Infinity"
            if value["target_value"] == float("-inf")
            else value["target_value"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetConfiguration:
    out: TargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetConfiguration) -> dict:
    out: dict = {}
    if "target_value" in value:
        out["TargetValue"] = value["target_value"]
    return out


def deserialize_cbor(data: dict) -> TargetConfiguration:
    out: TargetConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    return out
