"""Generated from Smithy shape ``com.amazonaws.inspector2#ImageLayerAggregationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.non_empty_string
    import capo_inspector2.types.severity_counts


class ImageLayerAggregationResponse(TypedDict, closed=True):
    repository: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The repository the layer resides in.</p>"""
    resource_id: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The resource ID of the container image layer.</p>"""
    layer_hash: "capo_inspector2.types.non_empty_string.NonEmptyString"
    """<p>The layer hash.</p>"""
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The ID of the Amazon Web Services account that owns the container image hosting the layer image.</p>"""
    cloud_provider: NotRequired["str"]
    """<p>The cloud service provider associated with this image layer aggregation. Valid values:</p> <ul> <li> <p> <code>AWS</code> – Findings from Amazon Web Services resources.</p> </li> <li> <p> <code>AZURE</code> – Findings from Microsoft Azure resources.</p> </li> </ul>"""
    cloud_account_id: NotRequired["str"]
    """<p>The cloud account ID for the image layer aggregation.</p>"""
    cloud_org_id: NotRequired["str"]
    """<p>The cloud organization ID for the image layer aggregation.</p>"""
    cloud_region: NotRequired["str"]
    """<p>The cloud Region associated with this image layer aggregation. The value format depends on the cloud provider:</p> <ul> <li> <p>An Amazon Web Services Region, such as <code>us-east-1</code>.</p> </li> <li> <p>An Azure region, such as <code>eastus</code>.</p> </li> </ul>"""
    cloud_partition: NotRequired["str"]
    """<p>The cloud infrastructure partition associated with this image layer aggregation. Valid values:</p> <ul> <li> <p> <code>aws</code> – Amazon Web Services commercial Regions.</p> </li> <li> <p> <code>aws-cn</code> – Amazon Web Services China Regions.</p> </li> <li> <p> <code>aws-us-gov</code> – Amazon Web Services GovCloud (US) Regions.</p> </li> <li> <p> <code>AzureCloud</code> – Azure commercial Regions.</p> </li> </ul>"""
    severity_counts: NotRequired["capo_inspector2.types.severity_counts.SeverityCounts"]
    """<p>An object that represents the count of matched findings per severity.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImageLayerAggregationResponse) -> dict:
    out: dict = {}
    out["repository"] = value["repository"]
    out["resourceId"] = value["resource_id"]
    out["layerHash"] = value["layer_hash"]
    out["accountId"] = value["account_id"]
    if "cloud_provider" in value:
        out["cloudProvider"] = value["cloud_provider"]
    if "cloud_account_id" in value:
        out["cloudAccountId"] = value["cloud_account_id"]
    if "cloud_org_id" in value:
        out["cloudOrgId"] = value["cloud_org_id"]
    if "cloud_region" in value:
        out["cloudRegion"] = value["cloud_region"]
    if "cloud_partition" in value:
        out["cloudPartition"] = value["cloud_partition"]
    if "severity_counts" in value:
        import capo_inspector2.types.severity_counts

        out["severityCounts"] = capo_inspector2.types.severity_counts.serialize_json(
            value["severity_counts"]
        )
    return out


def deserialize_json(data: dict) -> ImageLayerAggregationResponse:
    out: ImageLayerAggregationResponse = {}  # type: ignore[typeddict-item]
    if data.get("repository") is not None:
        out["repository"] = data["repository"]
    else:
        out["repository"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("layerHash") is not None:
        out["layer_hash"] = data["layerHash"]
    else:
        out["layer_hash"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("cloudProvider") is not None:
        out["cloud_provider"] = data["cloudProvider"]
    if data.get("cloudAccountId") is not None:
        out["cloud_account_id"] = data["cloudAccountId"]
    if data.get("cloudOrgId") is not None:
        out["cloud_org_id"] = data["cloudOrgId"]
    if data.get("cloudRegion") is not None:
        out["cloud_region"] = data["cloudRegion"]
    if data.get("cloudPartition") is not None:
        out["cloud_partition"] = data["cloudPartition"]
    if data.get("severityCounts") is not None:
        import capo_inspector2.types.severity_counts

        out["severity_counts"] = capo_inspector2.types.severity_counts.deserialize_json(
            data["severityCounts"]
        )
    return out
