"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#ServiceTopologyEdgeSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.aws_account_id
    import capo_resiliencehubv2.types.aws_region
    import capo_resiliencehubv2.types.edge_property_list


class ServiceTopologyEdgeSummary(TypedDict, closed=True):
    source_resource_identifier: "str"
    """<p>The identifier of the source resource.</p>"""
    destination_resource_identifier: "str"
    """<p>The identifier of the destination resource.</p>"""
    source_region: NotRequired["capo_resiliencehubv2.types.aws_region.AwsRegion"]
    """<p>The AWS Region of the source resource.</p>"""
    destination_region: NotRequired["capo_resiliencehubv2.types.aws_region.AwsRegion"]
    """<p>The AWS Region of the destination resource.</p>"""
    source_account: NotRequired[
        "capo_resiliencehubv2.types.aws_account_id.AwsAccountId"
    ]
    """<p>The AWS account ID of the source resource.</p>"""
    destination_account: NotRequired[
        "capo_resiliencehubv2.types.aws_account_id.AwsAccountId"
    ]
    """<p>The AWS account ID of the destination resource.</p>"""
    properties: NotRequired[
        "capo_resiliencehubv2.types.edge_property_list.EdgePropertyList"
    ]
    """<p>The properties of the topology edge.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ServiceTopologyEdgeSummary) -> dict:
    out: dict = {}
    out["sourceResourceIdentifier"] = value["source_resource_identifier"]
    out["destinationResourceIdentifier"] = value["destination_resource_identifier"]
    if "source_region" in value:
        out["sourceRegion"] = value["source_region"]
    if "destination_region" in value:
        out["destinationRegion"] = value["destination_region"]
    if "source_account" in value:
        out["sourceAccount"] = value["source_account"]
    if "destination_account" in value:
        out["destinationAccount"] = value["destination_account"]
    if "properties" in value:
        import capo_resiliencehubv2.types.edge_property_list

        out["properties"] = (
            capo_resiliencehubv2.types.edge_property_list.serialize_json(
                value["properties"]
            )
        )
    return out


def deserialize_json(data: dict) -> ServiceTopologyEdgeSummary:
    out: ServiceTopologyEdgeSummary = {}  # type: ignore[typeddict-item]
    if data.get("sourceResourceIdentifier") is not None:
        out["source_resource_identifier"] = data["sourceResourceIdentifier"]
    else:
        out["source_resource_identifier"] = ""
    if data.get("destinationResourceIdentifier") is not None:
        out["destination_resource_identifier"] = data["destinationResourceIdentifier"]
    else:
        out["destination_resource_identifier"] = ""
    if data.get("sourceRegion") is not None:
        out["source_region"] = data["sourceRegion"]
    if data.get("destinationRegion") is not None:
        out["destination_region"] = data["destinationRegion"]
    if data.get("sourceAccount") is not None:
        out["source_account"] = data["sourceAccount"]
    if data.get("destinationAccount") is not None:
        out["destination_account"] = data["destinationAccount"]
    if data.get("properties") is not None:
        import capo_resiliencehubv2.types.edge_property_list

        out["properties"] = (
            capo_resiliencehubv2.types.edge_property_list.deserialize_json(
                data["properties"]
            )
        )
    return out
