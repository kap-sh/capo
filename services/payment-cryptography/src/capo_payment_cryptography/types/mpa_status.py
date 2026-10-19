"""Generated from Smithy shape ``com.amazonaws.paymentcryptography#MpaStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_payment_cryptography.types.mpa_session_arn
    import capo_payment_cryptography.types.mpa_status_message
    import capo_payment_cryptography.types.session_status
    import capo_payment_cryptography.types.timestamp


class MpaStatus(TypedDict, closed=True):
    mpa_session_arn: "capo_payment_cryptography.types.mpa_session_arn.MpaSessionArn"
    """<p>The ARN of the MPA session.</p>"""
    status: "capo_payment_cryptography.types.session_status.SessionStatus"
    """<p>The current status of the MPA session.</p>"""
    initiation_date: "capo_payment_cryptography.types.timestamp.Timestamp"
    """<p>The date and time when the MPA session was initiated.</p>"""
    status_message: NotRequired[
        "capo_payment_cryptography.types.mpa_status_message.MpaStatusMessage"
    ]
    """<p>The message providing additional information about the MPA session status.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: MpaStatus) -> dict:
    out: dict = {}
    out["MpaSessionArn"] = value["mpa_session_arn"]
    out["Status"] = value["status"]
    import capo_payment_cryptography.types.timestamp

    out["InitiationDate"] = (
        capo_payment_cryptography.types.timestamp.serialize_aws_json_1_0(
            value["initiation_date"]
        )
    )
    if "status_message" in value:
        out["StatusMessage"] = value["status_message"]
    return out


def deserialize_aws_json_1_0(data: dict) -> MpaStatus:
    out: MpaStatus = {}  # type: ignore[typeddict-item]
    if data.get("MpaSessionArn") is not None:
        out["mpa_session_arn"] = data["MpaSessionArn"]
    else:
        out["mpa_session_arn"] = ""
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("InitiationDate") is not None:
        import capo_payment_cryptography.types.timestamp

        out["initiation_date"] = (
            capo_payment_cryptography.types.timestamp.deserialize_aws_json_1_0(
                data["InitiationDate"]
            )
        )
    else:
        import datetime

        out["initiation_date"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("StatusMessage") is not None:
        out["status_message"] = data["StatusMessage"]
    return out
