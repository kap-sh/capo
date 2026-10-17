"""Generated from Smithy shape ``com.amazonaws.securityhub#ResourceGroupByField``."""

from typing import Literal, TypeAlias, cast

ResourceGroupByField: TypeAlias = Literal[
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
    "ResourceSubCategory",
    "DiscoveryType",
    "ResourceInfo.AIDetails.HostResourceType",
    "ResourceInfo.AIDetails.CanonicalId",
]


# --- restJson1 ser/de ---
def serialize_json(value: ResourceGroupByField) -> str:
    return value


def deserialize_json(data: str) -> ResourceGroupByField:
    return cast(ResourceGroupByField, data)
