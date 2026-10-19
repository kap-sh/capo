"""Generated from Smithy shape ``com.amazonaws.inspector2#ScopeConfigurationInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.scope_type
    import capo_inspector2.types.scope_value_list


class ScopeConfigurationInput(TypedDict, closed=True):
    scope_type: "capo_inspector2.types.scope_type.ScopeType"
    """<p>The type of scope. Valid values are <code>TENANT</code>, which scans all resources in the Azure tenant, and <code>SUBSCRIPTION</code>, which scans only the resources in the specified Azure subscriptions.</p>"""
    scope_values: NotRequired["capo_inspector2.types.scope_value_list.ScopeValueList"]
    """<p>The list of scope values. For subscription-level scope, these are Azure subscription IDs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ScopeConfigurationInput) -> dict:
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
    return out


def deserialize_json(data: dict) -> ScopeConfigurationInput:
    out: ScopeConfigurationInput = {}  # type: ignore[typeddict-item]
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
    return out
