"""Generated from Smithy shape ``com.amazonaws.licensemanager#DeleteLicenseConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class DeleteLicenseConfigurationRequest(TypedDict, closed=True):
    license_configuration_arn: "capo_license_manager.types.string.String"
    """<p>ID of the license configuration.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DeleteLicenseConfigurationRequest) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DeleteLicenseConfigurationRequest:
    out: DeleteLicenseConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConfigurationArn") is not None:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        out["license_configuration_arn"] = ""
    return out
