"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterDefaultHostManagementConfigurationResult``."""

from typing_extensions import TypedDict


class DeregisterDefaultHostManagementConfigurationResult(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeregisterDefaultHostManagementConfigurationResult,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeregisterDefaultHostManagementConfigurationResult:
    out: DeregisterDefaultHostManagementConfigurationResult = {}  # type: ignore[typeddict-item]
    return out
