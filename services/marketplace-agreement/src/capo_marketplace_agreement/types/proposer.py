"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#Proposer``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.aws_account_id


class Proposer(TypedDict, closed=True):
    account_id: NotRequired[
        "capo_marketplace_agreement.types.aws_account_id.AWSAccountId"
    ]
    """<p>The AWS account ID of the proposer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Proposer) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> Proposer:
    out: Proposer = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Proposer) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    return out


def deserialize_cbor(data: dict) -> Proposer:
    out: Proposer = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    return out
