"""Generated from Smithy shape ``com.amazonaws.partnercentralselling#CreateResourceSnapshotJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_partnercentral_selling.types.catalog_identifier
    import capo_partnercentral_selling.types.client_token
    import capo_partnercentral_selling.types.engagement_identifier
    import capo_partnercentral_selling.types.resource_identifier
    import capo_partnercentral_selling.types.resource_template_name
    import capo_partnercentral_selling.types.resource_type
    import capo_partnercentral_selling.types.tag_list


class CreateResourceSnapshotJobRequest(TypedDict, closed=True):
    catalog: "capo_partnercentral_selling.types.catalog_identifier.CatalogIdentifier"
    """<p>Specifies the catalog in which to create the snapshot job. Valid values are <code>AWS</code> and <code> Sandbox</code>.</p>"""
    client_token: "capo_partnercentral_selling.types.client_token.ClientToken"
    """<p>A client-generated UUID used for idempotency check. The token helps prevent duplicate job creations.</p>"""
    engagement_identifier: (
        "capo_partnercentral_selling.types.engagement_identifier.EngagementIdentifier"
    )
    """<p>Specifies the identifier of the engagement associated with the resource to be snapshotted.</p>"""
    resource_type: "capo_partnercentral_selling.types.resource_type.ResourceType"
    """<p>The type of resource for which the snapshot job is being created. Must be one of the supported resource types i.e. <code>Opportunity</code> </p>"""
    resource_identifier: (
        "capo_partnercentral_selling.types.resource_identifier.ResourceIdentifier"
    )
    """<p>Specifies the identifier of the specific resource to be snapshotted. The format depends on the <code> ResourceType</code>.</p>"""
    resource_snapshot_template_identifier: (
        "capo_partnercentral_selling.types.resource_template_name.ResourceTemplateName"
    )
    """<p>Specifies the name of the template that defines the schema for the snapshot.</p>"""
    tags: NotRequired["capo_partnercentral_selling.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateResourceSnapshotJobRequest) -> dict:
    out: dict = {}
    out["Catalog"] = value["catalog"]
    out["ClientToken"] = value["client_token"]
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
    if "tags" in value:
        import capo_partnercentral_selling.types.tag_list

        out["Tags"] = capo_partnercentral_selling.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateResourceSnapshotJobRequest:
    out: CreateResourceSnapshotJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("Catalog") is not None:
        out["catalog"] = data["Catalog"]
    else:
        out["catalog"] = ""
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    else:
        out["client_token"] = ""
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
    if data.get("Tags") is not None:
        import capo_partnercentral_selling.types.tag_list

        out["tags"] = (
            capo_partnercentral_selling.types.tag_list.deserialize_aws_json_1_0(
                data["Tags"]
            )
        )
    return out
