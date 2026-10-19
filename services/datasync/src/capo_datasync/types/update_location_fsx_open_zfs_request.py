"""Generated from Smithy shape ``com.amazonaws.datasync#UpdateLocationFsxOpenZfsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.fsx_protocol
    import capo_datasync.types.location_arn
    import capo_datasync.types.smb_subdirectory


class UpdateLocationFsxOpenZfsRequest(TypedDict, closed=True):
    location_arn: "capo_datasync.types.location_arn.LocationArn"
    """<p>Specifies the Amazon Resource Name (ARN) of the FSx for OpenZFS transfer location that you're updating.</p>"""
    protocol: NotRequired["capo_datasync.types.fsx_protocol.FsxProtocol"]
    subdirectory: NotRequired["capo_datasync.types.smb_subdirectory.SmbSubdirectory"]
    """<p>Specifies a subdirectory in the location's path that must begin with <code>/fsx</code>. DataSync uses this subdirectory to read or write data (depending on whether the file system is a source or destination location).</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateLocationFsxOpenZfsRequest) -> dict:
    out: dict = {}
    out["LocationArn"] = value["location_arn"]
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["Protocol"] = capo_datasync.types.fsx_protocol.serialize_aws_json_1_1(
            value["protocol"]
        )
    if "subdirectory" in value:
        out["Subdirectory"] = value["subdirectory"]
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateLocationFsxOpenZfsRequest:
    out: UpdateLocationFsxOpenZfsRequest = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    else:
        out["location_arn"] = ""
    if data.get("Protocol") is not None:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.deserialize_aws_json_1_1(
            data["Protocol"]
        )
    if data.get("Subdirectory") is not None:
        out["subdirectory"] = data["Subdirectory"]
    return out


def redact_sensitive(value: UpdateLocationFsxOpenZfsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "protocol" in value:
        import capo_datasync.types.fsx_protocol

        out["protocol"] = capo_datasync.types.fsx_protocol.redact_sensitive(
            value["protocol"]
        )
    return out
