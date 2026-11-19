"""Generated from Smithy shape ``com.amazonaws.lightsail#ResourceType``."""

from typing import Literal, TypeAlias, cast

ResourceType: TypeAlias = Literal[
    "ContainerService",
    "Instance",
    "StaticIp",
    "KeyPair",
    "InstanceSnapshot",
    "Domain",
    "PeeredVpc",
    "LoadBalancer",
    "LoadBalancerTlsCertificate",
    "Disk",
    "DiskSnapshot",
    "RelationalDatabase",
    "RelationalDatabaseSnapshot",
    "ExportSnapshotRecord",
    "CloudFormationStackRecord",
    "Alarm",
    "ContactMethod",
    "Distribution",
    "Certificate",
    "Bucket",
    "Subdomain",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ResourceType) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ResourceType:
    return cast(ResourceType, data)
