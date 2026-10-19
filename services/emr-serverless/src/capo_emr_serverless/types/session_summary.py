"""Generated from Smithy shape ``com.amazonaws.emrserverless#SessionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_serverless.types.application_id
    import capo_emr_serverless.types.date
    import capo_emr_serverless.types.iam_role_arn
    import capo_emr_serverless.types.release_label
    import capo_emr_serverless.types.request_identity_user_arn
    import capo_emr_serverless.types.session_arn
    import capo_emr_serverless.types.session_id
    import capo_emr_serverless.types.session_state
    import capo_emr_serverless.types.string256
    import capo_emr_serverless.types.string1024


class SessionSummary(TypedDict, closed=True):
    application_id: "capo_emr_serverless.types.application_id.ApplicationId"
    """<p>The ID of the application that the session belongs to.</p>"""
    session_id: "capo_emr_serverless.types.session_id.SessionId"
    """<p>The ID of the session.</p>"""
    arn: "capo_emr_serverless.types.session_arn.SessionArn"
    """<p>The Amazon Resource Name (ARN) of the session.</p>"""
    name: NotRequired["capo_emr_serverless.types.string256.String256"]
    """<p>The optional name of the session.</p>"""
    state: "capo_emr_serverless.types.session_state.SessionState"
    """<p>The state of the session.</p>"""
    state_details: "capo_emr_serverless.types.string1024.String1024"
    """<p>Additional details about the current state of the session.</p>"""
    release_label: "capo_emr_serverless.types.release_label.ReleaseLabel"
    """<p>The Amazon EMR release label associated with the session.</p>"""
    execution_role_arn: "capo_emr_serverless.types.iam_role_arn.IAMRoleArn"
    """<p>The Amazon Resource Name (ARN) of the execution role for the session.</p>"""
    created_by: (
        "capo_emr_serverless.types.request_identity_user_arn.RequestIdentityUserArn"
    )
    """<p>The IAM principal that created the session.</p>"""
    created_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time that the session was created.</p>"""
    updated_at: "capo_emr_serverless.types.date.Date"
    """<p>The date and time that the session was last updated.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SessionSummary) -> dict:
    out: dict = {}
    out["applicationId"] = value["application_id"]
    out["sessionId"] = value["session_id"]
    out["arn"] = value["arn"]
    if "name" in value:
        out["name"] = value["name"]
    out["state"] = value["state"]
    out["stateDetails"] = value["state_details"]
    out["releaseLabel"] = value["release_label"]
    out["executionRoleArn"] = value["execution_role_arn"]
    out["createdBy"] = value["created_by"]
    import capo_emr_serverless.types.date

    out["createdAt"] = capo_emr_serverless.types.date.serialize_json(
        value["created_at"]
    )
    import capo_emr_serverless.types.date

    out["updatedAt"] = capo_emr_serverless.types.date.serialize_json(
        value["updated_at"]
    )
    return out


def deserialize_json(data: dict) -> SessionSummary:
    out: SessionSummary = {}  # type: ignore[typeddict-item]
    if data.get("applicationId") is not None:
        out["application_id"] = data["applicationId"]
    else:
        out["application_id"] = ""
    if data.get("sessionId") is not None:
        out["session_id"] = data["sessionId"]
    else:
        out["session_id"] = ""
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("state") is not None:
        out["state"] = data["state"]
    else:
        out["state"] = ""
    if data.get("stateDetails") is not None:
        out["state_details"] = data["stateDetails"]
    else:
        out["state_details"] = ""
    if data.get("releaseLabel") is not None:
        out["release_label"] = data["releaseLabel"]
    else:
        out["release_label"] = ""
    if data.get("executionRoleArn") is not None:
        out["execution_role_arn"] = data["executionRoleArn"]
    else:
        out["execution_role_arn"] = ""
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("createdAt") is not None:
        import capo_emr_serverless.types.date

        out["created_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_emr_serverless.types.date

        out["updated_at"] = capo_emr_serverless.types.date.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    return out
