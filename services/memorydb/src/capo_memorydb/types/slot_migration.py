"""Generated from Smithy shape ``com.amazonaws.memorydb#SlotMigration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_memorydb.types.double


class SlotMigration(TypedDict, closed=True):
    progress_percentage: "capo_memorydb.types.double.Double"
    """<p>The percentage of the slot migration that is complete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SlotMigration) -> dict:
    out: dict = {}
    out["ProgressPercentage"] = (
        "NaN"
        if value.get("progress_percentage", 0) != value.get("progress_percentage", 0)
        else "Infinity"
        if value.get("progress_percentage", 0) == float("inf")
        else "-Infinity"
        if value.get("progress_percentage", 0) == float("-inf")
        else value.get("progress_percentage", 0)
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> SlotMigration:
    out: SlotMigration = {}  # type: ignore[typeddict-item]
    if data.get("ProgressPercentage") is not None:
        out["progress_percentage"] = float(data["ProgressPercentage"])
    else:
        out["progress_percentage"] = 0
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SlotMigration) -> dict:
    out: dict = {}
    out["ProgressPercentage"] = value.get("progress_percentage", 0)
    return out


def deserialize_cbor(data: dict) -> SlotMigration:
    out: SlotMigration = {}  # type: ignore[typeddict-item]
    if data.get("ProgressPercentage") is not None:
        out["progress_percentage"] = float(data["ProgressPercentage"])
    else:
        out["progress_percentage"] = 0
    return out
