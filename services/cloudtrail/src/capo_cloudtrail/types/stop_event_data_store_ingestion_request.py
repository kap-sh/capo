"""Generated from Smithy shape ``com.amazonaws.cloudtrail#StopEventDataStoreIngestionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_arn


class StopEventDataStoreIngestionRequest(TypedDict, closed=True):
    event_data_store: "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or ID suffix of the ARN) of the event data store for which you want to stop ingestion.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: StopEventDataStoreIngestionRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> StopEventDataStoreIngestionRequest:
    out: StopEventDataStoreIngestionRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    else:
        out["event_data_store"] = ""
    return out
