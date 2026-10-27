"""Generated from Smithy shape ``com.amazonaws.billing#ContractSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import datetime

    import capo_billing.types.arn_string
    import capo_billing.types.association_status
    import capo_billing.types.contract_type
    import capo_billing.types.interval


class ContractSummary(TypedDict, closed=True):
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the contract. Pass this value to operations such as <code>GetContractInformation</code>, <code>ListContractualInvestmentSummaries</code>, and <code>AssociateContract</code>.</p>"""
    contract_term: "capo_billing.types.interval.Interval"
    """<p>The contract term period of the contract, expressed as an interval with an inclusive start date and an inclusive end date.</p>"""
    contract_type: NotRequired["capo_billing.types.contract_type.ContractType"]
    """<p>The classification of the contract. Valid values are <code>Cross-Service</code>, <code>Service-Specific</code>, and <code>Other</code>. <code>Cross-Service</code> applies across multiple Amazon Web Services services. <code>Service-Specific</code> applies to a specific Amazon Web Services service. <code>Other</code> applies to other arrangements.</p>"""
    association_status: "capo_billing.types.association_status.AssociationStatus"
    """<p>Indicates whether the contract is currently associated with your account. Valid values are <code>ASSOCIATED</code> and <code>NOT_ASSOCIATED</code>. <code>ASSOCIATED</code> means the contract is associated with your account. <code>NOT_ASSOCIATED</code> means the contract is not associated with your account.</p>"""
    last_updated_at: NotRequired["datetime.datetime"]
    """<p>The time when the contract was last associated with your account.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ContractSummary) -> dict:
    out: dict = {}
    out["contractArn"] = value["contract_arn"]
    import capo_billing.types.interval

    out["contractTerm"] = capo_billing.types.interval.serialize_aws_json_1_0(
        value["contract_term"]
    )
    if "contract_type" in value:
        import capo_billing.types.contract_type

        out["contractType"] = capo_billing.types.contract_type.serialize_aws_json_1_0(
            value["contract_type"]
        )
    import capo_billing.types.association_status

    out["associationStatus"] = (
        capo_billing.types.association_status.serialize_aws_json_1_0(
            value["association_status"]
        )
    )
    if "last_updated_at" in value:
        import capo_billing.types._prelude.timestamp

        out["lastUpdatedAt"] = (
            capo_billing.types._prelude.timestamp.serialize_aws_json_1_0(
                value["last_updated_at"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> ContractSummary:
    out: ContractSummary = {}  # type: ignore[typeddict-item]
    if data.get("contractArn") is not None:
        out["contract_arn"] = data["contractArn"]
    else:
        out["contract_arn"] = ""
    if data.get("contractTerm") is not None:
        import capo_billing.types.interval

        out["contract_term"] = capo_billing.types.interval.deserialize_aws_json_1_0(
            data["contractTerm"]
        )
    else:
        raise DeserializationError("ContractSummary.contract_term required")
    if data.get("contractType") is not None:
        import capo_billing.types.contract_type

        out["contract_type"] = (
            capo_billing.types.contract_type.deserialize_aws_json_1_0(
                data["contractType"]
            )
        )
    if data.get("associationStatus") is not None:
        import capo_billing.types.association_status

        out["association_status"] = (
            capo_billing.types.association_status.deserialize_aws_json_1_0(
                data["associationStatus"]
            )
        )
    else:
        import typing

        out["association_status"] = typing.cast(
            "capo_billing.types.association_status.AssociationStatus", ""
        )
    if data.get("lastUpdatedAt") is not None:
        import capo_billing.types._prelude.timestamp

        out["last_updated_at"] = (
            capo_billing.types._prelude.timestamp.deserialize_aws_json_1_0(
                data["lastUpdatedAt"]
            )
        )
    return out
