"""Generated from Smithy shape ``com.amazonaws.guardduty#MetadataRecord``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_guardduty.types.metadata_total_time_milliseconds


class MetadataRecord(TypedDict, closed=True):
    total_time_milliseconds: NotRequired[
        "capo_guardduty.types.metadata_total_time_milliseconds.MetadataTotalTimeMilliseconds"
    ]
    """<p>The total time that the investigation took, in milliseconds.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataRecord) -> dict:
    out: dict = {}
    if "total_time_milliseconds" in value:
        out["totalTimeMilliseconds"] = value["total_time_milliseconds"]
    return out


def deserialize_json(data: dict) -> MetadataRecord:
    out: MetadataRecord = {}  # type: ignore[typeddict-item]
    if data.get("totalTimeMilliseconds") is not None:
        out["total_time_milliseconds"] = data["totalTimeMilliseconds"]
    return out
