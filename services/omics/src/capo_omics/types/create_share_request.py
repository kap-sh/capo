"""Generated from Smithy shape ``com.amazonaws.omics#CreateShareRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_omics.types.share_name


class CreateShareRequest(TypedDict, closed=True):
    resource_arn: "str"
    """<p>The ARN of the resource to be shared.</p>"""
    principal_subscriber: "str"
    """<p>The principal subscriber is the account being offered shared access to the resource. </p>"""
    share_name: NotRequired["capo_omics.types.share_name.ShareName"]
    """<p>A name that the owner defines for the share.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateShareRequest) -> dict:
    out: dict = {}
    out["resourceArn"] = value["resource_arn"]
    out["principalSubscriber"] = value["principal_subscriber"]
    if "share_name" in value:
        out["shareName"] = value["share_name"]
    return out


def deserialize_json(data: dict) -> CreateShareRequest:
    out: CreateShareRequest = {}  # type: ignore[typeddict-item]
    if data.get("resourceArn") is not None:
        out["resource_arn"] = data["resourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("principalSubscriber") is not None:
        out["principal_subscriber"] = data["principalSubscriber"]
    else:
        out["principal_subscriber"] = ""
    if data.get("shareName") is not None:
        out["share_name"] = data["shareName"]
    return out
