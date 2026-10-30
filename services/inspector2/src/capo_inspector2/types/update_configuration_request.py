"""Generated from Smithy shape ``com.amazonaws.inspector2#UpdateConfigurationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.account_id
    import capo_inspector2.types.ami_configuration
    import capo_inspector2.types.ec2_configuration
    import capo_inspector2.types.ecr_configuration
    import capo_inspector2.types.update_configuration_inheritance


class UpdateConfigurationRequest(TypedDict, closed=True):
    account_id: NotRequired["capo_inspector2.types.account_id.AccountId"]
    """<p>The 12-digit Amazon Web Services account ID of the member account whose scan configuration you want to update. When specified, you must be the delegated administrator for this member account. If not specified, the operation updates your own configuration and propagates changes to any member accounts that have not been individually configured.</p>"""
    ecr_configuration: NotRequired[
        "capo_inspector2.types.ecr_configuration.EcrConfiguration"
    ]
    """<p>Specifies how the ECR automated re-scan will be updated for your environment.</p>"""
    ec2_configuration: NotRequired[
        "capo_inspector2.types.ec2_configuration.Ec2Configuration"
    ]
    """<p>Specifies how the Amazon EC2 automated scan will be updated for your environment.</p>"""
    ami_configuration: NotRequired[
        "capo_inspector2.types.ami_configuration.AmiConfiguration"
    ]
    """<p>The Amazon Machine Image (AMI) scan configuration to apply to the account.</p>"""
    update_configuration_inheritance: NotRequired[
        "capo_inspector2.types.update_configuration_inheritance.UpdateConfigurationInheritance"
    ]
    """<p>Specifies which scan-type configurations to reset to the delegated administrator's inherited values for the targeted member account. Each member of this structure is independently optional. When specified, <code>ec2Configuration</code> and <code>ecrConfiguration</code> must be absent, and <code>accountId</code> must also be present. Only <code>INHERIT_FROM_ADMIN</code> is valid for each member. If not specified, the operation uses the <code>ec2Configuration</code> and <code>ecrConfiguration</code> parameters instead.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateConfigurationRequest) -> dict:
    out: dict = {}
    if "account_id" in value:
        out["accountId"] = value["account_id"]
    if "ecr_configuration" in value:
        import capo_inspector2.types.ecr_configuration

        out["ecrConfiguration"] = (
            capo_inspector2.types.ecr_configuration.serialize_json(
                value["ecr_configuration"]
            )
        )
    if "ec2_configuration" in value:
        import capo_inspector2.types.ec2_configuration

        out["ec2Configuration"] = (
            capo_inspector2.types.ec2_configuration.serialize_json(
                value["ec2_configuration"]
            )
        )
    if "ami_configuration" in value:
        import capo_inspector2.types.ami_configuration

        out["amiConfiguration"] = (
            capo_inspector2.types.ami_configuration.serialize_json(
                value["ami_configuration"]
            )
        )
    if "update_configuration_inheritance" in value:
        import capo_inspector2.types.update_configuration_inheritance

        out["updateConfigurationInheritance"] = (
            capo_inspector2.types.update_configuration_inheritance.serialize_json(
                value["update_configuration_inheritance"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateConfigurationRequest:
    out: UpdateConfigurationRequest = {}  # type: ignore[typeddict-item]
    if data.get("accountId") is not None:
        out["account_id"] = data["accountId"]
    if data.get("ecrConfiguration") is not None:
        import capo_inspector2.types.ecr_configuration

        out["ecr_configuration"] = (
            capo_inspector2.types.ecr_configuration.deserialize_json(
                data["ecrConfiguration"]
            )
        )
    if data.get("ec2Configuration") is not None:
        import capo_inspector2.types.ec2_configuration

        out["ec2_configuration"] = (
            capo_inspector2.types.ec2_configuration.deserialize_json(
                data["ec2Configuration"]
            )
        )
    if data.get("amiConfiguration") is not None:
        import capo_inspector2.types.ami_configuration

        out["ami_configuration"] = (
            capo_inspector2.types.ami_configuration.deserialize_json(
                data["amiConfiguration"]
            )
        )
    if data.get("updateConfigurationInheritance") is not None:
        import capo_inspector2.types.update_configuration_inheritance

        out["update_configuration_inheritance"] = (
            capo_inspector2.types.update_configuration_inheritance.deserialize_json(
                data["updateConfigurationInheritance"]
            )
        )
    return out
