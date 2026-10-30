"""Generated from Smithy shape ``com.amazonaws.ivs#InsertAdBreakResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.ad_break_id
    import capo_ivs.types.time


class InsertAdBreakResponse(TypedDict, closed=True):
    ad_break_id: NotRequired["capo_ivs.types.ad_break_id.AdBreakId"]
    """<p>Unique identifier for the ad break that was inserted into the playlist.</p>"""
    target_start_at: NotRequired["capo_ivs.types.time.Time"]
    """<p>Target start time for the inserted ad break.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InsertAdBreakResponse) -> dict:
    out: dict = {}
    if "ad_break_id" in value:
        out["adBreakId"] = value["ad_break_id"]
    if "target_start_at" in value:
        import capo_ivs.types.time

        out["targetStartAt"] = capo_ivs.types.time.serialize_json(
            value["target_start_at"]
        )
    return out


def deserialize_json(data: dict) -> InsertAdBreakResponse:
    out: InsertAdBreakResponse = {}  # type: ignore[typeddict-item]
    if data.get("adBreakId") is not None:
        out["ad_break_id"] = data["adBreakId"]
    if data.get("targetStartAt") is not None:
        import capo_ivs.types.time

        out["target_start_at"] = capo_ivs.types.time.deserialize_json(
            data["targetStartAt"]
        )
    return out
