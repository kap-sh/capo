"""Generated from Smithy shape ``com.amazonaws.billing#AssociateContractRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.arn_string
    import capo_billing.types.contract_document_id


class AssociateContractRequest(TypedDict, closed=True):
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the contract to associate with your account.</p>"""
    contract_document_id: "capo_billing.types.contract_document_id.ContractDocumentId"
    """<p>The contract ID from the contract document. It can be found in the top right corner of your contract's pages. This value confirms that you have access to the contract you are associating.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateContractRequest) -> dict:
    out: dict = {}
    out["contractArn"] = value["contract_arn"]
    out["contractDocumentId"] = value["contract_document_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociateContractRequest:
    out: AssociateContractRequest = {}  # type: ignore[typeddict-item]
    if data.get("contractArn") is not None:
        out["contract_arn"] = data["contractArn"]
    else:
        out["contract_arn"] = ""
    if data.get("contractDocumentId") is not None:
        out["contract_document_id"] = data["contractDocumentId"]
    else:
        out["contract_document_id"] = ""
    return out


def redact_sensitive(value: AssociateContractRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contract_document_id" in value:
        out["contract_document_id"] = "*** Sensitive Data Redacted ***"
    return out
