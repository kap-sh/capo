"""Generated from Smithy shape ``com.amazonaws.healthlake#DeleteFHIRDatastoreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.datastore_id


class DeleteFHIRDatastoreRequest(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """<p> The Amazon Web Services-generated identifier for the data store to be deleted.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DeleteFHIRDatastoreRequest) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DeleteFHIRDatastoreRequest:
    out: DeleteFHIRDatastoreRequest = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    return out
