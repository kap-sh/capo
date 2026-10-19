"""Generated from Smithy shape ``com.amazonaws.cleanrooms#CreateCollaborationChangeRequestInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.change_input_list
    import capo_cleanrooms.types.collaboration_identifier


class CreateCollaborationChangeRequestInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>The identifier of the collaboration that the change request is made against.</p>"""
    changes: "capo_cleanrooms.types.change_input_list.ChangeInputList"
    """<p>The list of changes to apply to the collaboration. Each change specifies the type of modification and the details of what should be changed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateCollaborationChangeRequestInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.change_input_list

    out["changes"] = capo_cleanrooms.types.change_input_list.serialize_json(
        value["changes"]
    )
    return out


def deserialize_json(data: dict) -> CreateCollaborationChangeRequestInput:
    out: CreateCollaborationChangeRequestInput = {}  # type: ignore[typeddict-item]
    if data.get("changes") is not None:
        import capo_cleanrooms.types.change_input_list

        out["changes"] = capo_cleanrooms.types.change_input_list.deserialize_json(
            data["changes"]
        )
    else:
        out["changes"] = []
    return out
