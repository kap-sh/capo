"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#AgreementApprovalProposer``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.aws_account_id
    import capo_marketplace_agreement.types.proposer_legal_name


class AgreementApprovalProposer(TypedDict, closed=True):
    account_id: "capo_marketplace_agreement.types.aws_account_id.AWSAccountId"
    """<p>The AWS account ID of the proposer.</p>"""
    legal_name: "capo_marketplace_agreement.types.proposer_legal_name.ProposerLegalName"
    """<p>The legal name of the proposer.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AgreementApprovalProposer) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["legalName"] = value["legal_name"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AgreementApprovalProposer:
    out: AgreementApprovalProposer = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("legalName") is not None:
        out["legal_name"] = data["legalName"]
    else:
        out["legal_name"] = ""
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AgreementApprovalProposer) -> dict:
    out: dict = {}
    out["accountId"] = value["account_id"]
    out["legalName"] = value["legal_name"]
    return out


def deserialize_cbor(data: dict) -> AgreementApprovalProposer:
    out: AgreementApprovalProposer = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("legalName") is not None:
        out["legal_name"] = data["legalName"]
    else:
        out["legal_name"] = ""
    return out
