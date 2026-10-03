"""Generated from Smithy shape ``com.amazonaws.ssm#Session``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.access_type
    import capo_ssm.types.date_time
    import capo_ssm.types.document_name
    import capo_ssm.types.max_session_duration
    import capo_ssm.types.session_details
    import capo_ssm.types.session_id
    import capo_ssm.types.session_manager_output_url
    import capo_ssm.types.session_owner
    import capo_ssm.types.session_reason
    import capo_ssm.types.session_status
    import capo_ssm.types.session_target


class Session(TypedDict, closed=True):
    session_id: NotRequired["capo_ssm.types.session_id.SessionId"]
    """<p>The ID of the session.</p>"""
    target: NotRequired["capo_ssm.types.session_target.SessionTarget"]
    """<p>The managed node that the Session Manager session connected to.</p>"""
    status: NotRequired["capo_ssm.types.session_status.SessionStatus"]
    """<p>The status of the session. For example, "Connected" or "Terminated".</p>"""
    start_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time, in ISO-8601 Extended format, when the session began.</p>"""
    end_date: NotRequired["capo_ssm.types.date_time.DateTime"]
    """<p>The date and time, in ISO-8601 Extended format, when the session was terminated.</p>"""
    document_name: NotRequired["capo_ssm.types.document_name.DocumentName"]
    """<p>The name of the Session Manager SSM document used to define the parameters and plugin settings for the session. For example, <code>SSM-SessionManagerRunShell</code>.</p>"""
    owner: NotRequired["capo_ssm.types.session_owner.SessionOwner"]
    """<p>The ID of the Amazon Web Services user that started the session.</p>"""
    reason: NotRequired["capo_ssm.types.session_reason.SessionReason"]
    """<p>The reason for connecting to the instance.</p>"""
    details: NotRequired["capo_ssm.types.session_details.SessionDetails"]
    """<p>Reserved for future use.</p>"""
    output_url: NotRequired[
        "capo_ssm.types.session_manager_output_url.SessionManagerOutputUrl"
    ]
    """<p>Reserved for future use.</p>"""
    max_session_duration: NotRequired[
        "capo_ssm.types.max_session_duration.MaxSessionDuration"
    ]
    """<p>The maximum duration of a session before it terminates.</p>"""
    access_type: NotRequired["capo_ssm.types.access_type.AccessType"]
    """<p> <code>Standard</code> access type is the default for Session Manager sessions. <code>JustInTime</code> is the access type for <a href="https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-just-in-time-node-access.html">Just-in-time node access</a>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Session) -> dict:
    out: dict = {}
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "target" in value:
        out["Target"] = value["target"]
    if "status" in value:
        import capo_ssm.types.session_status

        out["Status"] = capo_ssm.types.session_status.serialize_aws_json_1_1(
            value["status"]
        )
    if "start_date" in value:
        import capo_ssm.types.date_time

        out["StartDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["start_date"]
        )
    if "end_date" in value:
        import capo_ssm.types.date_time

        out["EndDate"] = capo_ssm.types.date_time.serialize_aws_json_1_1(
            value["end_date"]
        )
    if "document_name" in value:
        out["DocumentName"] = value["document_name"]
    if "owner" in value:
        out["Owner"] = value["owner"]
    if "reason" in value:
        out["Reason"] = value["reason"]
    if "details" in value:
        out["Details"] = value["details"]
    if "output_url" in value:
        import capo_ssm.types.session_manager_output_url

        out["OutputUrl"] = (
            capo_ssm.types.session_manager_output_url.serialize_aws_json_1_1(
                value["output_url"]
            )
        )
    if "max_session_duration" in value:
        out["MaxSessionDuration"] = value["max_session_duration"]
    if "access_type" in value:
        import capo_ssm.types.access_type

        out["AccessType"] = capo_ssm.types.access_type.serialize_aws_json_1_1(
            value["access_type"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> Session:
    out: Session = {}  # type: ignore[typeddict-item]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    if data.get("Status") is not None:
        import capo_ssm.types.session_status

        out["status"] = capo_ssm.types.session_status.deserialize_aws_json_1_1(
            data["Status"]
        )
    if data.get("StartDate") is not None:
        import capo_ssm.types.date_time

        out["start_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["StartDate"]
        )
    if data.get("EndDate") is not None:
        import capo_ssm.types.date_time

        out["end_date"] = capo_ssm.types.date_time.deserialize_aws_json_1_1(
            data["EndDate"]
        )
    if data.get("DocumentName") is not None:
        out["document_name"] = data["DocumentName"]
    if data.get("Owner") is not None:
        out["owner"] = data["Owner"]
    if data.get("Reason") is not None:
        out["reason"] = data["Reason"]
    if data.get("Details") is not None:
        out["details"] = data["Details"]
    if data.get("OutputUrl") is not None:
        import capo_ssm.types.session_manager_output_url

        out["output_url"] = (
            capo_ssm.types.session_manager_output_url.deserialize_aws_json_1_1(
                data["OutputUrl"]
            )
        )
    if data.get("MaxSessionDuration") is not None:
        out["max_session_duration"] = data["MaxSessionDuration"]
    if data.get("AccessType") is not None:
        import capo_ssm.types.access_type

        out["access_type"] = capo_ssm.types.access_type.deserialize_aws_json_1_1(
            data["AccessType"]
        )
    return out
