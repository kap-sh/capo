"""Generated from Smithy shape ``com.amazonaws.codeguruprofiler#PutPermissionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_codeguruprofiler.types.revision_id


class PutPermissionResponse(TypedDict, closed=True):
    policy: "str"
    """<p> The JSON-formatted resource-based policy on the profiling group that includes the added permissions. </p>"""
    revision_id: "capo_codeguruprofiler.types.revision_id.RevisionId"
    """<p> A universally unique identifier (UUID) for the revision of the resource-based policy that includes the added permissions. The JSON-formatted policy is in the <code>policy</code> element of the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutPermissionResponse) -> dict:
    out: dict = {}
    out["policy"] = value["policy"]
    out["revisionId"] = value["revision_id"]
    return out


def deserialize_json(data: dict) -> PutPermissionResponse:
    out: PutPermissionResponse = {}  # type: ignore[typeddict-item]
    if data.get("policy") is not None:
        out["policy"] = data["policy"]
    else:
        out["policy"] = ""
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        out["revision_id"] = ""
    return out
