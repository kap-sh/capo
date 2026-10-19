"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseUsageRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.arn


class GetLicenseUsageRequest(TypedDict, closed=True):
    license_arn: "capo_license_manager.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the license.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseUsageRequest) -> dict:
    out: dict = {}
    out["LicenseArn"] = value["license_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseUsageRequest:
    out: GetLicenseUsageRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseArn") is not None:
        out["license_arn"] = data["LicenseArn"]
    else:
        out["license_arn"] = ""
    return out
