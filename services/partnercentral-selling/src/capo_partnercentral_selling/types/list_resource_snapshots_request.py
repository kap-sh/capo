"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#ListResourceSnapshotsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_partnercentral_selling.errors import DeserializationError

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.aws_account
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.page_size
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type


class ListResourceSnapshotsRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog related to the request. </p>"""
    max_results: "capo_partnercentral_selling.types.page_size.PageSize"
    """<p> The maximum number of results to return in a single call. </p>"""
    next_token: NotRequired["str"]
    """<p> The token for the next set of results. </p>"""
    engagement_identifier: (
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    )
    """<p> The unique identifier of the engagement associated with the snapshots. </p>"""
    resource_type: NotRequired[
        "capo_partnercentral_selling.types.resource_type.ResourceType"
    ]
    """<p> Filters the response to include only snapshots of the specified resource type. </p>"""
    resource_identifier: NotRequired[
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    ]
    """<p> Filters the response to include only snapshots of the specified resource. </p>"""
    resource_snapshot_template_identifier: NotRequired[
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    ]
    """<p>Filters the response to include only snapshots created using the specified template.</p>"""
    created_by: NotRequired["capo_partnercentral_selling.types.aws_account.AwsAccount"]
    """<p>Filters the response to include only snapshots of resources owned by the specified AWS account. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListResourceSnapshotsRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["MaxResults"] = value.get("max_results", 100)
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    if "resource_type" in value:
        import capo_partnercentral_selling.types.resource_type

        out["ResourceType"] = (
            capo_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
                value["resource_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "resource_snapshot_template_identifier" in value:
        out["ResourceSnapshotTemplateIdentifier"] = value[
            "resource_snapshot_template_identifier"
        ]
    if "created_by" in value:
        out["CreatedBy"] = value["created_by"]
    return out


def deserialize_aws_json_1_0(data: dict) -> ListResourceSnapshotsRequest:
    out: ListResourceSnapshotsRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        raise DeserializationError("ListResourceSnapshotsRequest.catalog required")
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    else:
        out["max_results"] = 100
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("EngagementIdentifier") is not None:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        raise DeserializationError(
            "ListResourceSnapshotsRequest.engagement_identifier required"
        )
    if data.get("ResourceType") is not None:
        import capo_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            capo_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("ResourceSnapshotTemplateIdentifier") is not None:
        out["resource_snapshot_template_identifier"] = data[
            "ResourceSnapshotTemplateIdentifier"
        ]
    if data.get("CreatedBy") is not None:
        out["created_by"] = data["CreatedBy"]
    return out


def redact_sensitive(value: ListResourceSnapshotsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "created_by" in value:
        out["created_by"] = "*** Sensitive Data Redacted ***"
    return out
