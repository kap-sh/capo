"""Generated from Smithy shape ``com.amazonaws.licensemanager#UpdateLicenseSpecificationsForResourceRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_specifications
    import capo_license_manager.types.string


class UpdateLicenseSpecificationsForResourceRequest(TypedDict, closed=True):
    resource_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the Amazon Web Services resource.</p>"""
    add_license_specifications: NotRequired[
        "capo_license_manager.types.license_specifications.LicenseSpecifications"
    ]
    """<p>ARNs of the license configurations to add.</p>"""
    remove_license_specifications: NotRequired[
        "capo_license_manager.types.license_specifications.LicenseSpecifications"
    ]
    """<p>ARNs of the license configurations to remove.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: UpdateLicenseSpecificationsForResourceRequest,
) -> dict:
    out: dict = {}
    out["ResourceArn"] = value["resource_arn"]
    if "add_license_specifications" in value:
        import capo_license_manager.types.license_specifications

        out["AddLicenseSpecifications"] = (
            capo_license_manager.types.license_specifications.serialize_aws_json_1_1(
                value["add_license_specifications"]
            )
        )
    if "remove_license_specifications" in value:
        import capo_license_manager.types.license_specifications

        out["RemoveLicenseSpecifications"] = (
            capo_license_manager.types.license_specifications.serialize_aws_json_1_1(
                value["remove_license_specifications"]
            )
        )
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> UpdateLicenseSpecificationsForResourceRequest:
    out: UpdateLicenseSpecificationsForResourceRequest = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArn") is not None:
        out["resource_arn"] = data["ResourceArn"]
    else:
        out["resource_arn"] = ""
    if data.get("AddLicenseSpecifications") is not None:
        import capo_license_manager.types.license_specifications

        out["add_license_specifications"] = (
            capo_license_manager.types.license_specifications.deserialize_aws_json_1_1(
                data["AddLicenseSpecifications"]
            )
        )
    if data.get("RemoveLicenseSpecifications") is not None:
        import capo_license_manager.types.license_specifications

        out["remove_license_specifications"] = (
            capo_license_manager.types.license_specifications.deserialize_aws_json_1_1(
                data["RemoveLicenseSpecifications"]
            )
        )
    return out
