"""Generated from Smithy shape ``com.amazonaws.networkflowmonitor#UpdateScopeOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_networkflowmonitor.types.arn
    import capo_networkflowmonitor.types.scope_id
    import capo_networkflowmonitor.types.scope_status
    import capo_networkflowmonitor.types.tag_map


class UpdateScopeOutput(TypedDict, closed=True):
    scope_id: "capo_networkflowmonitor.types.scope_id.ScopeId"
    """<p>The identifier for the scope that includes the resources you want to get data results for. A scope ID is an internally-generated identifier that includes all the resources for a specific root account.</p>"""
    status: "capo_networkflowmonitor.types.scope_status.ScopeStatus"
    """<p>The status for a scope. The status can be one of the following: <code>SUCCEEDED</code>, <code>IN_PROGRESS</code>, <code>FAILED</code>, <code>DEACTIVATING</code>, or <code>DEACTIVATED</code>.</p> <p>A status of <code>DEACTIVATING</code> means that you've requested a scope to be deactivated and Network Flow Monitor is in the process of deactivating the scope. A status of <code>DEACTIVATED</code> means that the deactivating process is complete.</p>"""
    scope_arn: "capo_networkflowmonitor.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the scope.</p>"""
    tags: NotRequired["capo_networkflowmonitor.types.tag_map.TagMap"]
    """<p>The tags for a scope.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateScopeOutput) -> dict:
    out: dict = {}
    out["scopeId"] = value["scope_id"]
    import capo_networkflowmonitor.types.scope_status

    out["status"] = capo_networkflowmonitor.types.scope_status.serialize_json(
        value["status"]
    )
    out["scopeArn"] = value["scope_arn"]
    if "tags" in value:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateScopeOutput:
    out: UpdateScopeOutput = {}  # type: ignore[typeddict-item]
    if data.get("scopeId") is not None:
        out["scope_id"] = data["scopeId"]
    else:
        out["scope_id"] = ""
    if data.get("status") is not None:
        import capo_networkflowmonitor.types.scope_status

        out["status"] = capo_networkflowmonitor.types.scope_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_networkflowmonitor.types.scope_status.ScopeStatus", ""
        )
    if data.get("scopeArn") is not None:
        out["scope_arn"] = data["scopeArn"]
    else:
        out["scope_arn"] = ""
    if data.get("tags") is not None:
        import capo_networkflowmonitor.types.tag_map

        out["tags"] = capo_networkflowmonitor.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
