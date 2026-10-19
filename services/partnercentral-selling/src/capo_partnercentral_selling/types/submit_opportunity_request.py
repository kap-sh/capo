"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#SubmitOpportunityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.opportunity_identifier
    import capo_partnercentral_selling.types.sales_involvement_type
    import capo_partnercentral_selling.types.visibility


class SubmitOpportunityRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Submits the opportunity request from the production AWS environment.</p> </li> <li> <p>Sandbox: Submits the opportunity request from a sandbox environment used for testing or development purposes.</p> </li> </ul>"""
    identifier: (
        "capo_partnercentral_selling.types.opportunity_identifier.OpportunityIdentifier"
    )
    """<p>The identifier of the Opportunity previously created by partner and needs to be submitted.</p>"""
    involvement_type: (
        "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType"
    )
    """<p>Specifies the level of AWS sellers' involvement on the opportunity. Valid values:</p> <ul> <li> <p> <code>Co-sell</code>: Indicates the user wants to co-sell with AWS. Share the opportunity with AWS to receive deal assistance and support.</p> </li> <li> <p> <code>For Visibility Only</code>: Indicates that the user does not need support from AWS Sales Rep. Share this opportunity with AWS for visibility only, you will not receive deal assistance and support.</p> </li> </ul>"""
    visibility: NotRequired["capo_partnercentral_selling.types.visibility.Visibility"]
    """<p>Determines whether to restrict visibility of the opportunity from AWS sales. Default value is Full. Valid values:</p> <ul> <li> <p> <code>Full</code>: The opportunity is fully visible to AWS sales.</p> </li> <li> <p> <code>Limited</code>: The opportunity has restricted visibility to AWS sales.</p> </li> </ul>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SubmitOpportunityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["Identifier"] = value["identifier"]
    import capo_partnercentral_selling.types.sales_involvement_type

    out["InvolvementType"] = (
        capo_partnercentral_selling.types.sales_involvement_type.serialize_aws_json_1_0(
            value["involvement_type"]
        )
    )
    if "visibility" in value:
        import capo_partnercentral_selling.types.visibility

        out["Visibility"] = (
            capo_partnercentral_selling.types.visibility.serialize_aws_json_1_0(
                value["visibility"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> SubmitOpportunityRequest:
    out: SubmitOpportunityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("InvolvementType") is not None:
        import capo_partnercentral_selling.types.sales_involvement_type

        out["involvement_type"] = (
            capo_partnercentral_selling.types.sales_involvement_type.deserialize_aws_json_1_0(
                data["InvolvementType"]
            )
        )
    else:
        import typing

        out["involvement_type"] = typing.cast(
            "capo_partnercentral_selling.types.sales_involvement_type.SalesInvolvementType",
            "",
        )
    if data.get("Visibility") is not None:
        import capo_partnercentral_selling.types.visibility

        out["visibility"] = (
            capo_partnercentral_selling.types.visibility.deserialize_aws_json_1_0(
                data["Visibility"]
            )
        )
    return out
