"""Generated from Smithy shape ``com.amazonaws.inspector2#CoveredResource``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.coverage_resource_type
    import capo_inspector2.types.date_time_timestamp
    import capo_inspector2.types.provider
    import capo_inspector2.types.provider_account_id
    import capo_inspector2.types.provider_org_id
    import capo_inspector2.types.provider_partition
    import capo_inspector2.types.provider_region
    import capo_inspector2.types.resource_id
    import capo_inspector2.types.resource_scan_metadata
    import capo_inspector2.types.scan_mode
    import capo_inspector2.types.scan_status
    import capo_inspector2.types.scan_type


class CoveredResource(TypedDict, closed=True):
    resource_type: "capo_inspector2.types.coverage_resource_type.CoverageResourceType"
    """<p>The type of the covered resource.</p>"""
    resource_id: "capo_inspector2.types.resource_id.ResourceId"
    """<p>The ID of the covered resource.</p>"""
    account_id: "capo_inspector2.types.account_id.AccountId"
    """<p>The Amazon Web Services account ID of the covered resource.</p>"""
    scan_type: "capo_inspector2.types.scan_type.ScanType"
    """<p>The Amazon Inspector scan type covering the resource.</p>"""
    scan_status: NotRequired["capo_inspector2.types.scan_status.ScanStatus"]
    """<p>The status of the scan covering the resource.</p>"""
    resource_metadata: NotRequired[
        "capo_inspector2.types.resource_scan_metadata.ResourceScanMetadata"
    ]
    """<p>An object that contains details about the metadata.</p>"""
    last_scanned_at: NotRequired[
        "capo_inspector2.types.date_time_timestamp.DateTimeTimestamp"
    ]
    """<p>The date and time the resource was last checked for vulnerabilities.</p>"""
    scan_mode: NotRequired["capo_inspector2.types.scan_mode.ScanMode"]
    """<p>The scan method that is applied to the instance.</p>"""
    provider: NotRequired["capo_inspector2.types.provider.Provider"]
    """<p>The cloud provider of the covered resource.</p>"""
    provider_account_id: NotRequired[
        "capo_inspector2.types.provider_account_id.ProviderAccountId"
    ]
    """<p>The cloud provider account ID of the covered resource.</p>"""
    provider_org_id: NotRequired["capo_inspector2.types.provider_org_id.ProviderOrgId"]
    """<p>The cloud provider organization ID of the covered resource.</p>"""
    provider_region: NotRequired["capo_inspector2.types.provider_region.ProviderRegion"]
    """<p>The cloud provider region of the covered resource.</p>"""
    provider_partition: NotRequired[
        "capo_inspector2.types.provider_partition.ProviderPartition"
    ]
    """<p>The cloud provider partition of the covered resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CoveredResource) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    out["resourceId"] = value["resource_id"]
    out["accountId"] = value["account_id"]
    out["scanType"] = value["scan_type"]
    if "scan_status" in value:
        import capo_inspector2.types.scan_status

        out["scanStatus"] = capo_inspector2.types.scan_status.serialize_json(
            value["scan_status"]
        )
    if "resource_metadata" in value:
        import capo_inspector2.types.resource_scan_metadata

        out["resourceMetadata"] = (
            capo_inspector2.types.resource_scan_metadata.serialize_json(
                value["resource_metadata"]
            )
        )
    if "last_scanned_at" in value:
        import capo_inspector2.types.date_time_timestamp

        out["lastScannedAt"] = capo_inspector2.types.date_time_timestamp.serialize_json(
            value["last_scanned_at"]
        )
    if "scan_mode" in value:
        out["scanMode"] = value["scan_mode"]
    if "provider" in value:
        out["provider"] = value["provider"]
    if "provider_account_id" in value:
        out["providerAccountId"] = value["provider_account_id"]
    if "provider_org_id" in value:
        out["providerOrgId"] = value["provider_org_id"]
    if "provider_region" in value:
        out["providerRegion"] = value["provider_region"]
    if "provider_partition" in value:
        out["providerPartition"] = value["provider_partition"]
    return out


def deserialize_json(data: dict) -> CoveredResource:
    out: CoveredResource = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        out["resource_type"] = ""
    if data.get("resourceId") is not None:
        out["resource_id"] = data["resourceId"]
    else:
        out["resource_id"] = ""
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    else:
        out["account_id"] = ""
    if data.get("scanType") is not None:
        out["scan_type"] = data["scanType"]
    else:
        out["scan_type"] = ""
    if data.get("scanStatus") is not None:
        import capo_inspector2.types.scan_status

        out["scan_status"] = capo_inspector2.types.scan_status.deserialize_json(
            data["scanStatus"]
        )
    if data.get("resourceMetadata") is not None:
        import capo_inspector2.types.resource_scan_metadata

        out["resource_metadata"] = (
            capo_inspector2.types.resource_scan_metadata.deserialize_json(
                data["resourceMetadata"]
            )
        )
    if data.get("lastScannedAt") is not None:
        import capo_inspector2.types.date_time_timestamp

        out["last_scanned_at"] = (
            capo_inspector2.types.date_time_timestamp.deserialize_json(
                data["lastScannedAt"]
            )
        )
    if data.get("scanMode") is not None:
        out["scan_mode"] = data["scanMode"]
    if data.get("provider") is not None:
        out["provider"] = data["provider"]
    if data.get("providerAccountId") is not None:
        out["provider_account_id"] = data["providerAccountId"]
    if data.get("providerOrgId") is not None:
        out["provider_org_id"] = data["providerOrgId"]
    if data.get("providerRegion") is not None:
        out["provider_region"] = data["providerRegion"]
    if data.get("providerPartition") is not None:
        out["provider_partition"] = data["providerPartition"]
    return out
