"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#LicenseSpecification``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.license_configuration_arn


class LicenseSpecification(TypedDict, closed=True):
    license_configuration_arn: "capo_bedrock_agentcore_control.types.license_configuration_arn.LicenseConfigurationArn"
    """<p>The Amazon Resource Name (ARN) of the license configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LicenseSpecification) -> dict:
    out: dict = {}
    out["licenseConfigurationArn"] = value["license_configuration_arn"]
    return out


def deserialize_json(data: dict) -> LicenseSpecification:
    out: LicenseSpecification = {}  # type: ignore[typeddict-item]
    if data.get("licenseConfigurationArn") is not None:
        out["license_configuration_arn"] = data["licenseConfigurationArn"]
    else:
        out["license_configuration_arn"] = ""
    return out
