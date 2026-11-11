"""Generated from Smithy shape ``com.amazonaws.ssm#DeregisterDefaultHostManagementConfigurationRequest``."""

from typing_extensions import TypedDict


class DeregisterDefaultHostManagementConfigurationRequest(TypedDict, closed=True):
    pass


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DeregisterDefaultHostManagementConfigurationRequest,
) -> dict:
    out: dict = {}
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DeregisterDefaultHostManagementConfigurationRequest:
    out: DeregisterDefaultHostManagementConfigurationRequest = {}  # type: ignore[typeddict-item]
    return out
