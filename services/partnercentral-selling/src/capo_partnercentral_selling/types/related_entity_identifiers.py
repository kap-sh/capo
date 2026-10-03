"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#RelatedEntityIdentifiers``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_marketplace_offer_identifiers
    import capo_partnercentral_selling.types.aws_marketplace_offer_set_identifiers
    import capo_partnercentral_selling.types.aws_marketplace_product_identifiers
    import capo_partnercentral_selling.types.aws_marketplace_solution_identifiers
    import capo_partnercentral_selling.types.aws_product_identifiers
    import capo_partnercentral_selling.types.solution_identifiers


class RelatedEntityIdentifiers(TypedDict, closed=True):
    aws_marketplace_offers: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_offer_identifiers.AwsMarketplaceOfferIdentifiers"
    ]
    """<p>Takes one value per opportunity. Each value is an Amazon Resource Name (ARN), in this format: <code>"offers": ["arn:aws:aws-marketplace:us-east-1:999999999999:AWSMarketplace/Offer/offer-sampleOffer32"]</code>.</p> <p>Use the <a href="https://docs.aws.amazon.com/marketplace-catalog/latest/api-reference/API_ListEntities.html">ListEntities</a> action in the Marketplace Catalog APIs for a list of offers in the associated Marketplace seller account.</p>"""
    aws_marketplace_offer_sets: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_offer_set_identifiers.AwsMarketplaceOfferSetIdentifiers"
    ]
    """<p>Enables the association of AWS Marketplace offer sets with the <code>Opportunity</code>. Offer sets allow grouping multiple related marketplace offers together for comprehensive solution packaging. Each value is an Amazon Resource Name (ARN) in this format: <code>arn:aws:aws-marketplace:us-east-1:999999999999:AWSMarketplace/OfferSet/offerset-sampleOfferSet32</code>.</p>"""
    solutions: NotRequired[
        "capo_partnercentral_selling.types.solution_identifiers.SolutionIdentifiers"
    ]
    """<p>Enables partner solutions or offerings' association with an opportunity. To associate a solution, provide the solution's unique identifier, which you can obtain with the <code>ListSolutions</code> operation.</p> <p>If the specific solution identifier is not available, you can use the value <code>Other</code> and provide details about the solution in the <code>otherSolutionOffered</code> field. But when the opportunity reaches the <code>Committed</code> stage or beyond, the <code>Other</code> value cannot be used, and a valid solution identifier must be provided.</p> <p>By associating the relevant solutions with the opportunity, you can communicate the offerings that are being considered or implemented to address the customer's business problem.</p>"""
    aws_products: NotRequired[
        "capo_partnercentral_selling.types.aws_product_identifiers.AwsProductIdentifiers"
    ]
    """<p>Enables the association of specific Amazon Web Services products with the <code>Opportunity</code>. Partners can indicate the relevant Amazon Web Services products for the <code>Opportunity</code>'s solution and align with the customer's needs. Returns multiple values separated by commas. For example, <code>"AWSProducts" : ["AmazonRedshift", "AWSAppFabric", "AWSCleanRooms"]</code>.</p> <p>Use the file with the list of Amazon Web Services products hosted on GitHub: <a href="https://github.com/aws-samples/partner-crm-integration-samples/blob/main/resources/aws_products.json"> Amazon Web Services products</a>.</p>"""
    aws_marketplace_solutions: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_solution_identifiers.AwsMarketplaceSolutionIdentifiers"
    ]
    """<p>Specifies the AWS Marketplace solutions to associate with the <code>Opportunity</code>. Each value is an Amazon Resource Name (ARN) that identifies a solution listing in AWS Marketplace.</p>"""
    aws_marketplace_products: NotRequired[
        "capo_partnercentral_selling.types.aws_marketplace_product_identifiers.AwsMarketplaceProductIdentifiers"
    ]
    """<p>Specifies the AWS Marketplace products to associate with the <code>Opportunity</code>. Each value is an Amazon Resource Name (ARN) that identifies a product listing in AWS Marketplace.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: RelatedEntityIdentifiers) -> dict:
    out: dict = {}
    if "aws_marketplace_offers" in value:
        import capo_partnercentral_selling.types.aws_marketplace_offer_identifiers

        out["AwsMarketplaceOffers"] = (
            capo_partnercentral_selling.types.aws_marketplace_offer_identifiers.serialize_aws_json_1_0(
                value["aws_marketplace_offers"]
            )
        )
    if "aws_marketplace_offer_sets" in value:
        import capo_partnercentral_selling.types.aws_marketplace_offer_set_identifiers

        out["AwsMarketplaceOfferSets"] = (
            capo_partnercentral_selling.types.aws_marketplace_offer_set_identifiers.serialize_aws_json_1_0(
                value["aws_marketplace_offer_sets"]
            )
        )
    if "solutions" in value:
        import capo_partnercentral_selling.types.solution_identifiers

        out["Solutions"] = (
            capo_partnercentral_selling.types.solution_identifiers.serialize_aws_json_1_0(
                value["solutions"]
            )
        )
    if "aws_products" in value:
        import capo_partnercentral_selling.types.aws_product_identifiers

        out["AwsProducts"] = (
            capo_partnercentral_selling.types.aws_product_identifiers.serialize_aws_json_1_0(
                value["aws_products"]
            )
        )
    if "aws_marketplace_solutions" in value:
        import capo_partnercentral_selling.types.aws_marketplace_solution_identifiers

        out["AwsMarketplaceSolutions"] = (
            capo_partnercentral_selling.types.aws_marketplace_solution_identifiers.serialize_aws_json_1_0(
                value["aws_marketplace_solutions"]
            )
        )
    if "aws_marketplace_products" in value:
        import capo_partnercentral_selling.types.aws_marketplace_product_identifiers

        out["AwsMarketplaceProducts"] = (
            capo_partnercentral_selling.types.aws_marketplace_product_identifiers.serialize_aws_json_1_0(
                value["aws_marketplace_products"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> RelatedEntityIdentifiers:
    out: RelatedEntityIdentifiers = {}  # type: ignore[typeddict-item]
    if data.get("AwsMarketplaceOffers") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_offer_identifiers

        out["aws_marketplace_offers"] = (
            capo_partnercentral_selling.types.aws_marketplace_offer_identifiers.deserialize_aws_json_1_0(
                data["AwsMarketplaceOffers"]
            )
        )
    if data.get("AwsMarketplaceOfferSets") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_offer_set_identifiers

        out["aws_marketplace_offer_sets"] = (
            capo_partnercentral_selling.types.aws_marketplace_offer_set_identifiers.deserialize_aws_json_1_0(
                data["AwsMarketplaceOfferSets"]
            )
        )
    if data.get("Solutions") is not None:
        import capo_partnercentral_selling.types.solution_identifiers

        out["solutions"] = (
            capo_partnercentral_selling.types.solution_identifiers.deserialize_aws_json_1_0(
                data["Solutions"]
            )
        )
    if data.get("AwsProducts") is not None:
        import capo_partnercentral_selling.types.aws_product_identifiers

        out["aws_products"] = (
            capo_partnercentral_selling.types.aws_product_identifiers.deserialize_aws_json_1_0(
                data["AwsProducts"]
            )
        )
    if data.get("AwsMarketplaceSolutions") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_solution_identifiers

        out["aws_marketplace_solutions"] = (
            capo_partnercentral_selling.types.aws_marketplace_solution_identifiers.deserialize_aws_json_1_0(
                data["AwsMarketplaceSolutions"]
            )
        )
    if data.get("AwsMarketplaceProducts") is not None:
        import capo_partnercentral_selling.types.aws_marketplace_product_identifiers

        out["aws_marketplace_products"] = (
            capo_partnercentral_selling.types.aws_marketplace_product_identifiers.deserialize_aws_json_1_0(
                data["AwsMarketplaceProducts"]
            )
        )
    return out
