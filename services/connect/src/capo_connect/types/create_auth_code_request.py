"""Generated from Smithy shape ``com.amazonaws.connect#CreateAuthCodeRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.auth_scope
    import capo_connect.types.instance_id
    import capo_connect.types.max_session_duration_minutes
    import capo_connect.types.session_inactivity_duration_minutes


class CreateAuthCodeRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    scope: "capo_connect.types.auth_scope.AuthScope"
    """<p>The scope for the authorization code. Defines the permissions and access boundaries for the session.</p>"""
    max_session_duration_minutes: NotRequired[
        "capo_connect.types.max_session_duration_minutes.MaxSessionDurationMinutes"
    ]
    """<p>The maximum duration of the session, in minutes. Minimum value of 1440 (24 hours). Maximum value of 43200 (30 days). If no value is provided, the session will expire after 400 days.</p>"""
    session_inactivity_duration_minutes: "capo_connect.types.session_inactivity_duration_minutes.SessionInactivityDurationMinutes"
    """<p>The duration of inactivity, in minutes, after which the session expires. Minimum value of 1440 (24 hours). Maximum value of 20160 (14 days).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAuthCodeRequest) -> dict:
    out: dict = {}
    import capo_connect.types.auth_scope

    out["Scope"] = capo_connect.types.auth_scope.serialize_json(value["scope"])
    if "max_session_duration_minutes" in value:
        out["MaxSessionDurationMinutes"] = value["max_session_duration_minutes"]
    out["SessionInactivityDurationMinutes"] = value.get(
        "session_inactivity_duration_minutes", 0
    )
    return out


def deserialize_json(data: dict) -> CreateAuthCodeRequest:
    out: CreateAuthCodeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_connect.types.auth_scope

        out["scope"] = capo_connect.types.auth_scope.deserialize_json(data["Scope"])
    else:
        raise DeserializationError("CreateAuthCodeRequest.scope required")
    if data.get("MaxSessionDurationMinutes") is not None:
        out["max_session_duration_minutes"] = data["MaxSessionDurationMinutes"]
    if data.get("SessionInactivityDurationMinutes") is not None:
        out["session_inactivity_duration_minutes"] = data[
            "SessionInactivityDurationMinutes"
        ]
    else:
        out["session_inactivity_duration_minutes"] = 0
    return out
