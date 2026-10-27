"""Generated from Smithy shape ``com.amazonaws.billing#CreateContractualInvestmentAttestationRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.additional_recipients
    import capo_billing.types.approver_details
    import capo_billing.types.arn_string
    import capo_billing.types.attestation_client_token
    import capo_billing.types.attestation_details
    import capo_billing.types.contract_document_id
    import capo_billing.types.identifier_string


class CreateContractualInvestmentAttestationRequest(TypedDict, closed=True):
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the contract that contains the investment being attested.</p>"""
    investment_summary_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment summary being attested. This is the parent to the investmentId.</p>"""
    investment_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment (outcome) being attested.</p>"""
    contract_document_id: "capo_billing.types.contract_document_id.ContractDocumentId"
    """<p>The contract ID from the contract document, located in the top-right corner of the private pricing contract pages. This value confirms that you have access to the contract.</p>"""
    approver_details: "capo_billing.types.approver_details.ApproverDetails"
    """<p>The details of the executive who authorized the attestation, under the terms of the private pricing contract. The executive receives a click-to-accept email to confirm the attestation.</p>"""
    investment_disbursed_at: NotRequired["datetime.datetime"]
    """<p>The date on which the investment is disbursed to the investment accounts. The disbursement date is subject to review timelines.</p>"""
    attestation_details: "capo_billing.types.attestation_details.AttestationDetails"
    """<p>The details of the attestation, including the value being claimed and how the resulting investment is distributed across investment accounts.</p>"""
    additional_recipients: NotRequired[
        "capo_billing.types.additional_recipients.AdditionalRecipients"
    ]
    """<p>The email addresses to copy as viewers on the executive approval request.</p>"""
    client_token: NotRequired[
        "capo_billing.types.attestation_client_token.AttestationClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If you retry a request that completed successfully using the same client token and parameters, the retry completes without performing any further actions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(
    value: CreateContractualInvestmentAttestationRequest,
) -> dict:
    out: dict = {}
    out["contractArn"] = value["contract_arn"]
    out["investmentSummaryId"] = value["investment_summary_id"]
    out["investmentId"] = value["investment_id"]
    out["contractDocumentId"] = value["contract_document_id"]
    import capo_billing.types.approver_details

    out["approverDetails"] = capo_billing.types.approver_details.serialize_aws_json_1_0(
        value["approver_details"]
    )
    if "investment_disbursed_at" in value:
        import capo_billing.types._prelude.timestamp

        out["investmentDisbursedAt"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["investment_disbursed_at"]
            )
        )
    import capo_billing.types.attestation_details

    out["attestationDetails"] = (
        capo_billing.types.attestation_details.serialize_aws_json_1_0(
            value["attestation_details"]
        )
    )
    if "additional_recipients" in value:
        import capo_billing.types.additional_recipients

        out["additionalRecipients"] = (
            capo_billing.types.additional_recipients.serialize_aws_json_1_0(
                value["additional_recipients"]
            )
        )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(
    data: dict,
) -> CreateContractualInvestmentAttestationRequest:
    out: CreateContractualInvestmentAttestationRequest = {}  # type: ignore[typeddict-item]
    if data.get("contractArn") is not None:
        out["contract_arn"] = data["contractArn"]
    else:
        out["contract_arn"] = ""
    if data.get("investmentSummaryId") is not None:
        out["investment_summary_id"] = data["investmentSummaryId"]
    else:
        out["investment_summary_id"] = ""
    if data.get("investmentId") is not None:
        out["investment_id"] = data["investmentId"]
    else:
        out["investment_id"] = ""
    if data.get("contractDocumentId") is not None:
        out["contract_document_id"] = data["contractDocumentId"]
    else:
        out["contract_document_id"] = ""
    if data.get("approverDetails") is not None:
        import capo_billing.types.approver_details

        out["approver_details"] = (
            capo_billing.types.approver_details.deserialize_aws_json_1_0(
                data["approverDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContractualInvestmentAttestationRequest.approver_details required"
        )
    if data.get("investmentDisbursedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["investment_disbursed_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["investmentDisbursedAt"]
            )
        )
    if data.get("attestationDetails") is not None:
        import capo_billing.types.attestation_details

        out["attestation_details"] = (
            capo_billing.types.attestation_details.deserialize_aws_json_1_0(
                data["attestationDetails"]
            )
        )
    else:
        raise DeserializationError(
            "CreateContractualInvestmentAttestationRequest.attestation_details required"
        )
    if data.get("additionalRecipients") is not None:
        import capo_billing.types.additional_recipients

        out["additional_recipients"] = (
            capo_billing.types.additional_recipients.deserialize_aws_json_1_0(
                data["additionalRecipients"]
            )
        )
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out


def redact_sensitive(
    value: CreateContractualInvestmentAttestationRequest,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "contract_document_id" in value:
        out["contract_document_id"] = "*** Sensitive Data Redacted ***"
    if "approver_details" in value:
        import capo_billing.types.approver_details

        out["approver_details"] = capo_billing.types.approver_details.redact_sensitive(
            value["approver_details"]
        )
    if "additional_recipients" in value:
        import capo_billing.types.additional_recipients

        out["additional_recipients"] = (
            capo_billing.types.additional_recipients.redact_sensitive(
                value["additional_recipients"]
            )
        )
    return out
