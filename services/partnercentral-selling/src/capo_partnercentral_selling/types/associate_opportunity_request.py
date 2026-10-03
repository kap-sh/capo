"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#AssociateOpportunityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.related_entity_type


class AssociateOpportunityRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity association is made in. Use <code>AWS</code> to associate opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    opportunity_identifier: (
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    )
    """<p>Requires the <code>Opportunity</code>'s unique identifier when you want to associate it with a related entity. Provide the correct identifier so the intended opportunity is updated with the association.</p>"""
    related_entity_type: (
        "capo_partnercentral_selling.types.related_entity_type.RelatedEntityType"
    )
    """<p>Specifies the entity type that you're associating with the <code> Opportunity</code>. This helps to categorize and properly process the association.</p>"""
    related_entity_identifier: "str"
    """<p>Requires the related entity's unique identifier when you want to associate it with the <code> Opportunity</code>. For Amazon Web Services Marketplace entities, provide the Amazon Resource Name (ARN). Use the <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/welcome.html"> Amazon Web Services Marketplace API</a> to obtain the ARN.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociateOpportunityRequest) -> dict:
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


def deserialize_aws_json_1_0(data: dict) -> AssociateOpportunityRequest:
    out: AssociateOpportunityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("AssociateOpportunityRequest.catalog required")
    if data.get("OpportunityIdentifier") is not None:
        out["opportunity_identifier"] = data["OpportunityIdentifier"]
    else:
        raise DeserializationError(
            "AssociateOpportunityRequest.opportunity_identifier required"
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
            "AssociateOpportunityRequest.related_entity_type required"
        )
    if data.get("RelatedEntityIdentifier") is not None:
        out["related_entity_identifier"] = data["RelatedEntityIdentifier"]
    else:
        raise DeserializationError(
            "AssociateOpportunityRequest.related_entity_identifier required"
        )
    return out
