"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#CreateAirflowUiUrlRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.expires_in_seconds_integer
    import capo_mwaa_serverless.types.session_duration_in_seconds_integer


class CreateAirflowUiUrlRequest(TypedDict, closed=True):
    expires_in_seconds: NotRequired[
        "capo_mwaa_serverless.types.expires_in_seconds_integer.ExpiresInSecondsInteger"
    ]
    """<p>Specifies the number of seconds that the launch URL stays valid. This value limits only the time to open the URL, not the length of the UI session. The default is 300.</p>"""
    session_duration_in_seconds: NotRequired[
        "capo_mwaa_serverless.types.session_duration_in_seconds_integer.SessionDurationInSecondsInteger"
    ]
    """<p>Specifies the number of seconds that the UI session lasts, starting from when you call this operation. The default is 43200 (12 hours).</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAirflowUiUrlRequest) -> dict:
    out: dict = {}
    if "expires_in_seconds" in value:
        out["ExpiresInSeconds"] = value["expires_in_seconds"]
    if "session_duration_in_seconds" in value:
        out["SessionDurationInSeconds"] = value["session_duration_in_seconds"]
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAirflowUiUrlRequest:
    out: CreateAirflowUiUrlRequest = {}  # type: ignore[typeddict-item]
    if data.get("ExpiresInSeconds") is not None:
        out["expires_in_seconds"] = data["ExpiresInSeconds"]
    if data.get("SessionDurationInSeconds") is not None:
        out["session_duration_in_seconds"] = data["SessionDurationInSeconds"]
    return out
