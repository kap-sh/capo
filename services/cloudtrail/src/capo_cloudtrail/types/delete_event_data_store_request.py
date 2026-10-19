"""Generated from Smithy shape ``com.amazonaws.cloudtrail#DeleteEventDataStoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cloudtrail.types.event_data_store_arn


class DeleteEventDataStoreRequest(TypedDict, closed=True):
    event_data_store: "capo_cloudtrail.types.event_data_store_arn.EventDataStoreArn"
    """<p>The ARN (or the ID suffix of the ARN) of the event data store to delete.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteEventDataStoreRequest) -> dict:
    out: dict = {}
    out["EventDataStore"] = value["event_data_store"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteEventDataStoreRequest:
    out: DeleteEventDataStoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("EventDataStore") is not None:
        out["event_data_store"] = data["EventDataStore"]
    else:
        out["event_data_store"] = ""
    return out
