"""Generated from Smithy shape ``com.amazonaws.m2#DataSet``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_m2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_m2.types.dataset_org_attributes
    import capo_m2.types.record_length


class DataSet(TypedDict, closed=True):
    storage_type: NotRequired["str"]
    """<p>The storage type of the data set: database or file system. For Micro Focus, database corresponds to datastore and file system corresponds to EFS/FSX. For Blu Age, there is no support of file system and database corresponds to Blusam. </p>"""
    dataset_name: "str"
    """<p>The logical identifier for a specific data set (in mainframe format).</p>"""
    dataset_org: "capo_m2.types.dataset_org_attributes.DatasetOrgAttributes"
    """<p>The type of dataset. The only supported value is VSAM.</p>"""
    relative_path: NotRequired["str"]
    """<p>The relative location of the data set in the database or file system. </p>"""
    record_length: "capo_m2.types.record_length.RecordLength"
    """<p>The length of a record.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSet) -> dict:
    out: dict = {}
    if "storage_type" in value:
        out["storageType"] = value["storage_type"]
    out["datasetName"] = value["dataset_name"]
    import capo_m2.types.dataset_org_attributes

    out["datasetOrg"] = capo_m2.types.dataset_org_attributes.serialize_json(
        value["dataset_org"]
    )
    if "relative_path" in value:
        out["relativePath"] = value["relative_path"]
    import capo_m2.types.record_length

    out["recordLength"] = capo_m2.types.record_length.serialize_json(
        value["record_length"]
    )
    return out


def deserialize_json(data: dict) -> DataSet:
    out: DataSet = {}  # type: ignore[typeddict-item]
    if data.get("storageType") is not None:
        out["storage_type"] = data["storageType"]
    if data.get("datasetName") is not None:
        out["dataset_name"] = data["datasetName"]
    else:
        out["dataset_name"] = ""
    if data.get("datasetOrg") is not None:
        import capo_m2.types.dataset_org_attributes

        out["dataset_org"] = capo_m2.types.dataset_org_attributes.deserialize_json(
            data["datasetOrg"]
        )
    else:
        out["dataset_org"] = {"$unknown": {"name": ""}}
    if data.get("relativePath") is not None:
        out["relative_path"] = data["relativePath"]
    if data.get("recordLength") is not None:
        import capo_m2.types.record_length

        out["record_length"] = capo_m2.types.record_length.deserialize_json(
            data["recordLength"]
        )
    else:
        raise DeserializationError("DataSet.record_length required")
    return out
