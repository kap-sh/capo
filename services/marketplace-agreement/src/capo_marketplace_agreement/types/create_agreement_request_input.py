"""Generated from Smithy shape ``com.amazonaws.marketplaceagreement#CreateAgreementRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_marketplace_agreement.types.agreement_proposal_id
    import capo_marketplace_agreement.types.client_token
    import capo_marketplace_agreement.types.intent
    import capo_marketplace_agreement.types.requested_term_list
    import capo_marketplace_agreement.types.resource_id
    import capo_marketplace_agreement.types.tax_configuration


class CreateAgreementRequestInput(TypedDict, closed=True):
    client_token: NotRequired[
        "capo_marketplace_agreement.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.</p>"""
    intent: "capo_marketplace_agreement.types.intent.Intent"
    """<p>The purpose and desired outcome of the agreement request. This is a required parameter that determines how the agreement request is processed.</p> <ul> <li> <p> <code>NEW</code> – Creates a new agreement for terms in the request.</p> </li> <li> <p> <code>AMEND</code> – Modifies an existing agreement with terms that are accepted in the request.</p> </li> <li> <p> <code>REPLACE</code> – Creates a new agreement with accepted terms and replaces the existing agreement.</p> </li> </ul>"""
    requested_terms: (
        "capo_marketplace_agreement.types.requested_term_list.RequestedTermList"
    )
    """<p>A list of terms that define what is being accepted as part of the agreement. Some terms require configuration.</p>"""
    source_agreement_identifier: NotRequired[
        "capo_marketplace_agreement.types.resource_id.ResourceId"
    ]
    """<p>The agreement's identifier that the request acts upon.</p> <important> <p> This parameter is required for all non-<code>NEW</code> intents (i.e., <code>AMEND</code> or <code>REPLACE</code>). Don't provide this parameter if the intent is <code>NEW</code>. </p> </important>"""
    agreement_proposal_identifier: NotRequired[
        "capo_marketplace_agreement.types.agreement_proposal_id.AgreementProposalId"
    ]
    """<p>The agreement proposal signed by the proposer. The proposal includes the requested resources and the terms that outline an agreement outcome.</p> <important> <p> This parameter is required if the intent is not <code>AMEND</code>.</p> </important>"""
    tax_configuration: NotRequired[
        "capo_marketplace_agreement.types.tax_configuration.TaxConfiguration"
    ]
    """<p>Configuration for tax estimation in the agreement request response.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAgreementRequestInput) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    import capo_marketplace_agreement.types.intent

    out["intent"] = capo_marketplace_agreement.types.intent.serialize_aws_json_1_0(
        value["intent"]
    )
    import capo_marketplace_agreement.types.requested_term_list

    out["requestedTerms"] = (
        capo_marketplace_agreement.types.requested_term_list.serialize_aws_json_1_0(
            value["requested_terms"]
        )
    )
    if "source_agreement_identifier" in value:
        out["sourceAgreementIdentifier"] = value["source_agreement_identifier"]
    if "agreement_proposal_identifier" in value:
        out["agreementProposalIdentifier"] = value["agreement_proposal_identifier"]
    if "tax_configuration" in value:
        import capo_marketplace_agreement.types.tax_configuration

        out["taxConfiguration"] = (
            capo_marketplace_agreement.types.tax_configuration.serialize_aws_json_1_0(
                value["tax_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAgreementRequestInput:
    out: CreateAgreementRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("intent") is not None:
        import capo_marketplace_agreement.types.intent

        out["intent"] = (
            capo_marketplace_agreement.types.intent.deserialize_aws_json_1_0(
                data["intent"]
            )
        )
    else:
        import typing

        out["intent"] = typing.cast(
            "capo_marketplace_agreement.types.intent.Intent", ""
        )
    if data.get("requestedTerms") is not None:
        import capo_marketplace_agreement.types.requested_term_list

        out["requested_terms"] = (
            capo_marketplace_agreement.types.requested_term_list.deserialize_aws_json_1_0(
                data["requestedTerms"]
            )
        )
    else:
        out["requested_terms"] = []
    if data.get("sourceAgreementIdentifier") is not None:
        out["source_agreement_identifier"] = data["sourceAgreementIdentifier"]
    if data.get("agreementProposalIdentifier") is not None:
        out["agreement_proposal_identifier"] = data["agreementProposalIdentifier"]
    if data.get("taxConfiguration") is not None:
        import capo_marketplace_agreement.types.tax_configuration

        out["tax_configuration"] = (
            capo_marketplace_agreement.types.tax_configuration.deserialize_aws_json_1_0(
                data["taxConfiguration"]
            )
        )
    return out
