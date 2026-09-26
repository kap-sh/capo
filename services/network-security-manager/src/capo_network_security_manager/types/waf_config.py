"""Generated from Smithy shape ``com.amazonaws.networksecuritymanager#WafConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_network_security_manager.errors import DeserializationError

if TYPE_CHECKING:
    import capo_network_security_manager.types.existing_customer_web_acl_resolution
    import capo_network_security_manager.types.waf_conflict_resolution_options


class WafConfig(TypedDict, closed=True):
    existing_customer_web_acl_resolution: "capo_network_security_manager.types.existing_customer_web_acl_resolution.ExistingCustomerWebACLResolution"
    """<p>Determines how AWS Network Security Manager handles remediation when a resource already has a customer-created web ACL. Required for AWS WAF policies.</p>"""
    conflict_resolution: "capo_network_security_manager.types.waf_conflict_resolution_options.WAFConflictResolutionOptions"
    """<p>The conflict-resolution strategy for AWS WAF policies. Required for AWS WAF policies.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: WafConfig) -> dict:
    out: dict = {}
    import capo_network_security_manager.types.existing_customer_web_acl_resolution

    out["existingCustomerWebACLResolution"] = (
        capo_network_security_manager.types.existing_customer_web_acl_resolution.serialize_json(
            value["existing_customer_web_acl_resolution"]
        )
    )
    import capo_network_security_manager.types.waf_conflict_resolution_options

    out["conflictResolution"] = (
        capo_network_security_manager.types.waf_conflict_resolution_options.serialize_json(
            value["conflict_resolution"]
        )
    )
    return out


def deserialize_json(data: dict) -> WafConfig:
    out: WafConfig = {}  # type: ignore[typeddict-item]
    if data.get("existingCustomerWebACLResolution") is not None:
        import capo_network_security_manager.types.existing_customer_web_acl_resolution

        out["existing_customer_web_acl_resolution"] = (
            capo_network_security_manager.types.existing_customer_web_acl_resolution.deserialize_json(
                data["existingCustomerWebACLResolution"]
            )
        )
    else:
        raise DeserializationError(
            "WafConfig.existing_customer_web_acl_resolution required"
        )
    if data.get("conflictResolution") is not None:
        import capo_network_security_manager.types.waf_conflict_resolution_options

        out["conflict_resolution"] = (
            capo_network_security_manager.types.waf_conflict_resolution_options.deserialize_json(
                data["conflictResolution"]
            )
        )
    else:
        raise DeserializationError("WafConfig.conflict_resolution required")
    return out
