"""Generated from Smithy shape ``com.amazonaws.fms#ViolationReason``."""

from typing import Literal, TypeAlias, cast

ViolationReason: TypeAlias = Literal[
    "WEB_ACL_MISSING_RULE_GROUP",
    "RESOURCE_MISSING_WEB_ACL",
    "RESOURCE_INCORRECT_WEB_ACL",
    "RESOURCE_MISSING_SHIELD_PROTECTION",
    "RESOURCE_MISSING_WEB_ACL_OR_SHIELD_PROTECTION",
    "RESOURCE_MISSING_SECURITY_GROUP",
    "RESOURCE_VIOLATES_AUDIT_SECURITY_GROUP",
    "SECURITY_GROUP_UNUSED",
    "SECURITY_GROUP_REDUNDANT",
    "FMS_CREATED_SECURITY_GROUP_EDITED",
    "MISSING_FIREWALL",
    "MISSING_FIREWALL_SUBNET_IN_AZ",
    "MISSING_EXPECTED_ROUTE_TABLE",
    "NETWORK_FIREWALL_POLICY_MODIFIED",
    "FIREWALL_SUBNET_IS_OUT_OF_SCOPE",
    "INTERNET_GATEWAY_MISSING_EXPECTED_ROUTE",
    "FIREWALL_SUBNET_MISSING_EXPECTED_ROUTE",
    "UNEXPECTED_FIREWALL_ROUTES",
    "UNEXPECTED_TARGET_GATEWAY_ROUTES",
    "TRAFFIC_INSPECTION_CROSSES_AZ_BOUNDARY",
    "INVALID_ROUTE_CONFIGURATION",
    "MISSING_TARGET_GATEWAY",
    "INTERNET_TRAFFIC_NOT_INSPECTED",
    "BLACK_HOLE_ROUTE_DETECTED",
    "BLACK_HOLE_ROUTE_DETECTED_IN_FIREWALL_SUBNET",
    "RESOURCE_MISSING_DNS_FIREWALL",
    "ROUTE_HAS_OUT_OF_SCOPE_ENDPOINT",
    "FIREWALL_SUBNET_MISSING_VPCE_ENDPOINT",
    "INVALID_NETWORK_ACL_ENTRY",
    "WEB_ACL_CONFIGURATION_OR_SCOPE_OF_USE",
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ViolationReason) -> str:
    return value


def deserialize_aws_json_1_1(data: str) -> ViolationReason:
    return cast(ViolationReason, data)


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ViolationReason) -> str:
    return value


def deserialize_cbor(data: str) -> ViolationReason:
    return cast(ViolationReason, data)
