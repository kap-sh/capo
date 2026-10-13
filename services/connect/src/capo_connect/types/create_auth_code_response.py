"""Generated from Smithy shape ``com.amazonaws.connect#CreateAuthCodeResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.auth_code
    import capo_connect.types.auth_code_entity_type
    import capo_connect.types.entity_id
    import capo_connect.types.session_id


class CreateAuthCodeResponse(TypedDict, closed=True):
    auth_code: NotRequired["capo_connect.types.auth_code.AuthCode"]
    """<p>The authorization code to use for establishing a session.</p>"""
    session_id: NotRequired["capo_connect.types.session_id.SessionId"]
    """<p>The identifier of the session created with the authorization code.</p>"""
    entity_type: NotRequired[
        "capo_connect.types.auth_code_entity_type.AuthCodeEntityType"
    ]
    """<p>The type of entity associated with the authorization code.</p>"""
    entity_id: NotRequired["capo_connect.types.entity_id.EntityId"]
    """<p>The identifier of the entity associated with the authorization code.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAuthCodeResponse) -> dict:
    out: dict = {}
    if "auth_code" in value:
        out["AuthCode"] = value["auth_code"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "entity_type" in value:
        import capo_connect.types.auth_code_entity_type

        out["EntityType"] = capo_connect.types.auth_code_entity_type.serialize_json(
            value["entity_type"]
        )
    if "entity_id" in value:
        out["EntityId"] = value["entity_id"]
    return out


def deserialize_json(data: dict) -> CreateAuthCodeResponse:
    out: CreateAuthCodeResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuthCode") is not None:
        out["auth_code"] = data["AuthCode"]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("EntityType") is not None:
        import capo_connect.types.auth_code_entity_type

        out["entity_type"] = capo_connect.types.auth_code_entity_type.deserialize_json(
            data["EntityType"]
        )
    if data.get("EntityId") is not None:
        out["entity_id"] = data["EntityId"]
    return out


def redact_sensitive(value: CreateAuthCodeResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "auth_code" in value:
        out["auth_code"] = "*** Sensitive Data Redacted ***"
    return out
