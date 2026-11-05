"""Generated from Smithy shape ``com.amazonaws.securityhub#SoftwareStringField``."""

from typing import Literal, TypeAlias, cast

"""<p>The software or resource field to filter on.</p>"""
SoftwareStringField: TypeAlias = Literal[
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
def serialize_json(value: SoftwareStringField) -> str:
    return value


def deserialize_json(data: str) -> SoftwareStringField:
    return cast(SoftwareStringField, data)
