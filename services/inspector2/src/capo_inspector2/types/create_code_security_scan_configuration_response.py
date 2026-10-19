"""Generated from Smithy shape ``com.amazonaws.inspector2#CreateCodeSecurityScanConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.scan_configuration_arn


class CreateCodeSecurityScanConfigurationResponse(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the created scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCodeSecurityScanConfigurationResponse) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> CreateCodeSecurityScanConfigurationResponse:
    out: CreateCodeSecurityScanConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
    return out
