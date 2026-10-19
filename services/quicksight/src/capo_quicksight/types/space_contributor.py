"""Generated from Smithy shape ``com.amazonaws.quicksight#SpaceContributor``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_quicksight.types.double
    import capo_quicksight.types.long


class SpaceContributor(TypedDict, closed=True):
    user_name: NotRequired["str"]
    """<p>The user name of the contributor.</p>"""
    raw_file_size_bytes: "capo_quicksight.types.long.Long"
    """<p>The raw file size in bytes contributed by the user.</p>"""
    percentage: NotRequired["capo_quicksight.types.double.Double"]
    """<p>The percentage of total contributions made by the user.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SpaceContributor) -> dict:
    out: dict = {}
    if "user_name" in value:
        out["userName"] = value["user_name"]
    out["rawFileSizeBytes"] = value["raw_file_size_bytes"]
    if "percentage" in value:
        out["percentage"] = (
            "NaN"
            if value["percentage"] != value["percentage"]
            else "Infinity"
            if value["percentage"] == float("inf")
            else "-Infinity"
            if value["percentage"] == float("-inf")
            else value["percentage"]
        )
    return out


def deserialize_json(data: dict) -> SpaceContributor:
    out: SpaceContributor = {}  # type: ignore[typeddict-item]
    if data.get("userName") is not None:
        out["user_name"] = data["userName"]
    if data.get("rawFileSizeBytes") is not None:
        out["raw_file_size_bytes"] = data["rawFileSizeBytes"]
    else:
        out["raw_file_size_bytes"] = 0
    if data.get("percentage") is not None:
        out["percentage"] = float(data["percentage"])
    return out
