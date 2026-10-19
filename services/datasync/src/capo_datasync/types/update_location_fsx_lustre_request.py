"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationFsxLustreRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.location_arn
    import capo_datasync.types.smb_subdirectory


class UpdateLocationFsxLustreRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the FSx for Lustre transfer location that you're updating.</p>"""
    subdirectory: NotRequired["capo_datasync.types.smb_subdirectory.SmbSubdirectory"]
    """<p>Specifies a mount path for your FSx for Lustre file system. The path can include subdirectories.</p> <p>When the location is used as a source, DataSync reads data from the mount path. When the location is used as a destination, DataSync writes data to the mount path. If you don't include this parameter, DataSync uses the file system's root directory (<code>/</code>).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationFsxLustreRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationFsxLustreRequest:
    out: UpdateLocationFsxLustreRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        out["location_arn"] = ""
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    return out
