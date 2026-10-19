"""Generated from Smithy shape ``com.amazonaws.inspector2#DeleteCisScanConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.cis_scan_configuration_arn


class DeleteCisScanConfigurationRequest(TypedDict, closed=True):
    scan_configuration_arn: (
        "capo_inspector2.types.cis_scan_configuration_arn.CisScanConfigurationArn"
    )
    """<p>The ARN of the CIS scan configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteCisScanConfigurationRequest) -> dict:
    out: dict = {}
    out["scanConfigurationArn"] = value["scan_configuration_arn"]
    return out


def deserialize_json(data: dict) -> DeleteCisScanConfigurationRequest:
    out: DeleteCisScanConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("scanConfigurationArn") is not None:
        out["scan_configuration_arn"] = data["scanConfigurationArn"]
    else:
        out["scan_configuration_arn"] = ""
    return out
