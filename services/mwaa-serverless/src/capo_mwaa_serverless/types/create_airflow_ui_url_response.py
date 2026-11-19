"""Generated from Smithy shape ``com.amazonaws.mwaaserverless#CreateAirflowUiUrlResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_mwaa_serverless.types.authorized_url_string
    import capo_mwaa_serverless.types.session_id_string
    import capo_mwaa_serverless.types.timestamp_value


class CreateAirflowUiUrlResponse(TypedDict, closed=True):
    authorized_url: (
        "capo_mwaa_serverless.types.authorized_url_string.AuthorizedUrlString"
    )
    """<p>The launch URL that opens the Airflow UI. Open it in a browser before <code>UrlExpiresAt</code>. The UI session uses the permissions of the identity that called this operation.</p>"""
    session_id: "capo_mwaa_serverless.types.session_id_string.SessionIdString"
    """<p>The URL starts a UI session that has this identifier.</p>"""
    url_expires_at: "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    """<p>The launch URL stops being valid at this time. The value is in ISO 8601 date-time format.</p>"""
    session_expires_at: "capo_mwaa_serverless.types.timestamp_value.TimestampValue"
    """<p>The UI session ends at this time. The value is in ISO 8601 date-time format. After this time, create a new URL to open the UI again.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateAirflowUiUrlResponse) -> dict:
    out: dict = {}
    out["AuthorizedUrl"] = value["authorized_url"]
    out["SessionId"] = value["session_id"]
    import capo_mwaa_serverless.types.timestamp_value

    out["UrlExpiresAt"] = (
        capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
            value["url_expires_at"]
        )
    )
    import capo_mwaa_serverless.types.timestamp_value

    out["SessionExpiresAt"] = (
        capo_mwaa_serverless.types.timestamp_value.serialize_aws_json_1_0(
            value["session_expires_at"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateAirflowUiUrlResponse:
    out: CreateAirflowUiUrlResponse = {}  # type: ignore[typeddict-item]
    if data.get("AuthorizedUrl") is not None:
        out["authorized_url"] = data["AuthorizedUrl"]
    else:
        out["authorized_url"] = ""
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    else:
        out["session_id"] = ""
    if data.get("UrlExpiresAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["url_expires_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["UrlExpiresAt"]
            )
        )
    else:
        import datetime

        out["url_expires_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("SessionExpiresAt") is not None:
        import capo_mwaa_serverless.types.timestamp_value

        out["session_expires_at"] = (
            capo_mwaa_serverless.types.timestamp_value.deserialize_aws_json_1_0(
                data["SessionExpiresAt"]
            )
        )
    else:
        import datetime

        out["session_expires_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    return out


def redact_sensitive(value: CreateAirflowUiUrlResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authorized_url" in value:
        out["authorized_url"] = "*** Sensitive Data Redacted ***"
    if "session_id" in value:
        out["session_id"] = "*** Sensitive Data Redacted ***"
    return out
