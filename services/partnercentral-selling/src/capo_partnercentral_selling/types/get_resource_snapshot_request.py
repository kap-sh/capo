"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#GetResourceSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_snapshot_revision
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type


class GetResourceSnapshotRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog related to the request. Valid values are:</p> <ul> <li> <p>AWS: Retrieves the snapshot from the production AWS environment.</p> </li> <li> <p>Sandbox: Retrieves the snapshot from a sandbox environment used for testing or development purposes.</p> </li> </ul>"""
    engagement_identifier: (
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    )
    """<p>The unique identifier of the engagement associated with the snapshot. This field links the snapshot to a specific engagement context.</p>"""
    resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType"
    """<p>Specifies the type of resource that was snapshotted. This field determines the structure and content of the snapshot payload. Valid value includes:<code>Opportunity</code>: For opportunity-related data. </p>"""
    resource_identifier: (
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    )
    """<p>The unique identifier of the specific resource that was snapshotted. The format and constraints of this identifier depend on the ResourceType specified. For <code>Opportunity</code> type, it will be an <code>opportunity ID</code> </p>"""
    resource_snapshot_template_identifier: (
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    )
    """<p>he name of the template that defines the schema for the snapshot. This template determines which subset of the resource data is included in the snapshot and must correspond to an existing and valid template for the specified <code>ResourceType</code>.</p>"""
    revision: NotRequired[
        "capo_partnercentral_selling.types.resource_snapshot_revision.ResourceSnapshotRevision"
    ]
    """<p>Specifies which revision of the snapshot to retrieve. If omitted returns the latest revision.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetResourceSnapshotRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["EngagementIdentifier"] = value["engagement_identifier"]
    import capo_partnercentral_selling.types.resource_type

    out["ResourceType"] = (
        capo_partnercentral_selling.types.resource_type.serialize_aws_json_1_0(
            value["resource_type"]
        )
    )
    out["ResourceIdentifier"] = value["resource_identifier"]
    out["ResourceSnapshotTemplateIdentifier"] = value[
        "resource_snapshot_template_identifier"
    ]
    if "revision" in value:
        out["Revision"] = value["revision"]
    return out


def deserialize_aws_json_1_0(data: dict) -> GetResourceSnapshotRequest:
    out: GetResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("EngagementIdentifier") is not None:
        out["engagement_identifier"] = data["EngagementIdentifier"]
    else:
        out["engagement_identifier"] = ""
    if data.get("ResourceType") is not None:
        import capo_partnercentral_selling.types.resource_type

        out["resource_type"] = (
            capo_partnercentral_selling.types.resource_type.deserialize_aws_json_1_0(
                data["ResourceType"]
            )
        )
    else:
        import typing

        out["resource_type"] = typing.cast(
            "capo_partnercentral_selling.types.resource_type.ResourceType", ""
        )
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    else:
        out["resource_identifier"] = ""
    if data.get("ResourceSnapshotTemplateIdentifier") is not None:
        out["resource_snapshot_template_identifier"] = data[
            "ResourceSnapshotTemplateIdentifier"
        ]
    else:
        out["resource_snapshot_template_identifier"] = ""
    if data.get("Revision") is not None:
        out["revision"] = data["Revision"]
    return out
