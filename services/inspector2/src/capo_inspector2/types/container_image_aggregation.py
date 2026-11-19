"""Generated from Smithy shape ``com.amazonaws.inspector2#ContainerImageAggregation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.container_image_sort_by
    import capo_inspector2.types.date_filter_list
    import capo_inspector2.types.number_filter_list
    import capo_inspector2.types.sort_order
    import capo_inspector2.types.string_filter_list


class ContainerImageAggregation(TypedDict, closed=True):
    resource_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The resource IDs to aggregate findings for.</p>"""
    image_digests: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The image digests to aggregate findings for.</p>"""
    repositories: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The image repositories to aggregate findings for.</p>"""
    registries: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The image registries to aggregate findings for.</p>"""
    architectures: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The image architectures to aggregate findings for.</p>"""
    image_tags: NotRequired["capo_inspector2.types.string_filter_list.StringFilterList"]
    """<p>The image tags to aggregate findings for.</p>"""
    cloud_providers: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud providers to aggregate findings for. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> <li> <p> <code>GCP</code> – Findings from Google Cloud Platform (GCP) resources.</p> </li> </ul>"""
    cloud_partitions: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud partitions to aggregate findings for. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""
    cloud_regions: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud regions to aggregate findings for. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> <li> <p>A Google Cloud Platform (GCP) location, such as the region <code>us-central1</code> or the zone <code>us-central1-a</code>.</p> </li> </ul>"""
    cloud_org_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud organization IDs to aggregate findings for.</p>"""
    cloud_account_ids: NotRequired[
        "capo_inspector2.types.string_filter_list.StringFilterList"
    ]
    """<p>The cloud account IDs to aggregate findings for.</p>"""
    last_in_use_at: NotRequired["capo_inspector2.types.date_filter_list.DateFilterList"]
    """<p>The last in-use timestamps to aggregate findings for.</p>"""
    in_use_count: NotRequired[
        "capo_inspector2.types.number_filter_list.NumberFilterList"
    ]
    """<p>The in-use counts to aggregate findings for.</p>"""
    sort_order: NotRequired["capo_inspector2.types.sort_order.SortOrder"]
    """<p>The order to sort results by. Valid values are <code>ASC</code> and <code>DESC</code>.</p>"""
    sort_by: NotRequired[
        "capo_inspector2.types.container_image_sort_by.ContainerImageSortBy"
    ]
    """<p>The value to sort results by. Specify a field name from the aggregation response, such as <code>CRITICAL</code>, <code>HIGH</code>, or <code>ALL</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContainerImageAggregation) -> dict:
    out: dict = {}
    if "resource_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["resourceIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["resource_ids"]
        )
    if "image_digests" in value:
        import capo_inspector2.types.string_filter_list

        out["imageDigests"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["image_digests"]
        )
    if "repositories" in value:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["repositories"]
        )
    if "registries" in value:
        import capo_inspector2.types.string_filter_list

        out["registries"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["registries"]
        )
    if "architectures" in value:
        import capo_inspector2.types.string_filter_list

        out["architectures"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["architectures"]
        )
    if "image_tags" in value:
        import capo_inspector2.types.string_filter_list

        out["imageTags"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["image_tags"]
        )
    if "cloud_providers" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudProviders"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["cloud_providers"]
        )
    if "cloud_partitions" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudPartitions"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["cloud_partitions"]
            )
        )
    if "cloud_regions" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudRegions"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["cloud_regions"]
        )
    if "cloud_org_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudOrgIds"] = capo_inspector2.types.string_filter_list.serialize_json(
            value["cloud_org_ids"]
        )
    if "cloud_account_ids" in value:
        import capo_inspector2.types.string_filter_list

        out["cloudAccountIds"] = (
            capo_inspector2.types.string_filter_list.serialize_json(
                value["cloud_account_ids"]
            )
        )
    if "last_in_use_at" in value:
        import capo_inspector2.types.date_filter_list

        out["lastInUseAt"] = capo_inspector2.types.date_filter_list.serialize_json(
            value["last_in_use_at"]
        )
    if "in_use_count" in value:
        import capo_inspector2.types.number_filter_list

        out["inUseCount"] = capo_inspector2.types.number_filter_list.serialize_json(
            value["in_use_count"]
        )
    if "sort_order" in value:
        out["sortOrder"] = value["sort_order"]
    if "sort_by" in value:
        out["sortBy"] = value["sort_by"]
    return out


def deserialize_json(data: dict) -> ContainerImageAggregation:
    out: ContainerImageAggregation = {}  # type: ignore[typeddict-item]
    if data.get("resourceIds") is not None:
        import capo_inspector2.types.string_filter_list

        out["resource_ids"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["resourceIds"]
        )
    if data.get("imageDigests") is not None:
        import capo_inspector2.types.string_filter_list

        out["image_digests"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["imageDigests"]
            )
        )
    if data.get("repositories") is not None:
        import capo_inspector2.types.string_filter_list

        out["repositories"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["repositories"]
        )
    if data.get("registries") is not None:
        import capo_inspector2.types.string_filter_list

        out["registries"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["registries"]
        )
    if data.get("architectures") is not None:
        import capo_inspector2.types.string_filter_list

        out["architectures"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["architectures"]
            )
        )
    if data.get("imageTags") is not None:
        import capo_inspector2.types.string_filter_list

        out["image_tags"] = capo_inspector2.types.string_filter_list.deserialize_json(
            data["imageTags"]
        )
    if data.get("cloudProviders") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_providers"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudProviders"]
            )
        )
    if data.get("cloudPartitions") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_partitions"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudPartitions"]
            )
        )
    if data.get("cloudRegions") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_regions"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudRegions"]
            )
        )
    if data.get("cloudOrgIds") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_org_ids"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudOrgIds"]
            )
        )
    if data.get("cloudAccountIds") is not None:
        import capo_inspector2.types.string_filter_list

        out["cloud_account_ids"] = (
            capo_inspector2.types.string_filter_list.deserialize_json(
                data["cloudAccountIds"]
            )
        )
    if data.get("lastInUseAt") is not None:
        import capo_inspector2.types.date_filter_list

        out["last_in_use_at"] = capo_inspector2.types.date_filter_list.deserialize_json(
            data["lastInUseAt"]
        )
    if data.get("inUseCount") is not None:
        import capo_inspector2.types.number_filter_list

        out["in_use_count"] = capo_inspector2.types.number_filter_list.deserialize_json(
            data["inUseCount"]
        )
    if data.get("sortOrder") is not None:
        out["sort_order"] = data["sortOrder"]
    if data.get("sortBy") is not None:
        out["sort_by"] = data["sortBy"]
    return out
