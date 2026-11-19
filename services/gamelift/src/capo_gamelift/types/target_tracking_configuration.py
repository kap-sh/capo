"""Generated from Smithy shape ``com.amazonaws.gamelift#TargetTrackingConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_gamelift.types.non_negative_double


class TargetTrackingConfiguration(TypedDict, closed=True):
    target_value: NotRequired[
        "capo_gamelift.types.non_negative_double.NonNegativeDouble"
    ]
    """<p>Desired value to use with a game server group target-based scaling policy. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetTrackingConfiguration) -> dict:
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


def deserialize_aws_json_1_1(data: dict) -> TargetTrackingConfiguration:
    out: TargetTrackingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetTrackingConfiguration) -> dict:
    out: dict = {}
    if "target_value" in value:
        out["TargetValue"] = value["target_value"]
    return out


def deserialize_cbor(data: dict) -> TargetTrackingConfiguration:
    out: TargetTrackingConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("TargetValue") is not None:
        out["target_value"] = float(data["TargetValue"])
    return out
