"""Generated from Smithy shape ``com.amazonaws.connecthealth#DeleteDatasetOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connecthealth.types.dataset_arn
    import capo_connecthealth.types.dataset_id
    import capo_connecthealth.types.dataset_status


class DeleteDatasetOutput(TypedDict, closed=True):
    arn: "capo_connecthealth.types.dataset_arn.DatasetArn"
    """<p>The Amazon Resource Name (ARN) of the dataset.</p>"""
    dataset_id: "capo_connecthealth.types.dataset_id.DatasetId"
    """<p>The unique identifier of the dataset.</p>"""
    status: "capo_connecthealth.types.dataset_status.DatasetStatus"
    """<p>The status of the dataset. After Amazon Connect Health accepts the request, the status is DELETING.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDatasetOutput) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["datasetId"] = value["dataset_id"]
    import capo_connecthealth.types.dataset_status

    out["status"] = capo_connecthealth.types.dataset_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteDatasetOutput:
    out: DeleteDatasetOutput = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("datasetId") is not None:
        out["dataset_id"] = data["datasetId"]
    else:
        out["dataset_id"] = ""
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
    return out
