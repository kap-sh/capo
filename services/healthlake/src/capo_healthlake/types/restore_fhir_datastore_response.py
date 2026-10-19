"""Generated from Smithy shape ``com.amazonaws.healthlake#RestoreFHIRDatastoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_healthlake.types.bounded_length_string
    import capo_healthlake.types.datastore_arn
    import capo_healthlake.types.datastore_id
    import capo_healthlake.types.datastore_status


class RestoreFHIRDatastoreResponse(TypedDict, closed=True):
    datastore_id: "capo_healthlake.types.datastore_id.DatastoreId"
    """The restored data store identifier."""
    datastore_arn: "capo_healthlake.types.datastore_arn.DatastoreArn"
    """The Amazon Resource Name (ARN) for the restored data store."""
    datastore_status: "capo_healthlake.types.datastore_status.DatastoreStatus"
    """The restored data store status."""
    datastore_endpoint: (
        "capo_healthlake.types.bounded_length_string.BoundedLengthString"
    )
    """The AWS endpoint for the restored data store."""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RestoreFHIRDatastoreResponse) -> dict:
    out: dict = {}
    out["DatastoreId"] = value["datastore_id"]
    out["DatastoreArn"] = value["datastore_arn"]
    import capo_healthlake.types.datastore_status

    out["DatastoreStatus"] = (
        capo_healthlake.types.datastore_status.serialize_aws_json_1_0(
            value["datastore_status"]
        )
    )
    out["DatastoreEndpoint"] = value["datastore_endpoint"]
    return out


def deserialize_aws_json_1_0(data: dict) -> RestoreFHIRDatastoreResponse:
    out: RestoreFHIRDatastoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("DatastoreId") is not None:
        out["datastore_id"] = data["DatastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("DatastoreArn") is not None:
        out["datastore_arn"] = data["DatastoreArn"]
    else:
        out["datastore_arn"] = ""
    if data.get("DatastoreStatus") is not None:
        import capo_healthlake.types.datastore_status

        out["datastore_status"] = (
            capo_healthlake.types.datastore_status.deserialize_aws_json_1_0(
                data["DatastoreStatus"]
            )
        )
    else:
        import typing

        out["datastore_status"] = typing.cast(
            "capo_healthlake.types.datastore_status.DatastoreStatus", ""
        )
    if data.get("DatastoreEndpoint") is not None:
        out["datastore_endpoint"] = data["DatastoreEndpoint"]
    else:
        out["datastore_endpoint"] = ""
    return out
