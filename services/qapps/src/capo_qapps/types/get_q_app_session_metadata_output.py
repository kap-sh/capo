"""Generated from Smithy shape ``com.amazonaws.qapps#GetQAppSessionMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.session_name
    import capo_qapps.types.session_sharing_configuration
    import capo_qapps.types.uuid


class GetQAppSessionMetadataOutput(TypedDict, closed=True):
    session_id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the Q App session.</p>"""
    session_arn: "str"
    """<p>The Amazon Resource Name (ARN) of the Q App session.</p>"""
    session_name: NotRequired["capo_qapps.types.session_name.SessionName"]
    """<p>The name of the Q App session.</p>"""
    sharing_configuration: (
        "capo_qapps.types.session_sharing_configuration.SessionSharingConfiguration"
    )
    """<p>The sharing configuration of the Q App data collection session.</p>"""
    session_owner: NotRequired["bool"]
    """<p>Indicates whether the current user is the owner of the Q App session.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetQAppSessionMetadataOutput) -> dict:
    out: dict = {}
    out["sessionId"] = value["session_id"]
    out["sessionArn"] = value["session_arn"]
    if "session_name" in value:
        out["sessionName"] = value["session_name"]
    import capo_qapps.types.session_sharing_configuration

    out["sharingConfiguration"] = (
        capo_qapps.types.session_sharing_configuration.serialize_json(
            value["sharing_configuration"]
        )
    )
    if "session_owner" in value:
        out["sessionOwner"] = value["session_owner"]
    return out


def deserialize_json(data: dict) -> GetQAppSessionMetadataOutput:
    out: GetQAppSessionMetadataOutput = {}  # type: ignore[typeddict-item]
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("sessionArn") is not None:
        out["session_arn"] = data["sessionArn"]
    else:
        out["session_arn"] = ""
    if data.get("sessionName") is not None:
        out["session_name"] = data["sessionName"]
    if data.get("sharingConfiguration") is not None:
        import capo_qapps.types.session_sharing_configuration

        out["sharing_configuration"] = (
            capo_qapps.types.session_sharing_configuration.deserialize_json(
                data["sharingConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "GetQAppSessionMetadataOutput.sharing_configuration required"
        )
    if data.get("sessionOwner") is not None:
        out["session_owner"] = data["sessionOwner"]
    return out
