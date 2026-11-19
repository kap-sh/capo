"""Generated from Smithy shape ``com.amazonaws.snowball#GetSoftwareUpdatesResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_snowball.types.string


class GetSoftwareUpdatesResult(TypedDict, closed=True):
    updates_uri: NotRequired["capo_snowball.types.string.String"]
    """<p>The Amazon S3 presigned URL for the update file associated with the specified <code>JobId</code> value. The software update will be available for 2 days after this request is made. To access an update after the 2 days have passed, you'll have to make another call to <code>GetSoftwareUpdates</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetSoftwareUpdatesResult) -> dict:
    out: dict = {}
    if "updates_uri" in value:
        out["UpdatesURI"] = value["updates_uri"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetSoftwareUpdatesResult:
    out: GetSoftwareUpdatesResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdatesURI") is not None:
        out["updates_uri"] = data["UpdatesURI"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: GetSoftwareUpdatesResult) -> dict:
    out: dict = {}
    if "updates_uri" in value:
        out["UpdatesURI"] = value["updates_uri"]
    return out


def deserialize_cbor(data: dict) -> GetSoftwareUpdatesResult:
    out: GetSoftwareUpdatesResult = {}  # type: ignore[typeddict-item]
    if data.get("UpdatesURI") is not None:
        out["updates_uri"] = data["UpdatesURI"]
    return out
