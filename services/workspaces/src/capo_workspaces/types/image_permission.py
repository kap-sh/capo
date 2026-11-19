"""Generated from Smithy shape ``com.amazonaws.workspaces#ImagePermission``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces.types.aws_account


class ImagePermission(TypedDict, closed=True):
    shared_account_id: NotRequired["capo_workspaces.types.aws_account.AwsAccount"]
    """<p>The identifier of the Amazon Web Services account that an image has been shared with.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ImagePermission) -> dict:
    out: dict = {}
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ImagePermission:
    out: ImagePermission = {}  # type: ignore[typeddict-item]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ImagePermission) -> dict:
    out: dict = {}
    if "shared_account_id" in value:
        out["SharedAccountId"] = value["shared_account_id"]
    return out


def deserialize_cbor(data: dict) -> ImagePermission:
    out: ImagePermission = {}  # type: ignore[typeddict-item]
    if data.get("SharedAccountId") is not None:
        out["shared_account_id"] = data["SharedAccountId"]
    return out
