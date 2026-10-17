"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourcesStringField``."""

from typing import Literal, TypeAlias, cast

ResourcesStringField: TypeAlias = Literal[
    "ResourceGuid",
    "ResourceId",
    "AccountId",
    "AccountName",
    "Region",
    "ResourceProvider",
    "ResourceOwnerAccountId",
    "ResourceOwnerOrgId",
    "ResourceCloudPartition",
    "ResourceRegion",
    "ResourceCategory",
    "ResourceType",
    "ResourceName",
    "FindingsSummary.FindingType",
    "FindingsSummary.ProductName",
    "ResourceSubCategory",
    "DiscoveryType",
    "ResourceInfo.AIDetails.HostResourceGuid",
    "ResourceInfo.AIDetails.HostResourceType",
    "ResourceInfo.AIDetails.CanonicalId",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourcesStringField) -> str:
    return value


def deserialize_json(data: str) -> ResourcesStringField:
    return cast(ResourcesStringField, data)
