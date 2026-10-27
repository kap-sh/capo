"""Generated from Smithy shape ``com.amazonaws.billing#PrivatePricingAddendum``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_billing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_billing.types.account_list
    import capo_billing.types.arn_string
    import capo_billing.types.contract_restrictions
    import capo_billing.types.interval
    import capo_billing.types.legal_entities


class PrivatePricingAddendum(TypedDict, closed=True):
    contract_arn: "capo_billing.types.arn_string.ArnString"
    """<p>The Amazon Resource Name (ARN) of the private pricing addendum.</p>"""
    contract_term: "capo_billing.types.interval.Interval"
    """<p>The contract term period of the private pricing addendum, expressed as an interval with an inclusive start date and an inclusive end date.</p>"""
    eligible_payer_accounts: "capo_billing.types.account_list.AccountList"
    """<p>The payer accounts that are eligible under the private pricing addendum. The list contains at most 100 account IDs.</p>"""
    investment_accounts: "capo_billing.types.account_list.AccountList"
    """<p>The accounts that are eligible to receive investments under the private pricing addendum. An <code>InvestmentDistribution</code> must target one of these accounts. The list contains at most 100 account IDs.</p>"""
    legal_entities: "capo_billing.types.legal_entities.LegalEntities"
    """<p>The legal entities on the private pricing addendum. The list contains at most 10 legal entities.</p>"""
    contract_restrictions: NotRequired[
        "capo_billing.types.contract_restrictions.ContractRestrictions"
    ]
    """<p>The restrictions that limit the self-service actions you can take on the private pricing addendum. An empty or absent value indicates that no restrictions apply. The list contains at most 10 restrictions.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: PrivatePricingAddendum) -> dict:
    out: dict = {}
    out["contractArn"] = value["contract_arn"]
    import capo_billing.types.interval

    out["contractTerm"] = capo_billing.types.interval.serialize_aws_json_1_0(
        value["contract_term"]
    )
    import capo_billing.types.account_list

    out["eligiblePayerAccounts"] = (
        capo_billing.types.account_list.serialize_aws_json_1_0(
            value["eligible_payer_accounts"]
        )
    )
    import capo_billing.types.account_list

    out["investmentAccounts"] = capo_billing.types.account_list.serialize_aws_json_1_0(
        value["investment_accounts"]
    )
    import capo_billing.types.legal_entities

    out["legalEntities"] = capo_billing.types.legal_entities.serialize_aws_json_1_0(
        value["legal_entities"]
    )
    if "contract_restrictions" in value:
        import capo_billing.types.contract_restrictions

        out["contractRestrictions"] = (
            capo_billing.types.contract_restrictions.serialize_aws_json_1_0(
                value["contract_restrictions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> PrivatePricingAddendum:
    out: PrivatePricingAddendum = {}  # type: ignore[typeddict-item]
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
        raise DeserializationError("PrivatePricingAddendum.contract_term required")
    if data.get("eligiblePayerAccounts") is not None:
        import capo_billing.types.account_list

        out["eligible_payer_accounts"] = (
            capo_billing.types.account_list.deserialize_aws_json_1_0(
                data["eligiblePayerAccounts"]
            )
        )
    else:
        out["eligible_payer_accounts"] = []
    if data.get("investmentAccounts") is not None:
        import capo_billing.types.account_list

        out["investment_accounts"] = (
            capo_billing.types.account_list.deserialize_aws_json_1_0(
                data["investmentAccounts"]
            )
        )
    else:
        out["investment_accounts"] = []
    if data.get("legalEntities") is not None:
        import capo_billing.types.legal_entities

        out["legal_entities"] = (
            capo_billing.types.legal_entities.deserialize_aws_json_1_0(
                data["legalEntities"]
            )
        )
    else:
        out["legal_entities"] = []
    if data.get("contractRestrictions") is not None:
        import capo_billing.types.contract_restrictions

        out["contract_restrictions"] = (
            capo_billing.types.contract_restrictions.deserialize_aws_json_1_0(
                data["contractRestrictions"]
            )
        )
    return out


def redact_sensitive(value: PrivatePricingAddendum) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "legal_entities" in value:
        import capo_billing.types.legal_entities

        out["legal_entities"] = capo_billing.types.legal_entities.redact_sensitive(
            value["legal_entities"]
        )
    return out
