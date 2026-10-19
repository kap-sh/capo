"""Generated from Smithy shape ``com.amazonaws.customerprofiles#Batch``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.timestamp


class Batch(TypedDict, closed=True):
    start_time: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>Start time of batch to split ingestion.</p>"""
    end_time: "capo_customer_profiles.types.timestamp.timestamp"
    """<p>End time of batch to split ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Batch) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.timestamp

    out["StartTime"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["start_time"]
    )
    import capo_customer_profiles.types.timestamp

    out["EndTime"] = capo_customer_profiles.types.timestamp.serialize_json(
        value["end_time"]
    )
    return out


def deserialize_json(data: dict) -> Batch:
    out: Batch = {}  # type: ignore[typeddict-item]
    if data.get("StartTime") is not None:
        import capo_customer_profiles.types.timestamp

        out["start_time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["StartTime"]
        )
    else:
        import datetime

        out["start_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("EndTime") is not None:
        import capo_customer_profiles.types.timestamp

        out["end_time"] = capo_customer_profiles.types.timestamp.deserialize_json(
            data["EndTime"]
        )
    else:
        import datetime

        out["end_time"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
