"""Generated from Smithy shape ``com.amazonaws.supplychain#DeleteDataLakeDatasetResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_supplychain.types.data_lake_dataset_name
    import capo_supplychain.types.data_lake_namespace_name
    import capo_supplychain.types.uuid


class DeleteDataLakeDatasetResponse(TypedDict, closed=True):
    instance_id: "capo_supplychain.types.uuid.UUID"
    """<p>The AWS Supply Chain instance identifier.</p>"""
    namespace: "capo_supplychain.types.data_lake_namespace_name.DataLakeNamespaceName"
    """<p>The namespace of deleted dataset.</p>"""
    name: "capo_supplychain.types.data_lake_dataset_name.DataLakeDatasetName"
    """<p>The name of deleted dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteDataLakeDatasetResponse) -> dict:
    out: dict = {}
    out["instanceId"] = value["instance_id"]
    out["namespace"] = value["namespace"]
    out["name"] = value["name"]
    return out


def deserialize_json(data: dict) -> DeleteDataLakeDatasetResponse:
    out: DeleteDataLakeDatasetResponse = {}  # type: ignore[typeddict-item]
    if data.get("instanceId") is not None:
        out["instance_id"] = data["instanceId"]
    else:
        out["instance_id"] = ""
    if data.get("namespace") is not None:
        out["namespace"] = data["namespace"]
    else:
        out["namespace"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    return out
