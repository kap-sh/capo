"""Generated from Smithy shape ``com.amazonaws.fms#PolicyTypeScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_fms.types.boolean
    import capo_fms.types.security_service_type_list


class PolicyTypeScope(TypedDict, closed=True):
    policy_types: NotRequired[
        "capo_fms.types.security_service_type_list.SecurityServiceTypeList"
    ]
    """<p>The list of policy types that the specified Firewall Manager administrator can manage.</p>"""
    all_policy_types_enabled: "capo_fms.types.boolean.Boolean"
    """<p>Allows the specified Firewall Manager administrator to manage all Firewall Manager policy types, except for third-party policy types. Third-party policy types can only be managed by the Firewall Manager default administrator.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PolicyTypeScope) -> dict:
    out: dict = {}
    if "policy_types" in value:
        import capo_fms.types.security_service_type_list

        out["PolicyTypes"] = (
            capo_fms.types.security_service_type_list.serialize_aws_json_1_1(
                value["policy_types"]
            )
        )
    out["AllPolicyTypesEnabled"] = value.get("all_policy_types_enabled", False)
    return out


def deserialize_aws_json_1_1(data: dict) -> PolicyTypeScope:
    out: PolicyTypeScope = {}  # type: ignore[typeddict-item]
    if data.get("PolicyTypes") is not None:
        import capo_fms.types.security_service_type_list

        out["policy_types"] = (
            capo_fms.types.security_service_type_list.deserialize_aws_json_1_1(
                data["PolicyTypes"]
            )
        )
    if data.get("AllPolicyTypesEnabled") is not None:
        out["all_policy_types_enabled"] = data["AllPolicyTypesEnabled"]
    else:
        out["all_policy_types_enabled"] = False
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: PolicyTypeScope) -> dict:
    out: dict = {}
    if "policy_types" in value:
        import capo_fms.types.security_service_type_list

        out["PolicyTypes"] = capo_fms.types.security_service_type_list.serialize_cbor(
            value["policy_types"]
        )
    out["AllPolicyTypesEnabled"] = value.get("all_policy_types_enabled", False)
    return out


def deserialize_cbor(data: dict) -> PolicyTypeScope:
    out: PolicyTypeScope = {}  # type: ignore[typeddict-item]
    if data.get("PolicyTypes") is not None:
        import capo_fms.types.security_service_type_list

        out["policy_types"] = (
            capo_fms.types.security_service_type_list.deserialize_cbor(
                data["PolicyTypes"]
            )
        )
    if data.get("AllPolicyTypesEnabled") is not None:
        out["all_policy_types_enabled"] = data["AllPolicyTypesEnabled"]
    else:
        out["all_policy_types_enabled"] = False
    return out
