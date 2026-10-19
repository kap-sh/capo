"""Generated from Smithy shape ``com.amazonaws.dataexchange#DeprecationRequestDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_dataexchange.types.timestamp


class DeprecationRequestDetails(TypedDict, closed=True):
    deprecation_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>A datetime in the future when the data set will be deprecated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeprecationRequestDetails) -> dict:
    out: dict = {}
    import capo_dataexchange.types.timestamp

    out["DeprecationAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["deprecation_at"]
    )
    return out


def deserialize_json(data: dict) -> DeprecationRequestDetails:
    out: DeprecationRequestDetails = {}  # type: ignore[typeddict-item]
    if data.get("DeprecationAt") is not None:
        import capo_dataexchange.types.timestamp

        out["deprecation_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["DeprecationAt"]
        )
    else:
        import datetime

        out["deprecation_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out
