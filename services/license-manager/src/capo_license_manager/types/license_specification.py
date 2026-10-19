"""Generated from Smithy shape ``com.amazonaws.licensemanager#LicenseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class LicenseSpecification(TypedDict, closed=True):
    license_configuration_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the license configuration.</p>"""
    ami_association_scope: NotRequired["capo_license_manager.types.string.String"]
    """<p>Scope of AMI associations. The possible value is <code>cross-account</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: LicenseSpecification) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    if "ami_association_scope" in value:
        out["AmiAssociationScope"] = value["ami_association_scope"]
    return out


def deserialize_aws_json_1_1(data: dict) -> LicenseSpecification:
    out: LicenseSpecification = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConfigurationArn") is not None:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        out["license_configuration_arn"] = ""
    if data.get("AmiAssociationScope") is not None:
        out["ami_association_scope"] = data["AmiAssociationScope"]
    return out
