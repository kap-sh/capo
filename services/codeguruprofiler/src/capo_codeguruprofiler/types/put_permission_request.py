"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#PutPermissionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.action_group
    import capo_codeguruprofiler.types.principals
    import capo_codeguruprofiler.types.profiling_group_name
    import capo_codeguruprofiler.types.revision_id


class PutPermissionRequest(TypedDict, closed=True):
    profiling_group_name: (
        "capo_codeguruprofiler.types.profiling_group_name.ProfilingGroupName"
    )
    """<p>The name of the profiling group to grant access to.</p>"""
    action_group: "capo_codeguruprofiler.types.action_group.ActionGroup"
    """<p> Specifies an action group that contains permissions to add to a profiling group resource. One action group is supported, <code>agentPermissions</code>, which grants permission to perform actions required by the profiling agent, <code>ConfigureAgent</code> and <code>PostAgentProfile</code> permissions. </p>"""
    principals: "capo_codeguruprofiler.types.principals.Principals"
    """<p> A list ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not are supported in the ARNs. </p>"""
    revision_id: NotRequired["capo_codeguruprofiler.types.revision_id.RevisionId"]
    """<p> A universally unique identifier (UUID) for the revision of the policy you are adding to the profiling group. Do not specify this when you add permissions to a profiling group for the first time. If a policy already exists on the profiling group, you must specify the <code>revisionId</code>. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPermissionRequest) -> dict:
    out: dict = {}
    import capo_codeguruprofiler.types.principals

    out["principals"] = capo_codeguruprofiler.types.principals.serialize_json(
        value["principals"]
    )
    if "revision_id" in value:
        out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutPermissionRequest:
    out: PutPermissionRequest = {}  # type: ignore[typeddict-item]
    if data.get("principals") is not None:
        import capo_codeguruprofiler.types.principals

        out["principals"] = capo_codeguruprofiler.types.principals.deserialize_json(
            data["principals"]
        )
    else:
        out["principals"] = []
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    return out
