"""Generated from Smithy shape ``com.amazonaws.cloudwatchomni#ScopedActions``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatchomni.types.context_conditions_map
    import capo_cloudwatchomni.types.resource_scope_list
    import capo_cloudwatchomni.types.scoped_action_name_list


class ScopedActions(TypedDict, closed=True):
    actions: "capo_cloudwatchomni.types.scoped_action_name_list.ScopedActionNameList"
    """The actions this group applies to."""
    resources: NotRequired[
        "capo_cloudwatchomni.types.resource_scope_list.ResourceScopeList"
    ]
    """Optional resource scopes constraining these actions to specific resources."""
    context_conditions: NotRequired[
        "capo_cloudwatchomni.types.context_conditions_map.ContextConditionsMap"
    ]
    """Optional context conditions for fine-grained access control on these actions."""


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: ScopedActions) -> dict:
    out: dict = {}
    import capo_cloudwatchomni.types.scoped_action_name_list

    out["actions"] = capo_cloudwatchomni.types.scoped_action_name_list.serialize_cbor(
        value["actions"]
    )
    if "resources" in value:
        import capo_cloudwatchomni.types.resource_scope_list

        out["resources"] = capo_cloudwatchomni.types.resource_scope_list.serialize_cbor(
            value["resources"]
        )
    if "context_conditions" in value:
        import capo_cloudwatchomni.types.context_conditions_map

        out["contextConditions"] = (
            capo_cloudwatchomni.types.context_conditions_map.serialize_cbor(
                value["context_conditions"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> ScopedActions:
    out: ScopedActions = {}  # type: ignore[typeddict-item]
    if data.get("actions") is not None:
        import capo_cloudwatchomni.types.scoped_action_name_list

        out["actions"] = (
            capo_cloudwatchomni.types.scoped_action_name_list.deserialize_cbor(
                data["actions"]
            )
        )
    else:
        out["actions"] = []
    if data.get("resources") is not None:
        import capo_cloudwatchomni.types.resource_scope_list

        out["resources"] = (
            capo_cloudwatchomni.types.resource_scope_list.deserialize_cbor(
                data["resources"]
            )
        )
    if data.get("contextConditions") is not None:
        import capo_cloudwatchomni.types.context_conditions_map

        out["context_conditions"] = (
            capo_cloudwatchomni.types.context_conditions_map.deserialize_cbor(
                data["contextConditions"]
            )
        )
    return out
