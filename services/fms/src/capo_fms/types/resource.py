"""Generated from Smithy shape ``com.amazonaws.fms#Resource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.aws_account_id
    import capo_fms.types.identifier


class Resource(TypedDict, closed=True):
    uri: "capo_fms.types.identifier.Identifier"
    """<p>The resource's universal resource indicator (URI).</p>"""
    account_id: NotRequired["capo_fms.types.aws_account_id.AWSAccountId"]
    """<p>The Amazon Web Services account ID that the associated resource belongs to.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Resource) -> dict:
    out: dict = {}
    out["URI"] = value["uri"]
    if "account_id" in value:
        out["AccountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> Resource:
    out: Resource = {}  # type: ignore[typeddict-item]
    if data.get("URI") is not None:
        out["uri"] = data["URI"]
    else:
        out["uri"] = ""
    if data.get("AccountId") is not None:
        out["account_id"] = data["AccountId"]
    return out
