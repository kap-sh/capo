"""Generated from Smithy shape ``com.amazonaws.dataexchange#JobEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_dataexchange.errors import DeserializationError

if TYPE_CHECKING:
    import capo_dataexchange.types.arn
    import capo_dataexchange.types.asset_configuration
    import capo_dataexchange.types.id
    import capo_dataexchange.types.list_of_job_error
    import capo_dataexchange.types.response_details
    import capo_dataexchange.types.state
    import capo_dataexchange.types.timestamp
    import capo_dataexchange.types.type


class JobEntry(TypedDict, closed=True):
    arn: "capo_dataexchange.types.arn.Arn"
    """<p>The ARN for the job.</p>"""
    asset_configuration: NotRequired[
        "capo_dataexchange.types.asset_configuration.AssetConfiguration"
    ]
    """<p>The configuration for the asset, including tags applied to assets created by the job.</p>"""
    created_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the job was created, in ISO 8601 format.</p>"""
    details: "capo_dataexchange.types.response_details.ResponseDetails"
    """<p>Details of the operation to be performed by the job, such as export destination details or import source details.</p>"""
    errors: NotRequired["capo_dataexchange.types.list_of_job_error.ListOfJobError"]
    """<p>Errors for jobs.</p>"""
    id: "capo_dataexchange.types.id.Id"
    """<p>The unique identifier for the job.</p>"""
    state: "capo_dataexchange.types.state.State"
    """<p>The state of the job.</p>"""
    type: "capo_dataexchange.types.type.Type"
    """<p>The job type.</p>"""
    updated_at: "capo_dataexchange.types.timestamp.Timestamp"
    """<p>The date and time that the job was last updated, in ISO 8601 format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: JobEntry) -> dict:
    out: dict = {}
    out["Arn"] = value["arn"]
    if "asset_configuration" in value:
        import capo_dataexchange.types.asset_configuration

        out["AssetConfiguration"] = (
            capo_dataexchange.types.asset_configuration.serialize_json(
                value["asset_configuration"]
            )
        )
    import capo_dataexchange.types.timestamp

    out["CreatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["created_at"]
    )
    import capo_dataexchange.types.response_details

    out["Details"] = capo_dataexchange.types.response_details.serialize_json(
        value["details"]
    )
    if "errors" in value:
        import capo_dataexchange.types.list_of_job_error

        out["Errors"] = capo_dataexchange.types.list_of_job_error.serialize_json(
            value["errors"]
        )
    out["Id"] = value["id"]
    out["State"] = value["state"]
    out["Type"] = value["type"]
    import capo_dataexchange.types.timestamp

    out["UpdatedAt"] = capo_dataexchange.types.timestamp.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> JobEntry:
    out: JobEntry = {}  # type: ignore[typeddict-item]
    if data.get("Arn") is not None:
        out["arn"] = data["Arn"]
    else:
        out["arn"] = ""
    if data.get("AssetConfiguration") is not None:
        import capo_dataexchange.types.asset_configuration

        out["asset_configuration"] = (
            capo_dataexchange.types.asset_configuration.deserialize_json(
                data["AssetConfiguration"]
            )
        )
    if data.get("CreatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["created_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["CreatedAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("Details") is not None:
        import capo_dataexchange.types.response_details

        out["details"] = capo_dataexchange.types.response_details.deserialize_json(
            data["Details"]
        )
    else:
        raise DeserializationError("JobEntry.details required")
    if data.get("Errors") is not None:
        import capo_dataexchange.types.list_of_job_error

        out["errors"] = capo_dataexchange.types.list_of_job_error.deserialize_json(
            data["Errors"]
        )
    if data.get("Id") is not None:
        out["id"] = data["Id"]
    else:
        out["id"] = ""
    if data.get("State") is not None:
        out["state"] = data["State"]
    else:
        out["state"] = ""
    if data.get("Type") is not None:
        out["type"] = data["Type"]
    else:
        out["type"] = ""
    if data.get("UpdatedAt") is not None:
        import capo_dataexchange.types.timestamp

        out["updated_at"] = capo_dataexchange.types.timestamp.deserialize_json(
            data["UpdatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
