"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateResourceSnapshotRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type


class CreateResourceSnapshotRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p> Specifies the catalog where the snapshot is created. Valid values are <code>AWS</code> and <code>Sandbox</code>. </p>"""
    engagement_identifier: (
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    )
    """<p> The unique identifier of the engagement associated with this snapshot. This field links the snapshot to a specific engagement context. </p>"""
    resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType"
    """<p> Specifies the type of resource for which the snapshot is being created. This field determines the structure and content of the snapshot. Must be one of the supported resource types, such as: <code>Opportunity</code>. </p>"""
    resource_identifier: (
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    )
    """<p> The unique identifier of the specific resource to be snapshotted. The format and constraints of this identifier depend on the <code>ResourceType</code> specified. For example: For <code>Opportunity</code> type, it will be an opportunity ID. </p>"""
    resource_snapshot_template_identifier: (
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    )
    """<p> The name of the template that defines the schema for the snapshot. This template determines which subset of the resource data will be included in the snapshot. Must correspond to an existing and valid template for the specified <code>ResourceType</code>. </p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p> Specifies a unique, client-generated UUID to ensure that the request is handled exactly once. This token helps prevent duplicate snapshot creations. </p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceSnapshotRequest) -> dict:
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
    out["ClientToken"] = value["client_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceSnapshotRequest:
    out: CreateResourceSnapshotRequest = {}  # type: ignore[typeddict-item]
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
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
    return out
