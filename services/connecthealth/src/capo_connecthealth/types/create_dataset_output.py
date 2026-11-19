"""Generated from Smithy shape ``com.amazonaws.connecthealth#CreateDatasetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_connecthealth.types.dataset_arn
    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.dataset_status
    import capo_connecthealth.types.dataset_type


class CreateDatasetOutput(TypedDict, closed=True):
    arn: "capo_connecthealth.types.dataset_arn.DatasetArn"
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_id: "capo_connecthealth.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    type: "capo_connecthealth.types.dataset_type.DatasetType"
    """<p>The type of the dataset, determined by the configuration that you provided.</p>"""
    status: "capo_connecthealth.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. A new dataset has the status CREATING.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time that the dataset was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateDatasetOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["datasetId"] = value["dataset_id"]
    import capo_connecthealth.types.dataset_type

    out["type"] = capo_connecthealth.types.dataset_type.serialize_json(value["type"])
    import capo_connecthealth.types.dataset_status

    out["status"] = capo_connecthealth.types.dataset_status.serialize_json(
        value["status"]
    )
    import capo_connecthealth.types._prelude.timestamp

    out["createdAt"] = capo_connecthealth.types._prelude.timestamp.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> CreateDatasetOutput:
    out: CreateDatasetOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
    if data.get("type") is not None:
        import capo_connecthealth.types.dataset_type

        out["type"] = capo_connecthealth.types.dataset_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_connecthealth.types.dataset_type.DatasetType", ""
        )
    if data.get("status") is not None:
        import capo_connecthealth.types.dataset_status

        out["status"] = capo_connecthealth.types.dataset_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_connecthealth.types.dataset_status.DatasetStatus", ""
        )
    if data.get("createdAt") is not None:
        import capo_connecthealth.types._prelude.timestamp

        out["created_at"] = (
            capo_connecthealth.types._prelude.timestamp.deserialize_json(
                data["createdAt"]
            )
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
