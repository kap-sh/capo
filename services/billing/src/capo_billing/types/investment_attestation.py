"""Generated from Smithy shape ``com.amazonaws.billing#InvestmentAttestation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.amount
    import capo_billing.types.identifier_string
    import capo_billing.types.investment_attestation_status
    import capo_billing.types.investment_distributions
    import capo_billing.types.rejection_reasons


class InvestmentAttestation(TypedDict, closed=True):
    attestation_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the attestation. This value is returned by <code>CreateContractualInvestmentAttestation</code> and is used to cancel the attestation with <code>CancelContractualInvestmentAttestation</code>. This value is 1–36 characters.</p>"""
    investment_name: "str"
    """<p>The name of the investment summary that contains the attested outcome. This value is 1–400 characters.</p>"""
    outcome_description: "str"
    """<p>The description of the attested outcome. This value is 1–2048 characters.</p>"""
    investment_summary_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment summary that was attested, as returned by <code>ListContractualInvestmentSummaries</code>.</p>"""
    investment_id: "capo_billing.types.identifier_string.IdentifierString"
    """<p>The identifier of the investment that was attested, as returned by <code>ListContractualInvestments</code>.</p>"""
    attested_at: "datetime.datetime"
    """<p>The date on which the attestation was submitted.</p>"""
    updated_at: "datetime.datetime"
    """<p>The date on which the attestation was last updated.</p>"""
    attestation_status: (
        "capo_billing.types.investment_attestation_status.InvestmentAttestationStatus"
    )
    """<p>The current status of the attestation. Valid values are <code>PENDING_REVIEW</code>, <code>PENDING_C_LEVEL_APPROVAL</code>, <code>PENDING_CANCELLATION</code>, <code>REJECTED</code>, <code>CANCELLED</code>, and <code>DISBURSED</code>. The values <code>DISBURSED</code>, <code>REJECTED</code>, and <code>CANCELLED</code> are terminal. The other values indicate the attestation is still in progress.</p>"""
    investment_disbursed_at: NotRequired["datetime.datetime"]
    """<p>The start date on which the investment is disbursed to the investment accounts. This is not the same as the time of disbursement, but reflects the date you submitted with the attestation.</p>"""
    attested_value: NotRequired["capo_billing.types.amount.Amount"]
    """<p>The monetary value attested.</p>"""
    investment_distributions: NotRequired[
        "capo_billing.types.investment_distributions.InvestmentDistributions"
    ]
    """<p>The distribution of the attested investment across the eligible investment accounts. The list contains at most 200 distributions.</p>"""
    rejection_reasons: NotRequired[
        "capo_billing.types.rejection_reasons.RejectionReasons"
    ]
    """<p>The reasons the attestation was rejected. This value is present only when <code>attestationStatus</code> is <code>REJECTED</code>. The list contains at most 30 reasons.</p>"""
    is_cancellable: NotRequired["bool"]
    """<p>Indicates whether the attestation can be canceled with <code>CancelContractualInvestmentAttestation</code>.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: InvestmentAttestation) -> dict:
    out: dict = {}
    out["attestationId"] = value["attestation_id"]
    out["investmentName"] = value["investment_name"]
    out["outcomeDescription"] = value["outcome_description"]
    out["investmentSummaryId"] = value["investment_summary_id"]
    out["investmentId"] = value["investment_id"]
    import capo_billing.types._prelude.timestamp

    out["attestedAt"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["attested_at"]
    )
    import capo_billing.types._prelude.timestamp

    out["updatedAt"] = capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
        value["updated_at"]
    )
    import capo_billing.types.investment_attestation_status

    out["attestationStatus"] = (
        capo_billing.types.investment_attestation_status.serialize_aws_json_1_0(
            value["attestation_status"]
        )
    )
    if "investment_disbursed_at" in value:
        import capo_billing.types._prelude.timestamp

        out["investmentDisbursedAt"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["investment_disbursed_at"]
            )
        )
    if "attested_value" in value:
        import capo_billing.types.amount

        out["attestedValue"] = capo_billing.types.amount.serialize_aws_json_1_0(
            value["attested_value"]
        )
    if "investment_distributions" in value:
        import capo_billing.types.investment_distributions

        out["investmentDistributions"] = (
            capo_billing.types.investment_distributions.serialize_aws_json_1_0(
                value["investment_distributions"]
            )
        )
    if "rejection_reasons" in value:
        import capo_billing.types.rejection_reasons

        out["rejectionReasons"] = (
            capo_billing.types.rejection_reasons.serialize_aws_json_1_0(
                value["rejection_reasons"]
            )
        )
    if "is_cancellable" in value:
        out["isCancellable"] = value["is_cancellable"]
    return out


def deserialize_aws_json_1_0(data: dict) -> InvestmentAttestation:
    out: InvestmentAttestation = {}  # type: ignore[typeddict-item]
    if data.get("attestationId") is not None:
        out["attestation_id"] = data["attestationId"]
    else:
        out["attestation_id"] = ""
    if data.get("investmentName") is not None:
        out["investment_name"] = data["investmentName"]
    else:
        out["investment_name"] = ""
    if data.get("outcomeDescription") is not None:
        out["outcome_description"] = data["outcomeDescription"]
    else:
        out["outcome_description"] = ""
    if data.get("investmentSummaryId") is not None:
        out["investment_summary_id"] = data["investmentSummaryId"]
    else:
        out["investment_summary_id"] = ""
    if data.get("investmentId") is not None:
        out["investment_id"] = data["investmentId"]
    else:
        out["investment_id"] = ""
    if data.get("attestedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["attested_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["attestedAt"]
            )
        )
    else:
        import datetime

        out["attested_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("updatedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["updated_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["updatedAt"]
            )
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("attestationStatus") is not None:
        import capo_billing.types.investment_attestation_status

        out["attestation_status"] = (
            capo_billing.types.investment_attestation_status.deserialize_aws_json_1_0(
                data["attestationStatus"]
            )
        )
    else:
        import typing

        out["attestation_status"] = typing.cast(
            "capo_billing.types.investment_attestation_status.InvestmentAttestationStatus",
            "",
        )
    if data.get("investmentDisbursedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["investment_disbursed_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["investmentDisbursedAt"]
            )
        )
    if data.get("attestedValue") is not None:
        import capo_billing.types.amount

        out["attested_value"] = capo_billing.types.amount.deserialize_aws_json_1_0(
            data["attestedValue"]
        )
    if data.get("investmentDistributions") is not None:
        import capo_billing.types.investment_distributions

        out["investment_distributions"] = (
            capo_billing.types.investment_distributions.deserialize_aws_json_1_0(
                data["investmentDistributions"]
            )
        )
    if data.get("rejectionReasons") is not None:
        import capo_billing.types.rejection_reasons

        out["rejection_reasons"] = (
            capo_billing.types.rejection_reasons.deserialize_aws_json_1_0(
                data["rejectionReasons"]
            )
        )
    if data.get("isCancellable") is not None:
        out["is_cancellable"] = data["isCancellable"]
    return out
