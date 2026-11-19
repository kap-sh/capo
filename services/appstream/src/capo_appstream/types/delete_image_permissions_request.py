"""Generated from Smithy shape ``com.amazonaws.appstream#DeleteImagePermissionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.aws_account_id
    import capo_appstream.types.name


class DeleteImagePermissionsRequest(TypedDict, closed=True):
    name: NotRequired["capo_appstream.types.name.Name"]
    """<p>The name of the private image.</p>"""
    shared_account_id: NotRequired["capo_appstream.types.aws_account_id.AwsAccountId"]
    """<p>The 12-digit identifier of the AWS account for which to delete image permissions.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteImagePermissionsRequest:
    out: DeleteImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DeleteImagePermissionsRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["Name"] = value["name"]
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_cbor(data: dict) -> DeleteImagePermissionsRequest:
    out: DeleteImagePermissionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    return out
