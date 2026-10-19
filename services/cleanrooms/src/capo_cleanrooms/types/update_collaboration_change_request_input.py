"""Generated from Smithy shape ``com.amazonaws.cleanrooms#UpdateCollaborationChangeRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.change_request_action
    import capo_cleanrooms.types.collaboration_change_request_identifier
    import capo_cleanrooms.types.collaboration_identifier


class UpdateCollaborationChangeRequestInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The unique identifier of the collaboration that contains the change request to be updated.</p>"""
    change_request_identifier: "capo_cleanrooms.types.collaboration_change_request_identifier.CollaborationChangeRequestIdentifier"
    """<p>The unique identifier of the specific change request to be updated within the collaboration.</p>"""
    action: "capo_cleanrooms.types.change_request_action.ChangeRequestAction"
    """<p>The action to perform on the change request. Valid values include APPROVE (approve the change), DENY (reject the change), CANCEL (cancel the request), and COMMIT (commit after the request is approved).</p> <p>For change requests without automatic approval, a member in the collaboration can manually APPROVE or DENY a change request. The collaboration owner can manually CANCEL or COMMIT a change request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateCollaborationChangeRequestInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.change_request_action

    out["action"] = capo_cleanrooms.types.change_request_action.serialize_json(
        value["action"]
    )
    return out


def deserialize_json(data: dict) -> UpdateCollaborationChangeRequestInput:
    out: UpdateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("action") is not None:
        import capo_cleanrooms.types.change_request_action

        out["action"] = capo_cleanrooms.types.change_request_action.deserialize_json(
            data["action"]
        )
    else:
        import typing

        out["action"] = typing.cast(
            "capo_cleanrooms.types.change_request_action.ChangeRequestAction", ""
        )
    return out
