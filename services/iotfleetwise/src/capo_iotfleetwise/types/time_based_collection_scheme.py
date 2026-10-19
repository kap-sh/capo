"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#TimeBasedCollectionScheme``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_iotfleetwise.types.collection_period_ms


class TimeBasedCollectionScheme(TypedDict, closed=True):
    period_ms: "capo_iotfleetwise.types.collection_period_ms.collectionPeriodMs"
    """<p>The time period (in milliseconds) to decide how often to collect data. For example, if the time period is <code>60000</code>, the Edge Agent software collects data once every minute.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TimeBasedCollectionScheme) -> dict:
    out: dict = {}
    out["periodMs"] = value["period_ms"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TimeBasedCollectionScheme:
    out: TimeBasedCollectionScheme = {}  # type: ignore[typeddict-item]
    if data.get("periodMs") is not None:
        out["period_ms"] = data["periodMs"]
    else:
        out["period_ms"] = 0
    return out
