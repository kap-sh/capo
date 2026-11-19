"""Generated from Smithy shape ``com.amazonaws.shield#InclusionProtectionGroupFilters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.protected_resource_type_filters
    import capo_shield.types.protection_group_aggregation_filters
    import capo_shield.types.protection_group_id_filters
    import capo_shield.types.protection_group_pattern_filters


class InclusionProtectionGroupFilters(TypedDict, closed=True):
    protection_group_ids: NotRequired[
        "capo_shield.types.protection_group_id_filters.ProtectionGroupIdFilters"
    ]
    """<p>The ID of the protection group that you want to retrieve. </p>"""
    patterns: NotRequired[
        "capo_shield.types.protection_group_pattern_filters.ProtectionGroupPatternFilters"
    ]
    """<p>The pattern specification of the protection groups that you want to retrieve. </p>"""
    resource_types: NotRequired[
        "capo_shield.types.protected_resource_type_filters.ProtectedResourceTypeFilters"
    ]
    """<p>The resource type configuration of the protection groups that you want to retrieve. In the protection group configuration, you specify the resource type when you set the group's <code>Pattern</code> to <code>BY_RESOURCE_TYPE</code>. </p>"""
    aggregations: NotRequired[
        "capo_shield.types.protection_group_aggregation_filters.ProtectionGroupAggregationFilters"
    ]
    """<p>The aggregation setting of the protection groups that you want to retrieve. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: InclusionProtectionGroupFilters) -> dict:
    out: dict = {}
    if "protection_group_ids" in value:
        import capo_shield.types.protection_group_id_filters

        out["ProtectionGroupIds"] = (
            capo_shield.types.protection_group_id_filters.serialize_aws_json_1_1(
                value["protection_group_ids"]
            )
        )
    if "patterns" in value:
        import capo_shield.types.protection_group_pattern_filters

        out["Patterns"] = (
            capo_shield.types.protection_group_pattern_filters.serialize_aws_json_1_1(
                value["patterns"]
            )
        )
    if "resource_types" in value:
        import capo_shield.types.protected_resource_type_filters

        out["ResourceTypes"] = (
            capo_shield.types.protected_resource_type_filters.serialize_aws_json_1_1(
                value["resource_types"]
            )
        )
    if "aggregations" in value:
        import capo_shield.types.protection_group_aggregation_filters

        out["Aggregations"] = (
            capo_shield.types.protection_group_aggregation_filters.serialize_aws_json_1_1(
                value["aggregations"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> InclusionProtectionGroupFilters:
    out: InclusionProtectionGroupFilters = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroupIds") is not None:
        import capo_shield.types.protection_group_id_filters

        out["protection_group_ids"] = (
            capo_shield.types.protection_group_id_filters.deserialize_aws_json_1_1(
                data["ProtectionGroupIds"]
            )
        )
    if data.get("Patterns") is not None:
        import capo_shield.types.protection_group_pattern_filters

        out["patterns"] = (
            capo_shield.types.protection_group_pattern_filters.deserialize_aws_json_1_1(
                data["Patterns"]
            )
        )
    if data.get("ResourceTypes") is not None:
        import capo_shield.types.protected_resource_type_filters

        out["resource_types"] = (
            capo_shield.types.protected_resource_type_filters.deserialize_aws_json_1_1(
                data["ResourceTypes"]
            )
        )
    if data.get("Aggregations") is not None:
        import capo_shield.types.protection_group_aggregation_filters

        out["aggregations"] = (
            capo_shield.types.protection_group_aggregation_filters.deserialize_aws_json_1_1(
                data["Aggregations"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: InclusionProtectionGroupFilters) -> dict:
    out: dict = {}
    if "protection_group_ids" in value:
        import capo_shield.types.protection_group_id_filters

        out["ProtectionGroupIds"] = (
            capo_shield.types.protection_group_id_filters.serialize_cbor(
                value["protection_group_ids"]
            )
        )
    if "patterns" in value:
        import capo_shield.types.protection_group_pattern_filters

        out["Patterns"] = (
            capo_shield.types.protection_group_pattern_filters.serialize_cbor(
                value["patterns"]
            )
        )
    if "resource_types" in value:
        import capo_shield.types.protected_resource_type_filters

        out["ResourceTypes"] = (
            capo_shield.types.protected_resource_type_filters.serialize_cbor(
                value["resource_types"]
            )
        )
    if "aggregations" in value:
        import capo_shield.types.protection_group_aggregation_filters

        out["Aggregations"] = (
            capo_shield.types.protection_group_aggregation_filters.serialize_cbor(
                value["aggregations"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> InclusionProtectionGroupFilters:
    out: InclusionProtectionGroupFilters = {}  # type: ignore[typeddict-item]
    if data.get("ProtectionGroupIds") is not None:
        import capo_shield.types.protection_group_id_filters

        out["protection_group_ids"] = (
            capo_shield.types.protection_group_id_filters.deserialize_cbor(
                data["ProtectionGroupIds"]
            )
        )
    if data.get("Patterns") is not None:
        import capo_shield.types.protection_group_pattern_filters

        out["patterns"] = (
            capo_shield.types.protection_group_pattern_filters.deserialize_cbor(
                data["Patterns"]
            )
        )
    if data.get("ResourceTypes") is not None:
        import capo_shield.types.protected_resource_type_filters

        out["resource_types"] = (
            capo_shield.types.protected_resource_type_filters.deserialize_cbor(
                data["ResourceTypes"]
            )
        )
    if data.get("Aggregations") is not None:
        import capo_shield.types.protection_group_aggregation_filters

        out["aggregations"] = (
            capo_shield.types.protection_group_aggregation_filters.deserialize_cbor(
                data["Aggregations"]
            )
        )
    return out
