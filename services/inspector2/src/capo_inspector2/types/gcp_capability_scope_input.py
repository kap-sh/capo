"""Generated from Smithy shape ``com.amazonaws.inspector2#GcpCapabilityScopeInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_inspector2.types.gcp_scope_value_list
    import capo_inspector2.types.scope_type


class GcpCapabilityScopeInput(TypedDict, closed=True):
    scope_type: "capo_inspector2.types.scope_type.ScopeType"
    """<p>The type of scope: <code>ORGANIZATION</code>, which scans all projects in the GCP organization, or <code>PROJECT</code>, which scans only the specified GCP projects.</p>"""
    scope_values: NotRequired[
        "capo_inspector2.types.gcp_scope_value_list.GcpScopeValueList"
    ]
    """<p>The GCP project IDs to scan. Required when <code>scopeType</code> is <code>PROJECT</code>. Don't specify scope values when <code>scopeType</code> is <code>ORGANIZATION</code>. Amazon Inspector scans the organization of the Amazon Web Services Config connector.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpCapabilityScopeInput) -> dict:
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
    return out


def deserialize_json(data: dict) -> GcpCapabilityScopeInput:
    out: GcpCapabilityScopeInput = {}  # type: ignore[typeddict-item]
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
    return out
