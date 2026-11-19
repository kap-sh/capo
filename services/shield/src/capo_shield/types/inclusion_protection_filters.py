"""Generated from Smithy shape ``com.amazonaws.shield#InclusionProtectionFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protected_resource_type_filters
    import capo_shield.types.protection_name_filters
    import capo_shield.types.resource_arn_filters


class InclusionProtectionFilters(TypedDict, closed=True):
    resource_arns: NotRequired[
        "capo_shield.types.resource_arn_filters.ResourceArnFilters"
    ]
    """<p>The ARN (Amazon Resource Name) of the resource whose protection you want to retrieve. </p>"""
    protection_names: NotRequired[
        "capo_shield.types.protection_name_filters.ProtectionNameFilters"
    ]
    """<p>The name of the protection that you want to retrieve. </p>"""
    resource_types: NotRequired[
        "capo_shield.types.protected_resource_type_filters.ProtectedResourceTypeFilters"
    ]
    """<p>The type of protected resource whose protections you want to retrieve. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InclusionProtectionFilters) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import capo_shield.types.resource_arn_filters

        out["ResourceArns"] = (
            capo_shield.types.resource_arn_filters.serialize_aws_json_1_1(
                value["resource_arns"]
            )
        )
    if "protection_names" in value:
        import capo_shield.types.protection_name_filters

        out["ProtectionNames"] = (
            capo_shield.types.protection_name_filters.serialize_aws_json_1_1(
                value["protection_names"]
            )
        )
    if "resource_types" in value:
        import capo_shield.types.protected_resource_type_filters

        out["ResourceTypes"] = (
            capo_shield.types.protected_resource_type_filters.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InclusionProtectionFilters:
    out: InclusionProtectionFilters = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArns") is not None:
        import capo_shield.types.resource_arn_filters

        out["resource_arns"] = (
            capo_shield.types.resource_arn_filters.deserialize_aws_json_1_1(
                data["ResourceArns"]
            )
        )
    if data.get("ProtectionNames") is not None:
        import capo_shield.types.protection_name_filters

        out["protection_names"] = (
            capo_shield.types.protection_name_filters.deserialize_aws_json_1_1(
                data["ProtectionNames"]
            )
        )
    if data.get("ResourceTypes") is not None:
        import capo_shield.types.protected_resource_type_filters

        out["resource_types"] = (
            capo_shield.types.protected_resource_type_filters.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InclusionProtectionFilters) -> dict:
    out: dict = {}
    if "resource_arns" in value:
        import capo_shield.types.resource_arn_filters

        out["ResourceArns"] = capo_shield.types.resource_arn_filters.serialize_cbor(
            value["resource_arns"]
        )
    if "protection_names" in value:
        import capo_shield.types.protection_name_filters

        out["ProtectionNames"] = (
            capo_shield.types.protection_name_filters.serialize_cbor(
                value["protection_names"]
            )
        )
    if "resource_types" in value:
        import capo_shield.types.protected_resource_type_filters

        out["ResourceTypes"] = (
            capo_shield.types.protected_resource_type_filters.serialize_cbor(
                value["resource_types"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InclusionProtectionFilters:
    out: InclusionProtectionFilters = {}  # type: ignore[typeddict-item]
    if data.get("ResourceArns") is not None:
        import capo_shield.types.resource_arn_filters

        out["resource_arns"] = capo_shield.types.resource_arn_filters.deserialize_cbor(
            data["ResourceArns"]
        )
    if data.get("ProtectionNames") is not None:
        import capo_shield.types.protection_name_filters

        out["protection_names"] = (
            capo_shield.types.protection_name_filters.deserialize_cbor(
                data["ProtectionNames"]
            )
        )
    if data.get("ResourceTypes") is not None:
        import capo_shield.types.protected_resource_type_filters

        out["resource_types"] = (
            capo_shield.types.protected_resource_type_filters.deserialize_cbor(
                data["ResourceTypes"]
            )
        )
    return out
