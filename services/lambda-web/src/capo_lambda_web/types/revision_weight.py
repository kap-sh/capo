"""Generated from Smithy shape ``com.amazonaws.lambdaweb#RevisionWeight``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.revision_id


class RevisionWeight(TypedDict, closed=True):
    revision_id: "capo_lambda_web.types.revision_id.RevisionId"
    """<p>The identifier of the revision.</p>"""
    weight: "int"
    """<p>The percentage of traffic to route to this revision. Minimum value of 1, maximum value of 100.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: RevisionWeight) -> dict:
    out: dict = {}
    out["revisionId"] = value["revision_id"]
    out["weight"] = value["weight"]
    return out


def deserialize_json(data: dict) -> RevisionWeight:
    out: RevisionWeight = {}  # type: ignore[typeddict-item]
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("RevisionWeight.revision_id required")
    if data.get("weight") is not None:
        out["weight"] = data["weight"]
    else:
        raise DeserializationError("RevisionWeight.weight required")
    return out
