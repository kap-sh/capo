"""Generated from Smithy shape ``com.amazonaws.inspector2#ImageLayerAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.image_layer_sort_by
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class ImageLayerAggregation(TypedDict, closed=True):
    repositories: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The repository associated with the container image hosting the layers.</p>"""
    resource_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The ID of the container image layer.</p>"""
    layer_hashes: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The hashes associated with the layers.</p>"""
    cloud_providers: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud providers to aggregate findings for. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> <li> <p> <code>GCP</code> – Findings from Google Cloud Platform (GCP) resources.</p> </li> </ul>"""
    cloud_account_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud account IDs to aggregate findings for.</p>"""
    cloud_org_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud organization IDs to aggregate findings for.</p>"""
    cloud_regions: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud regions to aggregate findings for. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> <li> <p>A Google Cloud Platform (GCP) location, such as the region <code>us-central1</code> or the zone <code>us-central1-a</code>.</p> </li> </ul>"""
    cloud_partitions: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud partitions to aggregate findings for. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by.</p>"""
    sort_by: NotRequired["capo_inspector2.types.image_layer_sort_by.ImageLayerSortBy"]
    """<p>The value to sort results by.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLayerAggregation) -> dict:
    out: dict = {}
    if "repositories" in value:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["repositories"]
        )
    if "resource_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "layer_hashes" in value:
        import capo_inspector2.types.string_filter_list

        out["layerHashes"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["layer_hashes"]
        )
    if "cloud_providers" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudProviders"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["cloud_providers"]
        )
    if "cloud_account_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudAccountIds"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["cloud_account_ids"]
            )
        )
    if "cloud_org_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudOrgIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["cloud_org_ids"]
        )
    if "cloud_regions" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudRegions"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["cloud_regions"]
        )
    if "cloud_partitions" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudPartitions"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["cloud_partitions"]
            )
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> ImageLayerAggregation:
    out: ImageLayerAggregation = {}  # type: ignore[typeddict-item]
    if data.get("repositories") is not None:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["repositories"]
        )
    if data.get("resourceIds") is not None:
        import capo_inspector2.types.string_filter_list

        out["resource_ids"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["resourceIds"]
        )
    if data.get("layerHashes") is not None:
        import capo_inspector2.types.string_filter_list

        out["layer_hashes"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["layerHashes"]
        )
    if data.get("cloudProviders") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_providers"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudProviders"]
            )
        )
    if data.get("cloudAccountIds") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_account_ids"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudAccountIds"]
            )
        )
    if data.get("cloudOrgIds") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_org_ids"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudOrgIds"]
            )
        )
    if data.get("cloudRegions") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_regions"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudRegions"]
            )
        )
    if data.get("cloudPartitions") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_partitions"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudPartitions"]
            )
        )
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    return out
