"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateCodeSecurityScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_inspector2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_inspector2.types.code_security_scan_configuration
    import capo_inspector2.types.scan_configuration_arn


class UpdateCodeSecurityScanConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.scan_configuration_arn.ScanConfigurationArn"
    )
    """<p>The Amazon Resource Name (ARN) of the scan configuration to update.</p>"""
    configuration: "capo_inspector2.types.code_security_scan_configuration.CodeSecurityScanConfiguration"
    """<p>The updated configuration settings for the code security scan.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCodeSecurityScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    import capo_inspector2.types.code_security_scan_configuration

    out["configuration"] = (
        capo_inspector2.types.code_security_scan_configuration.serialize_json(
            value["configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> UpdateCodeSecurityScanConfigurationRequest:
    out: UpdateCodeSecurityScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
    if data.get("configuration") is not None:
        import capo_inspector2.types.code_security_scan_configuration

        out["configuration"] = (
            capo_inspector2.types.code_security_scan_configuration.deserialize_json(
                data["configuration"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateCodeSecurityScanConfigurationRequest.configuration required"
        )
    return out
