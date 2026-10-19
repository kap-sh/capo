"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#EngagementResourceAssociationSummary``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_type


class EngagementResourceAssociationSummary(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Indicates the environment in which the resource and engagement exist. </p>"""
    engagement_id: NotRequired[
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    ]
    """<p> A unique identifier for the engagement associated with the resource. </p>"""
    resource_type: NotRequired[
        "capo_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p> Categorizes the type of resource associated with the engagement. </p>"""
    resource_id: NotRequired[
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p> A unique identifier for the specific resource. Varies depending on the resource type. </p>"""
    created_by: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>The AWS account ID of the entity that owns the resource. Identifies the account responsible for or having primary control over the resource. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EngagementResourceAssociationSummary) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    if "engagement_id" in value:
        out["EngagementId"] = value["engagement_id"]
    if "resource_type" in value:
        import capo_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            capo_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_id" in value:
        out["ResourceId"] = value["resource_id"]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> EngagementResourceAssociationSummary:
    out: EngagementResourceAssociationSummary = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("EngagementId") is not None:
        out["engagement_id"] = data["EngagementId"]
    if data.get("ResourceType") is not None:
        import capo_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            capo_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if data.get("ResourceId") is not None:
        out["resource_id"] = data["ResourceId"]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    return out


def redact_sensitive(value: EngagementResourceAssociationSummary) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "created_by" in value:
        out["created_by"] = "*** Sensitive Data Redacted ***"
    return out
