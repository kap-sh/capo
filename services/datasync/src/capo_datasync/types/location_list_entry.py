"""Generated from Smithy shape ``com.amazonaws.datasync#LocationListEntry``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datasync.types.location_arn
    import capo_datasync.types.location_uri


class LocationListEntry(TypedDict, closed=True):
    location_arn: NotRequired["capo_datasync.types.location_arn.LocationArn"]
    """<p>The Amazon Resource Name (ARN) of the location. For Network File System (NFS) or Amazon EFS, the location is the export path. For Amazon S3, the location is the prefix path that you want to mount and use as the root of the location.</p>"""
    location_uri: NotRequired["capo_datasync.types.location_uri.LocationUri"]
    """<p>Represents a list of URIs of a location. <code>LocationUri</code> returns an array that contains a list of locations when the <a href="https://docs.aws.amazon.com/datasync/latest/userguide/API_ListLocations.html">ListLocations</a> operation is called.</p> <p>Format: <code>TYPE://GLOBAL_ID/SUBDIR</code>.</p> <p>TYPE designates the type of location (for example, <code>nfs</code> or <code>s3</code>).</p> <p>GLOBAL_ID is the globally unique identifier of the resource that backs the location. An example for EFS is <code>us-east-2.fs-abcd1234</code>. An example for Amazon S3 is the bucket name, such as <code>myBucket</code>. An example for NFS is a valid IPv4 or IPv6 address or a hostname that is compliant with DNS.</p> <p>SUBDIR is a valid file system path, delimited by forward slashes as is the *nix convention. For NFS and Amazon EFS, it's the export path to mount the location. For Amazon S3, it's the prefix path that you mount to and treat as the root of the location.</p> <p></p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LocationListEntry) -> dict:
    out: dict = {}
    if "location_arn" in value:
        out["LocationArn"] = value["location_arn"]
    if "location_uri" in value:
        out["LocationUri"] = value["location_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LocationListEntry:
    out: LocationListEntry = {}  # type: ignore[typeddict-item]
    if data.get("LocationArn") is not None:
        out["location_arn"] = data["LocationArn"]
    if data.get("LocationUri") is not None:
        out["location_uri"] = data["LocationUri"]
    return out
