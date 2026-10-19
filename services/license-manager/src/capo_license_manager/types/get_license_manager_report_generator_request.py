"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseManagerReportGeneratorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.string


class GetLicenseManagerReportGeneratorRequest(TypedDict, closed=True):
    license_manager_report_generator_arn: "capo_license_manager.types.string.String"
    """<p>Amazon Resource Name (ARN) of the report generator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseManagerReportGeneratorRequest) -> dict:
    out: dict = {}
    out["LicenseManagerReportGeneratorArn"] = value[
        "license_manager_report_generator_arn"
    ]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseManagerReportGeneratorRequest:
    out: GetLicenseManagerReportGeneratorRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseManagerReportGeneratorArn") is not None:
        out["license_manager_report_generator_arn"] = data[
            "LicenseManagerReportGeneratorArn"
        ]
    else:
        out["license_manager_report_generator_arn"] = ""
    return out
