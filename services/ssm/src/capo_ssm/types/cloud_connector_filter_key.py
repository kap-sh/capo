"""Generated from Smithy shape ``com.amazonaws.ssm#CloudConnectorFilterKey``."""

from typing import Literal, TypeAlias, cast

CloudConnectorFilterKey: TypeAlias = Literal[
    "SubscriptionId",
    "TenantId",
    "ProjectId",
    "OrganizationId",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CloudConnectorFilterKey) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> CloudConnectorFilterKey:
    return cast(CloudConnectorFilterKey, data)
