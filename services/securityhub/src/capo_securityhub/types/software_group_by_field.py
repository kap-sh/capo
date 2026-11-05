"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareGroupByField``."""

from typing import Literal, TypeAlias, cast

"""<p>The software or resource field to group statistics by.</p>"""
SoftwareGroupByField: TypeAlias = Literal[
    "AccountId",
    "PackageName",
    "PackageVersion",
    "PackageType",
    "Region",
    "ResourceRegion",
    "ResourceType",
    "ResourceId",
    "ResourceProvider",
    "ResourceOwnerAccountId",
    "ResourceOwnerOrgId",
    "ResourceCloudPartition",
]


# --- restJson1 ser/de ---
def serialize_json(value: SoftwareGroupByField) -> str:
    return value


def deserialize_json(data: str) -> SoftwareGroupByField:
    return cast(SoftwareGroupByField, data)
