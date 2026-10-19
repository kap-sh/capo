"""Generated from Smithy shape ``com.amazonaws.deadline#BatchGetSessionActionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_deadline.types.batch_get_session_action_identifiers


class BatchGetSessionActionRequest(TypedDict, closed=True):
    identifiers: "capo_deadline.types.batch_get_session_action_identifiers.BatchGetSessionActionIdentifiers"
    """<p>The list of session action identifiers to retrieve. You can specify up to 100 identifiers per request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSessionActionRequest) -> dict:
    out: dict = {}
    import capo_deadline.types.batch_get_session_action_identifiers

    out["identifiers"] = (
        capo_deadline.types.batch_get_session_action_identifiers.serialize_json(
            value["identifiers"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetSessionActionRequest:
    out: BatchGetSessionActionRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifiers") is not None:
        import capo_deadline.types.batch_get_session_action_identifiers

        out["identifiers"] = (
            capo_deadline.types.batch_get_session_action_identifiers.deserialize_json(
                data["identifiers"]
            )
        )
    else:
        out["identifiers"] = []
    return out
