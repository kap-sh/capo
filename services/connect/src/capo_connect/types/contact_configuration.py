"""Generated from Smithy shape ``com.amazonaws.connect#ContactConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.contact_id
    import capo_connect.types.include_raw_message
    import capo_connect.types.participant_role


class ContactConfiguration(TypedDict, closed=True):
    contact_id: "capo_connect.types.contact_id.ContactId"
    """<p>The identifier of the contact within the Amazon Connect instance.</p>"""
    participant_role: NotRequired["capo_connect.types.participant_role.ParticipantRole"]
    """<p>The role of the participant in the chat conversation.</p> <note> <p>Only <code>CUSTOMER</code> is currently supported. Any other values other than <code>CUSTOMER</code> will result in an exception (4xx error).</p> </note>"""
    include_raw_message: "capo_connect.types.include_raw_message.IncludeRawMessage"
    """<p>Whether to include raw connect message in the push notification payload. Default is <code>False</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ContactConfiguration) -> dict:
    out: dict = {}
    out["ContactId"] = value["contact_id"]
    if "participant_role" in value:
        import capo_connect.types.participant_role

        out["ParticipantRole"] = capo_connect.types.participant_role.serialize_json(
            value["participant_role"]
        )
    out["IncludeRawMessage"] = value.get("include_raw_message", False)
    return out


def deserialize_json(data: dict) -> ContactConfiguration:
    out: ContactConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("ContactId") is not None:
        out["contact_id"] = data["ContactId"]
    else:
        out["contact_id"] = ""
    if data.get("ParticipantRole") is not None:
        import capo_connect.types.participant_role

        out["participant_role"] = capo_connect.types.participant_role.deserialize_json(
            data["ParticipantRole"]
        )
    if data.get("IncludeRawMessage") is not None:
        out["include_raw_message"] = data["IncludeRawMessage"]
    else:
        out["include_raw_message"] = False
    return out
