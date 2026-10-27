"""Generated from Smithy shape ``com.amazonaws.billing#CancelContractualInvestmentAttestationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_billing.types.arn_string
    import capo_billing.types.cancellation_reason
    import capo_billing.types.identifier_string


class CancelContractualInvestmentAttestationRequest(TypedDict, closed=True):
    attestation_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment attestation to cancel.</p>"""
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the contract that contains the attested investment.</p>"""
    reason: "capo_billing.types.cancellation_reason.CancellationReason"
    """<p>The reason for the cancellation. This value can be 1 to 80 characters.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: CancelContractualInvestmentAttestationRequest,
) -> dict:
    out: dict = {}
    out["attestationId"] = value["attestation_id"]
    out["contractArn"] = value["contract_arn"]
    out["reason"] = value["reason"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> CancelContractualInvestmentAttestationRequest:
    out: CancelContractualInvestmentAttestationRequest = {}  # type: ignore[typeddict-item]
    if data.get("attestationId") is not None:
        out["attestation_id"] = data["attestationId"]
    else:
        out["attestation_id"] = ""
    if data.get("contractArn") is not None:
        out["contract_arn"] = data["contractArn"]
    else:
        out["contract_arn"] = ""
    if data.get("reason") is not None:
        out["reason"] = data["reason"]
    else:
        out["reason"] = ""
    return out
