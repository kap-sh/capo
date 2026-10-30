"""Generated from Smithy shape ``com.amazonaws.inspector2#GetConfigurationResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.ami_configuration_state
    import capo_inspector2.types.ec2_configuration_state
    import capo_inspector2.types.ecr_configuration_state


class GetConfigurationResponse(TypedDict, closed=True):
    ecr_configuration: NotRequired[
        "capo_inspector2.types.ecr_configuration_state.EcrConfigurationState"
    ]
    """<p>Specifies how the ECR automated re-scan duration is currently configured for your environment.</p>"""
    ec2_configuration: NotRequired[
        "capo_inspector2.types.ec2_configuration_state.Ec2ConfigurationState"
    ]
    """<p>Specifies how the Amazon EC2 automated scan mode is currently configured for your environment.</p>"""
    ami_configuration: NotRequired[
        "capo_inspector2.types.ami_configuration_state.AmiConfigurationState"
    ]
    """<p>The current state of the Amazon Machine Image (AMI) scan configuration for the account.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetConfigurationResponse) -> dict:
    out: dict = {}
    if "ecr_configuration" in value:
        import capo_inspector2.types.ecr_configuration_state

        out["ecrConfiguration"] = (
            capo_inspector2.types.ecr_configuration_state.serialize_json(
                value["ecr_configuration"]
            )
        )
    if "ec2_configuration" in value:
        import capo_inspector2.types.ec2_configuration_state

        out["ec2Configuration"] = (
            capo_inspector2.types.ec2_configuration_state.serialize_json(
                value["ec2_configuration"]
            )
        )
    if "ami_configuration" in value:
        import capo_inspector2.types.ami_configuration_state

        out["amiConfiguration"] = (
            capo_inspector2.types.ami_configuration_state.serialize_json(
                value["ami_configuration"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetConfigurationResponse:
    out: GetConfigurationResponse = {}  # type: ignore[typeddict-item]
    if data.get("ecrConfiguration") is not None:
        import capo_inspector2.types.ecr_configuration_state

        out["ecr_configuration"] = (
            capo_inspector2.types.ecr_configuration_state.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    if data.get("ec2Configuration") is not None:
        import capo_inspector2.types.ec2_configuration_state

        out["ec2_configuration"] = (
            capo_inspector2.types.ec2_configuration_state.deserialize_json(
                data["ec2Configuration"]
            )
        )
    if data.get("amiConfiguration") is not None:
        import capo_inspector2.types.ami_configuration_state

        out["ami_configuration"] = (
            capo_inspector2.types.ami_configuration_state.deserialize_json(
                data["amiConfiguration"]
            )
        )
    return out
