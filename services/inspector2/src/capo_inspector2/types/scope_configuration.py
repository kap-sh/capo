"""Generated from Smithy shape ``com.amazonaws.inspector2#ScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.scope_state
    import capo_inspector2.types.scope_type
    import capo_inspector2.types.scope_value_list


class ScopeConfiguration(TypedDict, closed=True):
    scope_type: "capo_inspector2.types.scope_type.ScopeType"
    """<p>The type of scope. Valid values are <code>TENANT</code>, which scans all resources in the Azure tenant, and <code>SUBSCRIPTION</code>, which scans only the resources in the specified Azure subscriptions.</p>"""
    scope_values: NotRequired["capo_inspector2.types.scope_value_list.ScopeValueList"]
    """<p>The list of scope values. For subscription-level scope, these are Azure subscription IDs.</p>"""
    state: NotRequired["capo_inspector2.types.scope_state.ScopeState"]
    """<p>The current state of the scope configuration.</p>"""
    state_reason: NotRequired["str"]
    """<p>The reason for the current state of the scope configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeConfiguration) -> dict:
    out: dict = {}
    import capo_inspector2.types.scope_type

    out["scopeType"] = capo_inspector2.types.scope_type.serialize_json(
        value["scope_type"]
    )
    if "scope_values" in value:
        import capo_inspector2.types.scope_value_list

        out["scopeValues"] = capo_inspector2.types.scope_value_list.serialize_json(
            value["scope_values"]
        )
    if "state" in value:
        import capo_inspector2.types.scope_state

        out["state"] = capo_inspector2.types.scope_state.serialize_json(value["state"])
    if "state_reason" in value:
        out["stateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> ScopeConfiguration:
    out: ScopeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("scopeType") is not None:
        import capo_inspector2.types.scope_type

        out["scope_type"] = capo_inspector2.types.scope_type.deserialize_json(
            data["scopeType"]
        )
    else:
        import typing

        out["scope_type"] = typing.cast(
            "capo_inspector2.types.scope_type.ScopeType", ""
        )
    if data.get("scopeValues") is not None:
        import capo_inspector2.types.scope_value_list

        out["scope_values"] = capo_inspector2.types.scope_value_list.deserialize_json(
            data["scopeValues"]
        )
    if data.get("state") is not None:
        import capo_inspector2.types.scope_state

        out["state"] = capo_inspector2.types.scope_state.deserialize_json(data["state"])
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    return out
