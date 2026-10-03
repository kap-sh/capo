"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateOpportunityRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.customer
    import capo_partnercentral_selling.types.life_cycle
    import capo_partnercentral_selling.types.marketing
    import capo_partnercentral_selling.types.national_security
    import capo_partnercentral_selling.types.opportunity_origin
    import capo_partnercentral_selling.types.opportunity_type
    import capo_partnercentral_selling.types.partner_opportunity_team_members_list
    import capo_partnercentral_selling.types.primary_needs_from_aws
    import capo_partnercentral_selling.types.project
    import capo_partnercentral_selling.types.software_revenue
    import capo_partnercentral_selling.types.tag_list


class CreateOpportunityRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog associated with the request. This field takes a string value from a predefined list: <code>AWS</code> or <code>Sandbox</code>. The catalog determines which environment the opportunity is created in. Use <code>AWS</code> to create opportunities in the Amazon Web Services catalog, and <code>Sandbox</code> for testing in secure, isolated environments.</p>"""
    primary_needs_from_aws: NotRequired[
        "capo_partnercentral_selling.types.primary_needs_from_aws.PrimaryNeedsFromAws"
    ]
    """<p>Identifies the type of support the partner needs from Amazon Web Services.</p> <p>Valid values:</p> <ul> <li> <p>Cosell—Architectural Validation: Confirmation from Amazon Web Services that the partner's proposed solution architecture is aligned with Amazon Web Services best practices and poses minimal architectural risks.</p> </li> <li> <p>Cosell—Business Presentation: Request Amazon Web Services seller's participation in a joint customer presentation.</p> </li> <li> <p>Cosell—Competitive Information: Access to Amazon Web Services competitive resources and support for the partner's proposed solution.</p> </li> <li> <p>Cosell—Pricing Assistance: Connect with an Amazon Web Services seller for support situations where a partner may be receiving an upfront discount on a service (for example: EDP deals).</p> </li> <li> <p>Cosell—Technical Consultation: Connect with an Amazon Web Services Solutions Architect to address the partner's questions about the proposed solution.</p> </li> <li> <p>Cosell—Total Cost of Ownership Evaluation: Assistance with quoting different cost savings of proposed solutions on Amazon Web Services versus on-premises or a traditional hosting environment.</p> </li> <li> <p>Cosell—Deal Support: Request Amazon Web Services seller's support to progress the opportunity (for example: joint customer call, strategic positioning).</p> </li> <li> <p>Cosell—Support for Public Tender/RFx: Opportunity related to the public sector where the partner needs Amazon Web Services RFx support.</p> </li> </ul>"""
    national_security: NotRequired[
        "capo_partnercentral_selling.types.national_security.NationalSecurity"
    ]
    """<p>Indicates whether the <code>Opportunity</code> pertains to a national security project. This field must be set to <code>true</code> only when the customer's industry is <i>Government</i>. Additional privacy and security measures apply during the review and management process for opportunities marked as <code>NationalSecurity</code>.</p>"""
    partner_opportunity_identifier: NotRequired["str"]
    """<p>Specifies the opportunity's unique identifier in the partner's CRM system. This value is essential to track and reconcile because it's included in the outbound payload to the partner.</p> <p>This field allows partners to link an opportunity to their CRM, which helps to ensure seamless integration and accurate synchronization between the Partner Central API and the partner's internal systems.</p>"""
    customer: NotRequired["capo_partnercentral_selling.types.customer.Customer"]
    """<p>Specifies customer details associated with the <code>Opportunity</code>.</p>"""
    project: NotRequired["capo_partnercentral_selling.types.project.Project"]
    """<p>An object that contains project details for the <code>Opportunity</code>.</p>"""
    opportunity_type: NotRequired[
        "capo_partnercentral_selling.types.opportunity_type.OpportunityType"
    ]
    """<p>Specifies the opportunity type as a renewal, new, or expansion.</p> <p>Opportunity types:</p> <ul> <li> <p>New opportunity: Represents a new business opportunity with a potential customer that's not previously engaged with your solutions or services.</p> </li> <li> <p>Renewal opportunity: Represents an opportunity to renew an existing contract or subscription with a current customer, ensuring continuity of service.</p> </li> <li> <p>Expansion opportunity: Represents an opportunity to expand the scope of an existing contract or subscription, either by adding new services or increasing the volume of existing services for a current customer.</p> </li> </ul>"""
    marketing: NotRequired["capo_partnercentral_selling.types.marketing.Marketing"]
    """<p>This object contains marketing details and is optional for an opportunity.</p>"""
    software_revenue: NotRequired[
        "capo_partnercentral_selling.types.software_revenue.SoftwareRevenue"
    ]
    """<p>Specifies details of a customer's procurement terms. This is required only for partners in eligible programs.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>Required to be unique, and should be unchanging, it can be randomly generated or a meaningful string.</p> <p>Default: None</p> <p>Best practice: To help ensure uniqueness and avoid conflicts, use a Universally Unique Identifier (UUID) as the <code>ClientToken</code>. You can use standard libraries from most programming languages to generate this. If you use the same client token, the API returns the following error: "Conflicting client token submitted for a new request body."</p>"""
    life_cycle: NotRequired["capo_partnercentral_selling.types.life_cycle.LifeCycle"]
    """<p>An object that contains lifecycle details for the <code>Opportunity</code>.</p>"""
    origin: NotRequired[
        "capo_partnercentral_selling.types.opportunity_origin.OpportunityOrigin"
    ]
    """<p>Specifies the origin of the opportunity, indicating if it was sourced from Amazon Web Services or the partner. For all opportunities created with <code>Catalog: AWS</code>, this field must only be <code>Partner Referral</code>. However, when using <code>Catalog: Sandbox</code>, you can set this field to <code>AWS Referral</code> to simulate Amazon Web Services referral creation. This allows Amazon Web Services-originated flows testing in the sandbox catalog.</p>"""
    opportunity_team: NotRequired[
        "capo_partnercentral_selling.types.partner_opportunity_team_members_list.PartnerOpportunityTeamMembersList"
    ]
    """<p>Represents the internal team handling the opportunity. Specify collaborating members of this opportunity who are within the partner's organization.</p>"""
    tags: NotRequired["capo_partnercentral_selling.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateOpportunityRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "primary_needs_from_aws" in value:
        import capo_partnercentral_selling.types.primary_needs_from_aws

        out["PrimaryNeedsFromAws"] = (
            capo_partnercentral_selling.types.primary_needs_from_aws.serialize_aws_json_1_0(
                value["primary_needs_from_aws"]
            )
        )
    if "national_security" in value:
        import capo_partnercentral_selling.types.national_security

        out["NationalSecurity"] = (
            capo_partnercentral_selling.types.national_security.serialize_aws_json_1_0(
                value["national_security"]
            )
        )
    if "partner_opportunity_identifier" in value:
        out["PartnerOpportunityIdentifier"] = value["partner_opportunity_identifier"]
    if "customer" in value:
        import capo_partnercentral_selling.types.customer

        out["Customer"] = (
            capo_partnercentral_selling.types.customer.serialize_aws_json_1_0(
                value["customer"]
            )
        )
    if "project" in value:
        import capo_partnercentral_selling.types.project

        out["Project"] = (
            capo_partnercentral_selling.types.project.serialize_aws_json_1_0(
                value["project"]
            )
        )
    if "opportunity_type" in value:
        import capo_partnercentral_selling.types.opportunity_type

        out["OpportunityType"] = (
            capo_partnercentral_selling.types.opportunity_type.serialize_aws_json_1_0(
                value["opportunity_type"]
            )
        )
    if "marketing" in value:
        import capo_partnercentral_selling.types.marketing

        out["Marketing"] = (
            capo_partnercentral_selling.types.marketing.serialize_aws_json_1_0(
                value["marketing"]
            )
        )
    if "software_revenue" in value:
        import capo_partnercentral_selling.types.software_revenue

        out["SoftwareRevenue"] = (
            capo_partnercentral_selling.types.software_revenue.serialize_aws_json_1_0(
                value["software_revenue"]
            )
        )
    out["ClientToken"] = value["client_token"]
    if "life_cycle" in value:
        import capo_partnercentral_selling.types.life_cycle

        out["LifeCycle"] = (
            capo_partnercentral_selling.types.life_cycle.serialize_aws_json_1_0(
                value["life_cycle"]
            )
        )
    if "origin" in value:
        import capo_partnercentral_selling.types.opportunity_origin

        out["Origin"] = (
            capo_partnercentral_selling.types.opportunity_origin.serialize_aws_json_1_0(
                value["origin"]
            )
        )
    if "opportunity_team" in value:
        import capo_partnercentral_selling.types.partner_opportunity_team_members_list

        out["OpportunityTeam"] = (
            capo_partnercentral_selling.types.partner_opportunity_team_members_list.serialize_aws_json_1_0(
                value["opportunity_team"]
            )
        )
    if "tags" in value:
        import capo_partnercentral_selling.types.tag_list

        out["Tags"] = capo_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateOpportunityRequest:
    out: CreateOpportunityRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("CreateOpportunityRequest.catalog required")
    if data.get("PrimaryNeedsFromAws") is not None:
        import capo_partnercentral_selling.types.primary_needs_from_aws

        out["primary_needs_from_aws"] = (
            capo_partnercentral_selling.types.primary_needs_from_aws.deserialize_aws_json_1_0(
                data["PrimaryNeedsFromAws"]
            )
        )
    if data.get("NationalSecurity") is not None:
        import capo_partnercentral_selling.types.national_security

        out["national_security"] = (
            capo_partnercentral_selling.types.national_security.deserialize_aws_json_1_0(
                data["NationalSecurity"]
            )
        )
    if data.get("PartnerOpportunityIdentifier") is not None:
        out["partner_opportunity_identifier"] = data["PartnerOpportunityIdentifier"]
    if data.get("Customer") is not None:
        import capo_partnercentral_selling.types.customer

        out["customer"] = (
            capo_partnercentral_selling.types.customer.deserialize_aws_json_1_0(
                data["Customer"]
            )
        )
    if data.get("Project") is not None:
        import capo_partnercentral_selling.types.project

        out["project"] = (
            capo_partnercentral_selling.types.project.deserialize_aws_json_1_0(
                data["Project"]
            )
        )
    if data.get("OpportunityType") is not None:
        import capo_partnercentral_selling.types.opportunity_type

        out["opportunity_type"] = (
            capo_partnercentral_selling.types.opportunity_type.deserialize_aws_json_1_0(
                data["OpportunityType"]
            )
        )
    if data.get("Marketing") is not None:
        import capo_partnercentral_selling.types.marketing

        out["marketing"] = (
            capo_partnercentral_selling.types.marketing.deserialize_aws_json_1_0(
                data["Marketing"]
            )
        )
    if data.get("SoftwareRevenue") is not None:
        import capo_partnercentral_selling.types.software_revenue

        out["software_revenue"] = (
            capo_partnercentral_selling.types.software_revenue.deserialize_aws_json_1_0(
                data["SoftwareRevenue"]
            )
        )
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        raise DeserializationError("CreateOpportunityRequest.client_token required")
    if data.get("LifeCycle") is not None:
        import capo_partnercentral_selling.types.life_cycle

        out["life_cycle"] = (
            capo_partnercentral_selling.types.life_cycle.deserialize_aws_json_1_0(
                data["LifeCycle"]
            )
        )
    if data.get("Origin") is not None:
        import capo_partnercentral_selling.types.opportunity_origin

        out["origin"] = (
            capo_partnercentral_selling.types.opportunity_origin.deserialize_aws_json_1_0(
                data["Origin"]
            )
        )
    if data.get("OpportunityTeam") is not None:
        import capo_partnercentral_selling.types.partner_opportunity_team_members_list

        out["opportunity_team"] = (
            capo_partnercentral_selling.types.partner_opportunity_team_members_list.deserialize_aws_json_1_0(
                data["OpportunityTeam"]
            )
        )
    if data.get("Tags") is not None:
        import capo_partnercentral_selling.types.tag_list

        out["tags"] = (
            capo_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
