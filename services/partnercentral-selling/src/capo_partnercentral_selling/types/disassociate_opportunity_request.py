"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#DisassociateOpportunityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.related_entity_type


class DisassociateOpportunityRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity disassociation is made in. Use <code>AWS</code> to disassociate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    opportunity_identifier: (
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    )
    """<p>The opportunity's unique identifier for when you want to disassociate it from related entities. This identifier helps to ensure that the correct opportunity is updated.</p> <p>Validation: Ensure that the provided identifier corresponds to an existing opportunity in the Amazon Web Services system because incorrect identifiers result in an error and no changes are made.</p>"""
    related_entity_type: (
        "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType"
    )
    """<p>The type of the entity that you're disassociating from the opportunity. When you specify the entity type, it helps the system correctly process the disassociation request to ensure that the right connections are removed.</p> <p>Examples of entity types include Partner Solution, Amazon Web Services product, and Amazon Web Services Marketplaceoffer. Ensure that the value matches one of the expected entity types.</p> <p>Validation: Provide a valid entity type to help ensure successful disassociation. An invalid or incorrect entity type results in an error.</p>"""
    related_entity_identifier: "str"
    """<p>The related entity's identifier that you want to disassociate from the opportunity. Depending on the type of entity, this could be a simple identifier or an Amazon Resource Name (ARN) for entities managed through Amazon Web Services Marketplace.</p> <p>For Amazon Web Services Marketplace entities, use the Amazon Web Services Marketplace API to obtain the necessary ARNs. For guidance on retrieving these ARNs, see <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services MarketplaceUsing the Amazon Web Services Marketplace Catalog API</a>.</p> <p>Validation: Ensure the identifier or ARN is valid and corresponds to an existing entity. An incorrect or invalid identifier results in an error.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DisassociateOpportunityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["OpportunityIdentifier"] = value["opportunity_identifier"]
    import capo_partnercentral_selling.types.related_entity_type

    out["RelatedEntityType"] = (
        capo_partnercentral_selling.types.related_entity_type.serialize_aws_json_1_0(
            value["related_entity_type"]
        )
    )
    out["RelatedEntityIdentifier"] = value["related_entity_identifier"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DisassociateOpportunityRequest:
    out: DisassociateOpportunityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("DisassociateOpportunityRequest.catalog required")
    if data.get("OpportunityIdentifier") is not None:
        out["opportunity_identifier"] = data["OpportunityIdentifier"]
    else:
        raise DeserializationError(
            "DisassociateOpportunityRequest.opportunity_identifier required"
        )
    if data.get("RelatedEntityType") is not None:
        import capo_partnercentral_selling.types.related_entity_type

        out["related_entity_type"] = (
            capo_partnercentral_selling.types.related_entity_type.deserialize_aws_json_1_0(
                data["RelatedEntityType"]
            )
        )
    else:
        raise DeserializationError(
            "DisassociateOpportunityRequest.related_entity_type required"
        )
    if data.get("RelatedEntityIdentifier") is not None:
        out["related_entity_identifier"] = data["RelatedEntityIdentifier"]
    else:
        raise DeserializationError(
            "DisassociateOpportunityRequest.related_entity_identifier required"
        )
    return out
