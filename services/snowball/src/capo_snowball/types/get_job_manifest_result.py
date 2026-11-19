"""Generated from Smithy shape ``com.amazonaws.snowball#GetJobManifestResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class GetJobManifestResult(TypedDict, closed=True):
    manifest_uri: NotRequired["capo_snowball.types.string.String"]
    """<p>The Amazon S3 presigned URL for the manifest file associated with the specified <code>JobId</code> value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetJobManifestResult) -> dict:
    out: dict = {}
    if "manifest_uri" in value:
        out["ManifestURI"] = value["manifest_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetJobManifestResult:
    out: GetJobManifestResult = {}  # type: ignore[typeddict-item]
    if data.get("ManifestURI") is not None:
        out["manifest_uri"] = data["ManifestURI"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetJobManifestResult) -> dict:
    out: dict = {}
    if "manifest_uri" in value:
        out["ManifestURI"] = value["manifest_uri"]
    return out


def deserialize_cbor(data: dict) -> GetJobManifestResult:
    out: GetJobManifestResult = {}  # type: ignore[typeddict-item]
    if data.get("ManifestURI") is not None:
        out["manifest_uri"] = data["ManifestURI"]
    return out
