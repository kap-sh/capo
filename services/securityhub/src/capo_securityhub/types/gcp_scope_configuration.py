"""Generated from Smithy shape ``com.amazonaws.securityhub#GcpScopeConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_securityhub.types.gcp_scope_type
    import capo_securityhub.types.scope_value_list


class GcpScopeConfiguration(TypedDict, closed=True):
    scope_type: NotRequired["capo_securityhub.types.gcp_scope_type.GcpScopeType"]
    """<p>The type of scope. Valid values are <code>ORGANIZATION</code> and <code>PROJECT</code>.</p>"""
    scope_values: NotRequired["capo_securityhub.types.scope_value_list.ScopeValueList"]
    """<p>The list of scope values. Use an organization ID when the scope type is <code>ORGANIZATION</code>, or project IDs when the scope type is <code>PROJECT</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GcpScopeConfiguration) -> dict:
    out: dict = {}
    if "scope_type" in value:
        import capo_securityhub.types.gcp_scope_type

        out["ScopeType"] = capo_securityhub.types.gcp_scope_type.serialize_json(
            value["scope_type"]
        )
    if "scope_values" in value:
        import capo_securityhub.types.scope_value_list

        out["ScopeValues"] = capo_securityhub.types.scope_value_list.serialize_json(
            value["scope_values"]
        )
    return out


def deserialize_json(data: dict) -> GcpScopeConfiguration:
    out: GcpScopeConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ScopeType") is not None:
        import capo_securityhub.types.gcp_scope_type

        out["scope_type"] = capo_securityhub.types.gcp_scope_type.deserialize_json(
            data["ScopeType"]
        )
    if data.get("ScopeValues") is not None:
        import capo_securityhub.types.scope_value_list

        out["scope_values"] = capo_securityhub.types.scope_value_list.deserialize_json(
            data["ScopeValues"]
        )
    return out
