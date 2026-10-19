"""Generated from Smithy shape ``com.amazonaws.qapps#QAppSessionData``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.q_apps_timestamp
    import capo_qapps.types.user
    import capo_qapps.types.uuid


class QAppSessionData(TypedDict, closed=True):
    card_id: "capo_qapps.types.uuid.UUID"
    """<p>The card Id associated with the response submitted for a Q App session.</p>"""
    value: NotRequired["object"]
    """<p>The response submitted for a Q App session.</p>"""
    user: "capo_qapps.types.user.User"
    """<p>The user who submitted the response for a Q App session.</p>"""
    submission_id: NotRequired["capo_qapps.types.uuid.UUID"]
    """<p>The unique identifier of the submission.</p>"""
    timestamp: NotRequired["capo_qapps.types.q_apps_timestamp.QAppsTimestamp"]
    """<p>The date and time when the session data is submitted.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QAppSessionData) -> dict:
    out: dict = {}
    out["cardId"] = value["card_id"]
    if "value" in value:
        out["value"] = value["value"]
    import capo_qapps.types.user

    out["user"] = capo_qapps.types.user.serialize_json(value["user"])
    if "submission_id" in value:
        out["submissionId"] = value["submission_id"]
    if "timestamp" in value:
        import capo_qapps.types.q_apps_timestamp

        out["timestamp"] = capo_qapps.types.q_apps_timestamp.serialize_json(
            value["timestamp"]
        )
    return out


def deserialize_json(data: dict) -> QAppSessionData:
    out: QAppSessionData = {}  # type: ignore[typeddict-item]
    if data.get("cardId") is not None:
        out["card_id"] = data["cardId"]
    else:
        out["card_id"] = ""
    if data.get("value") is not None:
        out["value"] = data["value"]
    if data.get("user") is not None:
        import capo_qapps.types.user

        out["user"] = capo_qapps.types.user.deserialize_json(data["user"])
    else:
        raise DeserializationError("QAppSessionData.user required")
    if data.get("submissionId") is not None:
        out["submission_id"] = data["submissionId"]
    if data.get("timestamp") is not None:
        import capo_qapps.types.q_apps_timestamp

        out["timestamp"] = capo_qapps.types.q_apps_timestamp.deserialize_json(
            data["timestamp"]
        )
    return out
