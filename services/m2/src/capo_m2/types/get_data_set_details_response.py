"""Generated from Smithy shape ``com.amazonaws.m2#GetDataSetDetailsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.dataset_detail_org_attributes
    import capo_m2.types.integer
    import capo_m2.types.string200
    import capo_m2.types.string2000
    import capo_m2.types.timestamp


class GetDataSetDetailsResponse(TypedDict, closed=True):
    data_set_name: "capo_m2.types.string200.String200"
    """<p>The name of the data set.</p>"""
    data_set_org: NotRequired[
        "capo_m2.types.dataset_detail_org_attributes.DatasetDetailOrgAttributes"
    ]
    """<p>The type of data set. The only supported value is VSAM.</p>"""
    record_length: NotRequired["capo_m2.types.integer.Integer"]
    """<p>The length of records in the data set.</p>"""
    location: NotRequired["capo_m2.types.string2000.String2000"]
    """<p>The location where the data set is stored.</p>"""
    blocksize: NotRequired["capo_m2.types.integer.Integer"]
    """<p>The size of the block on disk. </p>"""
    creation_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when the data set was created.</p>"""
    last_updated_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was updated.</p>"""
    last_referenced_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was referenced.</p>"""
    file_size: NotRequired["int"]
    """<p>File size of the dataset.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetDataSetDetailsResponse) -> dict:
    out: dict = {}
    out["dataSetName"] = value["data_set_name"]
    if "data_set_org" in value:
        import capo_m2.types.dataset_detail_org_attributes

        out["dataSetOrg"] = capo_m2.types.dataset_detail_org_attributes.serialize_json(
            value["data_set_org"]
        )
    if "record_length" in value:
        out["recordLength"] = value["record_length"]
    if "location" in value:
        out["location"] = value["location"]
    if "blocksize" in value:
        out["blocksize"] = value["blocksize"]
    if "creation_time" in value:
        import capo_m2.types.timestamp

        out["creationTime"] = capo_m2.types.timestamp.serialize_json(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_m2.types.timestamp

        out["lastUpdatedTime"] = capo_m2.types.timestamp.serialize_json(
            value["last_updated_time"]
        )
    if "last_referenced_time" in value:
        import capo_m2.types.timestamp

        out["lastReferencedTime"] = capo_m2.types.timestamp.serialize_json(
            value["last_referenced_time"]
        )
    if "file_size" in value:
        out["fileSize"] = value["file_size"]
    return out


def deserialize_json(data: dict) -> GetDataSetDetailsResponse:
    out: GetDataSetDetailsResponse = {}  # type: ignore[typeddict-item]
    if data.get("dataSetName") is not None:
        out["data_set_name"] = data["dataSetName"]
    else:
        out["data_set_name"] = ""
    if data.get("dataSetOrg") is not None:
        import capo_m2.types.dataset_detail_org_attributes

        out["data_set_org"] = (
            capo_m2.types.dataset_detail_org_attributes.deserialize_json(
                data["dataSetOrg"]
            )
        )
    if data.get("recordLength") is not None:
        out["record_length"] = data["recordLength"]
    if data.get("location") is not None:
        out["location"] = data["location"]
    if data.get("blocksize") is not None:
        out["blocksize"] = data["blocksize"]
    if data.get("creationTime") is not None:
        import capo_m2.types.timestamp

        out["creation_time"] = capo_m2.types.timestamp.deserialize_json(
            data["creationTime"]
        )
    if data.get("lastUpdatedTime") is not None:
        import capo_m2.types.timestamp

        out["last_updated_time"] = capo_m2.types.timestamp.deserialize_json(
            data["lastUpdatedTime"]
        )
    if data.get("lastReferencedTime") is not None:
        import capo_m2.types.timestamp

        out["last_referenced_time"] = capo_m2.types.timestamp.deserialize_json(
            data["lastReferencedTime"]
        )
    if data.get("fileSize") is not None:
        out["file_size"] = data["fileSize"]
    return out
