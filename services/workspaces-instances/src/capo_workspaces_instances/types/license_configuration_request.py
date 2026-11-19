"""Generated from Smithy shape ``com.amazonaws.workspacesinstances#LicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_workspaces_instances.types.arn


class LicenseConfigurationRequest(TypedDict, closed=True):
    license_configuration_arn: NotRequired["capo_workspaces_instances.types.arn.ARN"]
    """<p>ARN of the license configuration for the WorkSpace Instance.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: LicenseConfigurationRequest) -> dict:
    out: dict = {}
    if "license_configuration_arn" in value:
        out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_aws_json_1_0(data: dict) -> LicenseConfigurationRequest:
    out: LicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConfigurationArn") is not None:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: LicenseConfigurationRequest) -> dict:
    out: dict = {}
    if "license_configuration_arn" in value:
        out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_cbor(data: dict) -> LicenseConfigurationRequest:
    out: LicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConfigurationArn") is not None:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    return out
