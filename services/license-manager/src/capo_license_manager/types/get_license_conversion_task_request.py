"""Generated from Smithy shape ``com.amazonaws.licensemanager#GetLicenseConversionTaskRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_license_manager.types.license_conversion_task_id


class GetLicenseConversionTaskRequest(TypedDict, closed=True):
    license_conversion_task_id: (
        "capo_license_manager.types.license_conversion_task_id.LicenseConversionTaskId"
    )
    """<p>ID of the license type conversion task to retrieve information on.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetLicenseConversionTaskRequest) -> dict:
    out: dict = {}
    out["LicenseConversionTaskId"] = value["license_conversion_task_id"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetLicenseConversionTaskRequest:
    out: GetLicenseConversionTaskRequest = {}  # type: ignore[typeddict-item]
    if data.get("LicenseConversionTaskId") is not None:
        out["license_conversion_task_id"] = data["LicenseConversionTaskId"]
    else:
        out["license_conversion_task_id"] = ""
    return out
