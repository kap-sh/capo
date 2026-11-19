"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpCapabilityScope``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_scope_value_list
    import capo_inspector2.types.scope_state
    import capo_inspector2.types.scope_type


class GcpCapabilityScope(TypedDict, closed=True):
    scope_type: "capo_inspector2.types.scope_type.ScopeType"
    """<p>The type of scope: <code>ORGANIZATION</code>, which scans all projects in the GCP organization, or <code>PROJECT</code>, which scans only the specified GCP projects.</p>"""
    scope_values: NotRequired[
        "capo_inspector2.types.gcp_scope_value_list.GcpScopeValueList"
    ]
    """<p>The GCP project IDs to scan when <code>scopeType</code> is <code>PROJECT</code>. Not used when <code>scopeType</code> is <code>ORGANIZATION</code>. Amazon Inspector scans the organization of the Amazon Web Services Config connector.</p>"""
    state: NotRequired["capo_inspector2.types.scope_state.ScopeState"]
    """<p>The current state of the scope configuration.</p>"""
    state_reason: NotRequired["str"]
    """<p>The reason for the current state of the scope configuration.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpCapabilityScope) -> dict:
    out: dict = {}
    import capo_inspector2.types.scope_type

    out["scopeType"] = capo_inspector2.types.scope_type.serialize_json(
        value["scope_type"]
    )
    if "scope_values" in value:
        import capo_inspector2.types.gcp_scope_value_list

        out["scopeValues"] = capo_inspector2.types.gcp_scope_value_list.serialize_json(
            value["scope_values"]
        )
    if "state" in value:
        import capo_inspector2.types.scope_state

        out["state"] = capo_inspector2.types.scope_state.serialize_json(value["state"])
    if "state_reason" in value:
        out["stateReason"] = value["state_reason"]
    return out


def deserialize_json(data: dict) -> GcpCapabilityScope:
    out: GcpCapabilityScope = {}  # type: ignore[typeddict-item]
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
        import capo_inspector2.types.gcp_scope_value_list

        out["scope_values"] = (
            capo_inspector2.types.gcp_scope_value_list.deserialize_json(
                data["scopeValues"]
            )
        )
    if data.get("state") is not None:
        import capo_inspector2.types.scope_state

        out["state"] = capo_inspector2.types.scope_state.deserialize_json(data["state"])
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    return out
