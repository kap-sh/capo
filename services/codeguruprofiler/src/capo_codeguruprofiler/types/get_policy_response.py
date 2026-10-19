"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#GetPolicyResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.revision_id


class GetPolicyResponse(TypedDict, closed=True):
    policy: "str"
    """<p>The JSON-formatted resource-based policy attached to the <code>ProfilingGroup</code>.</p>"""
    revision_id: "capo_codeguruprofiler.types.revision_id.RevisionId"
    """<p>A unique identifier for the current revision of the returned policy.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPolicyResponse) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> GetPolicyResponse:
    out: GetPolicyResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out
