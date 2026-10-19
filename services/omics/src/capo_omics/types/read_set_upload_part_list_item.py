"""Generated from Smithy shape ``com.amazonaws.omics#ReadSetUploadPartListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_omics.types.read_set_part_source


class ReadSetUploadPartListItem(TypedDict, closed=True):
    part_number: "int"
    """<p> The number identifying the part in an upload. </p>"""
    part_size: "int"
    """<p> The size of the the part in an upload. </p>"""
    part_source: "capo_omics.types.read_set_part_source.ReadSetPartSource"
    """<p> The origin of the part being direct uploaded. </p>"""
    checksum: "str"
    """<p> A unique identifier used to confirm that parts are being added to the correct upload. </p>"""
    creation_time: NotRequired["datetime.datetime"]
    """<p> The time stamp for when a direct upload was created. </p>"""
    last_updated_time: NotRequired["datetime.datetime"]
    """<p> The time stamp for the most recent update to an uploaded part. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ReadSetUploadPartListItem) -> dict:
    out: dict = {}
    out["partNumber"] = value["part_number"]
    out["partSize"] = value["part_size"]
    out["partSource"] = value["part_source"]
    out["checksum"] = value["checksum"]
    if "creation_time" in value:
        import capo_omics._protocol.serialize

        out["creationTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["creation_time"]
        )
    if "last_updated_time" in value:
        import capo_omics._protocol.serialize

        out["lastUpdatedTime"] = capo_omics._protocol.serialize.fmt_date_time(
            value["last_updated_time"]
        )
    return out


def deserialize_json(data: dict) -> ReadSetUploadPartListItem:
    out: ReadSetUploadPartListItem = {}  # type: ignore[typeddict-item]
    if data.get("partNumber") is not None:
        out["part_number"] = data["partNumber"]
    else:
        out["part_number"] = 0
    if data.get("partSize") is not None:
        out["part_size"] = data["partSize"]
    else:
        out["part_size"] = 0
    if data.get("partSource") is not None:
        out["part_source"] = data["partSource"]
    else:
        out["part_source"] = ""
    if data.get("checksum") is not None:
        out["checksum"] = data["checksum"]
    else:
        out["checksum"] = ""
    if data.get("creationTime") is not None:
        import datetime

        out["creation_time"] = datetime.datetime.fromisoformat(
            data["creationTime"].replace("Z", "+00:00")
        )
    if data.get("lastUpdatedTime") is not None:
        import datetime

        out["last_updated_time"] = datetime.datetime.fromisoformat(
            data["lastUpdatedTime"].replace("Z", "+00:00")
        )
    return out
