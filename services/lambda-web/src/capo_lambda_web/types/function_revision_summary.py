"""Generated from Smithy shape ``com.amazonaws.lambdaweb#FunctionRevisionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_web.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_web.types.date_time
    import capo_lambda_web.types.description
    import capo_lambda_web.types.revision_arn
    import capo_lambda_web.types.revision_id
    import capo_lambda_web.types.revision_state


class FunctionRevisionSummary(TypedDict, closed=True):
    revision_arn: "capo_lambda_web.types.revision_arn.RevisionArn"
    """<p>The Amazon Resource Name (ARN) of the revision.</p>"""
    revision_id: "capo_lambda_web.types.revision_id.RevisionId"
    """<p>The identifier of the revision.</p>"""
    description: NotRequired["capo_lambda_web.types.description.Description"]
    """<p>A description of the revision.</p>"""
    state: "capo_lambda_web.types.revision_state.RevisionState"
    """<p>The current state of the revision.</p>"""
    state_reason: "str"
    """<p>The reason for the current state of the revision.</p>"""
    created_at: "capo_lambda_web.types.date_time.DateTime"
    """<p>The date and time the revision was created.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionRevisionSummary) -> dict:
    out: dict = {}
    out["revisionArn"] = value["revision_arn"]
    out["revisionId"] = value["revision_id"]
    if "description" in value:
        out["description"] = value["description"]
    import capo_lambda_web.types.revision_state

    out["state"] = capo_lambda_web.types.revision_state.serialize_json(value["state"])
    out["stateReason"] = value["state_reason"]
    import capo_lambda_web.types.date_time

    out["createdAt"] = capo_lambda_web.types.date_time.serialize_json(
        value["created_at"]
    )
    return out


def deserialize_json(data: dict) -> FunctionRevisionSummary:
    out: FunctionRevisionSummary = {}  # type: ignore[typeddict-item]
    if data.get("revisionArn") is not None:
        out["revision_arn"] = data["revisionArn"]
    else:
        raise DeserializationError("FunctionRevisionSummary.revision_arn required")
    if data.get("revisionId") is not None:
        out["revision_id"] = data["revisionId"]
    else:
        raise DeserializationError("FunctionRevisionSummary.revision_id required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("state") is not None:
        import capo_lambda_web.types.revision_state

        out["state"] = capo_lambda_web.types.revision_state.deserialize_json(
            data["state"]
        )
    else:
        raise DeserializationError("FunctionRevisionSummary.state required")
    if data.get("stateReason") is not None:
        out["state_reason"] = data["stateReason"]
    else:
        raise DeserializationError("FunctionRevisionSummary.state_reason required")
    if data.get("createdAt") is not None:
        import capo_lambda_web.types.date_time

        out["created_at"] = capo_lambda_web.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        raise DeserializationError("FunctionRevisionSummary.created_at required")
    return out
