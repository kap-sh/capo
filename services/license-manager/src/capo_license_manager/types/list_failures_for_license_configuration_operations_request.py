"""Generated from Smithy shape ``com.amazonaws.licensemanager#ListFailuresForLicenseConfigurationOperationsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.box_integer
    import capo_license_manager.types.string


class ListFailuresForLicenseConfigurationOperationsRequest(TypedDict, closed=True):
    license_configuration_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name of the license configuration.</p>"""
    max_results: NotRequired["capo_license_manager.types.box_integer.BoxInteger"]
    """<p>Maximum number of results to return in a single call.</p>"""
    next_token: NotRequired["capo_license_manager.types.string.String"]
    """<p>Token for the next set of results.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: ListFailuresForLicenseConfigurationOperationsRequest,
) -> dict:
    out: dict = {}
    out["LicenseConfigurationArn"] = value["license_configuration_arn"]
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> ListFailuresForLicenseConfigurationOperationsRequest:
    out: ListFailuresForLicenseConfigurationOperationsRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConfigurationArn") is not None:
        out["license_configuration_arn"] = data["LicenseConfigurationArn"]
    else:
        out["license_configuration_arn"] = ""
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
