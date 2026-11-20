"""Generated from Smithy shape ``com.amazonaws.partnercentralmarketing#FileRef``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_marketing.types.s3_uri
    import capo_partnercentral_marketing.types.s3_version_id


class FileRef(TypedDict, closed=True):
    s3_uri: "capo_partnercentral_marketing.types.s3_uri.S3Uri"
    """The `s3://` location of the file."""
    version_id: "capo_partnercentral_marketing.types.s3_version_id.S3VersionId"
    """The version of the object to take: the `VersionId` the staging upload returned."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: FileRef) -> dict:
    out: dict = {}
    out["S3Uri"] = value["s3_uri"]
    out["VersionId"] = value["version_id"]
    return out


def deserialize_cbor(data: dict) -> FileRef:
    out: FileRef = {}  # type: ignore[typeddict-item]
    if data.get("S3Uri") is not None:
        out["s3_uri"] = data["S3Uri"]
    else:
        out["s3_uri"] = ""
    if data.get("VersionId") is not None:
        out["version_id"] = data["VersionId"]
    else:
        out["version_id"] = ""
    return out
