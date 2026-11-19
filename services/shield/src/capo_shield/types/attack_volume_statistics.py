"""Generated from Smithy shape ``com.amazonaws.shield#AttackVolumeStatistics``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_shield.types.double


class AttackVolumeStatistics(TypedDict, closed=True):
    max: "capo_shield.types.double.Double"
    """<p>The maximum attack volume observed for the given unit.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AttackVolumeStatistics) -> dict:
    out: dict = {}
    out["Max"] = (
        "NaN"
        if value.get("max", 0) != value.get("max", 0)
        else "Infinity"
        if value.get("max", 0) == float("inf")
        else "-Infinity"
        if value.get("max", 0) == float("-inf")
        else value.get("max", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> AttackVolumeStatistics:
    out: AttackVolumeStatistics = {}  # type: ignore[typeddict-item]
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    else:
        out["max"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AttackVolumeStatistics) -> dict:
    out: dict = {}
    out["Max"] = value.get("max", 0)
    return out


def deserialize_cbor(data: dict) -> AttackVolumeStatistics:
    out: AttackVolumeStatistics = {}  # type: ignore[typeddict-item]
    if data.get("Max") is not None:
        out["max"] = float(data["Max"])
    else:
        out["max"] = 0
    return out
