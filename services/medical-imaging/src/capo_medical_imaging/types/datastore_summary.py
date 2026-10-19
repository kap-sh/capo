"""Generated from Smithy shape ``com.amazonaws.medicalimaging#DatastoreSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_medical_imaging.types.arn
    import capo_medical_imaging.types.datastore_id
    import capo_medical_imaging.types.datastore_name
    import capo_medical_imaging.types.datastore_status
    import capo_medical_imaging.types.date


class DatastoreSummary(TypedDict, closed=True):
    datastore_id: "capo_medical_imaging.types.datastore_id.DatastoreId"
    """<p>The data store identifier.</p>"""
    datastore_name: "capo_medical_imaging.types.datastore_name.DatastoreName"
    """<p>The data store name.</p>"""
    datastore_status: "capo_medical_imaging.types.datastore_status.DatastoreStatus"
    """<p>The data store status.</p>"""
    datastore_arn: NotRequired["capo_medical_imaging.types.arn.Arn"]
    """<p>The Amazon Resource Name (ARN) for the data store.</p>"""
    created_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was created.</p>"""
    updated_at: NotRequired["capo_medical_imaging.types.date.Date"]
    """<p>The timestamp when the data store was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DatastoreSummary) -> dict:
    out: dict = {}
    out["datastoreId"] = value["datastore_id"]
    out["datastoreName"] = value["datastore_name"]
    import capo_medical_imaging.types.datastore_status

    out["datastoreStatus"] = capo_medical_imaging.types.datastore_status.serialize_json(
        value["datastore_status"]
    )
    if "datastore_arn" in value:
        out["datastoreArn"] = value["datastore_arn"]
    if "created_at" in value:
        import capo_medical_imaging.types.date

        out["createdAt"] = capo_medical_imaging.types.date.serialize_json(
            value["created_at"]
        )
    if "updated_at" in value:
        import capo_medical_imaging.types.date

        out["updatedAt"] = capo_medical_imaging.types.date.serialize_json(
            value["updated_at"]
        )
    return out


def deserialize_json(data: dict) -> DatastoreSummary:
    out: DatastoreSummary = {}  # type: ignore[typeddict-item]
    if data.get("datastoreId") is not None:
        out["datastore_id"] = data["datastoreId"]
    else:
        out["datastore_id"] = ""
    if data.get("datastoreName") is not None:
        out["datastore_name"] = data["datastoreName"]
    else:
        out["datastore_name"] = ""
    if data.get("datastoreStatus") is not None:
        import capo_medical_imaging.types.datastore_status

        out["datastore_status"] = (
            capo_medical_imaging.types.datastore_status.deserialize_json(
                data["datastoreStatus"]
            )
        )
    else:
        import typing

        out["datastore_status"] = typing.cast(
            "capo_medical_imaging.types.datastore_status.DatastoreStatus", ""
        )
    if data.get("datastoreArn") is not None:
        out["datastore_arn"] = data["datastoreArn"]
    if data.get("createdAt") is not None:
        import capo_medical_imaging.types.date

        out["created_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["createdAt"]
        )
    if data.get("updatedAt") is not None:
        import capo_medical_imaging.types.date

        out["updated_at"] = capo_medical_imaging.types.date.deserialize_json(
            data["updatedAt"]
        )
    return out
