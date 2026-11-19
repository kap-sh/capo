"""Generated from Smithy shape ``com.amazonaws.fms#ThirdPartyFirewallPolicy``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.firewall_deployment_model


class ThirdPartyFirewallPolicy(TypedDict, closed=True):
    firewall_deployment_model: NotRequired[
        "capo_fms.types.firewall_deployment_model.FirewallDeploymentModel"
    ]
    """<p>Defines the deployment model to use for the third-party firewall policy.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ThirdPartyFirewallPolicy) -> dict:
    out: dict = {}
    if "firewall_deployment_model" in value:
        import capo_fms.types.firewall_deployment_model

        out["FirewallDeploymentModel"] = (
            capo_fms.types.firewall_deployment_model.serialize_aws_json_1_1(
                value["firewall_deployment_model"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ThirdPartyFirewallPolicy:
    out: ThirdPartyFirewallPolicy = {}  # type: ignore[typeddict-item]
    if data.get("FirewallDeploymentModel") is not None:
        import capo_fms.types.firewall_deployment_model

        out["firewall_deployment_model"] = (
            capo_fms.types.firewall_deployment_model.deserialize_aws_json_1_1(
                data["FirewallDeploymentModel"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ThirdPartyFirewallPolicy) -> dict:
    out: dict = {}
    if "firewall_deployment_model" in value:
        import capo_fms.types.firewall_deployment_model

        out["FirewallDeploymentModel"] = (
            capo_fms.types.firewall_deployment_model.serialize_cbor(
                value["firewall_deployment_model"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ThirdPartyFirewallPolicy:
    out: ThirdPartyFirewallPolicy = {}  # type: ignore[typeddict-item]
    if data.get("FirewallDeploymentModel") is not None:
        import capo_fms.types.firewall_deployment_model

        out["firewall_deployment_model"] = (
            capo_fms.types.firewall_deployment_model.deserialize_cbor(
                data["FirewallDeploymentModel"]
            )
        )
    return out
