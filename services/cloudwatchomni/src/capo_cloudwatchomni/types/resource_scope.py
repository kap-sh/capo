"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ResourceScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatchomni.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.resource_arn_list
    import capo_cloudwatchomni.types.resource_scope_tag_map
    import capo_cloudwatchomni.types.row_scope_group_list
    import capo_cloudwatchomni.types.signal_type_list


class ResourceScope(TypedDict, closed=True):
    resource_type: "str"
    """Resource type name (e.g., "DataSet", "OmniDashboard")."""
    resource_arns: NotRequired[
        "capo_cloudwatchomni.types.resource_arn_list.ResourceArnList"
    ]
    """Specific resource ARNs or ARN patterns. When set, actions are limited to these resources. When absent, defaults to "*"."""
    tags: NotRequired[
        "capo_cloudwatchomni.types.resource_scope_tag_map.ResourceScopeTagMap"
    ]
    """Tag-based conditions for dynamic resource scoping. Access applies only to resources carrying all of the specified tag key/value pairs."""
    signal_types: NotRequired[
        "capo_cloudwatchomni.types.signal_type_list.SignalTypeList"
    ]
    """Signal types this scope's row filtering applies to. Required when rowScopeGroups is set."""
    row_scope_groups: NotRequired[
        "capo_cloudwatchomni.types.row_scope_group_list.RowScopeGroupList"
    ]
    """Row-level filters for this scope, as an OR of AND-groups: a row is visible when it matches every filter in any one group. Requires signalTypes. Row filters are additive across a principal's matching grants. A signal type with no matching group is unrestricted, and when rowScopeGroups is omitted all rows are visible for all signal types."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ResourceScope) -> dict:
    out: dict = {}
    out["resourceType"] = value["resource_type"]
    if "resource_arns" in value:
        import capo_cloudwatchomni.types.resource_arn_list

        out["resourceArns"] = (
            capo_cloudwatchomni.types.resource_arn_list.serialize_cbor(
                value["resource_arns"]
            )
        )
    if "tags" in value:
        import capo_cloudwatchomni.types.resource_scope_tag_map

        out["tags"] = capo_cloudwatchomni.types.resource_scope_tag_map.serialize_cbor(
            value["tags"]
        )
    if "signal_types" in value:
        import capo_cloudwatchomni.types.signal_type_list

        out["signalTypes"] = capo_cloudwatchomni.types.signal_type_list.serialize_cbor(
            value["signal_types"]
        )
    if "row_scope_groups" in value:
        import capo_cloudwatchomni.types.row_scope_group_list

        out["rowScopeGroups"] = (
            capo_cloudwatchomni.types.row_scope_group_list.serialize_cbor(
                value["row_scope_groups"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ResourceScope:
    out: ResourceScope = {}  # type: ignore[typeddict-item]
    if data.get("resourceType") is not None:
        out["resource_type"] = data["resourceType"]
    else:
        raise DeserializationError("ResourceScope.resource_type required")
    if data.get("resourceArns") is not None:
        import capo_cloudwatchomni.types.resource_arn_list

        out["resource_arns"] = (
            capo_cloudwatchomni.types.resource_arn_list.deserialize_cbor(
                data["resourceArns"]
            )
        )
    if data.get("tags") is not None:
        import capo_cloudwatchomni.types.resource_scope_tag_map

        out["tags"] = capo_cloudwatchomni.types.resource_scope_tag_map.deserialize_cbor(
            data["tags"]
        )
    if data.get("signalTypes") is not None:
        import capo_cloudwatchomni.types.signal_type_list

        out["signal_types"] = (
            capo_cloudwatchomni.types.signal_type_list.deserialize_cbor(
                data["signalTypes"]
            )
        )
    if data.get("rowScopeGroups") is not None:
        import capo_cloudwatchomni.types.row_scope_group_list

        out["row_scope_groups"] = (
            capo_cloudwatchomni.types.row_scope_group_list.deserialize_cbor(
                data["rowScopeGroups"]
            )
        )
    return out
