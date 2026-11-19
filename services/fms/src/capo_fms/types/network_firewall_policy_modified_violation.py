"""Generated from Smithy shape ``com.amazonaws.fms#NetworkFirewallPolicyModifiedViolation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.network_firewall_policy_description
    import capo_fms.types.violation_target


class NetworkFirewallPolicyModifiedViolation(TypedDict, closed=True):
    violation_target: NotRequired["capo_fms.types.violation_target.ViolationTarget"]
    """<p>The ID of the Network Firewall or VPC resource that's in violation.</p>"""
    current_policy_description: NotRequired[
        "capo_fms.types.network_firewall_policy_description.NetworkFirewallPolicyDescription"
    ]
    """<p>The policy that's currently in use in the individual account. </p>"""
    expected_policy_description: NotRequired[
        "capo_fms.types.network_firewall_policy_description.NetworkFirewallPolicyDescription"
    ]
    """<p>The policy that should be in use in the individual account in order to be compliant. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: NetworkFirewallPolicyModifiedViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "current_policy_description" in value:
        import capo_fms.types.network_firewall_policy_description

        out["CurrentPolicyDescription"] = (
            capo_fms.types.network_firewall_policy_description.serialize_aws_json_1_1(
                value["current_policy_description"]
            )
        )
    if "expected_policy_description" in value:
        import capo_fms.types.network_firewall_policy_description

        out["ExpectedPolicyDescription"] = (
            capo_fms.types.network_firewall_policy_description.serialize_aws_json_1_1(
                value["expected_policy_description"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> NetworkFirewallPolicyModifiedViolation:
    out: NetworkFirewallPolicyModifiedViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("CurrentPolicyDescription") is not None:
        import capo_fms.types.network_firewall_policy_description

        out["current_policy_description"] = (
            capo_fms.types.network_firewall_policy_description.deserialize_aws_json_1_1(
                data["CurrentPolicyDescription"]
            )
        )
    if data.get("ExpectedPolicyDescription") is not None:
        import capo_fms.types.network_firewall_policy_description

        out["expected_policy_description"] = (
            capo_fms.types.network_firewall_policy_description.deserialize_aws_json_1_1(
                data["ExpectedPolicyDescription"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: NetworkFirewallPolicyModifiedViolation) -> dict:
    out: dict = {}
    if "violation_target" in value:
        out["ViolationTarget"] = value["violation_target"]
    if "current_policy_description" in value:
        import capo_fms.types.network_firewall_policy_description

        out["CurrentPolicyDescription"] = (
            capo_fms.types.network_firewall_policy_description.serialize_cbor(
                value["current_policy_description"]
            )
        )
    if "expected_policy_description" in value:
        import capo_fms.types.network_firewall_policy_description

        out["ExpectedPolicyDescription"] = (
            capo_fms.types.network_firewall_policy_description.serialize_cbor(
                value["expected_policy_description"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> NetworkFirewallPolicyModifiedViolation:
    out: NetworkFirewallPolicyModifiedViolation = {}  # type: ignore[typeddict-item]
    if data.get("ViolationTarget") is not None:
        out["violation_target"] = data["ViolationTarget"]
    if data.get("CurrentPolicyDescription") is not None:
        import capo_fms.types.network_firewall_policy_description

        out["current_policy_description"] = (
            capo_fms.types.network_firewall_policy_description.deserialize_cbor(
                data["CurrentPolicyDescription"]
            )
        )
    if data.get("ExpectedPolicyDescription") is not None:
        import capo_fms.types.network_firewall_policy_description

        out["expected_policy_description"] = (
            capo_fms.types.network_firewall_policy_description.deserialize_cbor(
                data["ExpectedPolicyDescription"]
            )
        )
    return out
