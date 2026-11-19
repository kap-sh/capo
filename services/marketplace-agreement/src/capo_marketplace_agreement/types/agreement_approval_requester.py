"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalRequester``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.aws_account_id


class AgreementApprovalRequester(TypedDict, closed=True):
    account_id: "capo_marketplace_agreement.types.aws_account_id.AWSAccountId"
    """<p>The AWS account ID of the requester, which is the buyer of the agreement request.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalRequester) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalRequester:
    out: AgreementApprovalRequester = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalRequester) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    return out


def deserialize_cbor(data: dict) -> AgreementApprovalRequester:
    out: AgreementApprovalRequester = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    return out
