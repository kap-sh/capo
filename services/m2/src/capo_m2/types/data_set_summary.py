"""Generated from Smithy shape ``com.amazonaws.m2#DataSetSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_m2.types.string20
    import capo_m2.types.string200
    import capo_m2.types.timestamp


class DataSetSummary(TypedDict, closed=True):
    data_set_name: "capo_m2.types.string200.String200"
    """<p>The name of the data set.</p>"""
    data_set_org: NotRequired["capo_m2.types.string20.String20"]
    """<p>The type of data set. The only supported value is VSAM.</p>"""
    format: NotRequired["capo_m2.types.string20.String20"]
    """<p>The format of the data set. </p>"""
    creation_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The timestamp when the data set was created.</p>"""
    last_updated_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was updated.</p>"""
    last_referenced_time: NotRequired["capo_m2.types.timestamp.Timestamp"]
    """<p>The last time the data set was referenced.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DataSetSummary) -> dict:
    out: dict = {}
    out["dataSetName"] = value["data_set_name"]
    if "data_set_org" in value:
        out["dataSetOrg"] = value["data_set_org"]
    if "format" in value:
        out["format"] = value["format"]
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
    return out


def deserialize_json(data: dict) -> DataSetSummary:
    out: DataSetSummary = {}  # type: ignore[typeddict-item]
    if data.get("dataSetName") is not None:
        out["data_set_name"] = data["dataSetName"]
    else:
        out["data_set_name"] = ""
    if data.get("dataSetOrg") is not None:
        out["data_set_org"] = data["dataSetOrg"]
    if data.get("format") is not None:
        out["format"] = data["format"]
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
    return out
