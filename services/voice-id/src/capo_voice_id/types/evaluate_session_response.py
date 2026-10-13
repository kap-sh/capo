"""Generated from Smithy shape ``com.amazonaws.voiceid#EvaluateSessionResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_voice_id.types.authentication_result
    import capo_voice_id.types.domain_id
    import capo_voice_id.types.fraud_detection_result
    import capo_voice_id.types.session_id
    import capo_voice_id.types.session_name
    import capo_voice_id.types.streaming_status


class EvaluateSessionResponse(TypedDict, closed=True):
    domain_id: NotRequired["capo_voice_id.types.domain_id.DomainId"]
    """<p>The identifier of the domain that contains the session.</p>"""
    session_id: NotRequired["capo_voice_id.types.session_id.SessionId"]
    """<p>The service-generated identifier of the session.</p>"""
    session_name: NotRequired["capo_voice_id.types.session_name.SessionName"]
    """<p>The client-provided name of the session.</p>"""
    streaming_status: NotRequired[
        "capo_voice_id.types.streaming_status.StreamingStatus"
    ]
    """<p>The current status of audio streaming for this session. This field is useful to infer next steps when the Authentication or Fraud Detection results are empty or the decision is <code>NOT_ENOUGH_SPEECH</code>. In this situation, if the <code>StreamingStatus</code> is <code>ONGOING/PENDING_CONFIGURATION</code>, it can mean that the client should call the API again later, after Voice ID has enough audio to produce a result. If the decision remains <code>NOT_ENOUGH_SPEECH</code> even after <code>StreamingStatus</code> is <code>ENDED</code>, it means that the previously streamed session did not have enough speech to perform evaluation, and a new streaming session is needed to try again.</p>"""
    authentication_result: NotRequired[
        "capo_voice_id.types.authentication_result.AuthenticationResult"
    ]
    """<p>Details resulting from the authentication process, such as authentication decision and authentication score.</p>"""
    fraud_detection_result: NotRequired[
        "capo_voice_id.types.fraud_detection_result.FraudDetectionResult"
    ]
    """<p>Details resulting from the fraud detection process, such as fraud detection decision and risk score.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluateSessionResponse) -> dict:
    out: dict = {}
    if "domain_id" in value:
        out["DomainId"] = value["domain_id"]
    if "session_id" in value:
        out["SessionId"] = value["session_id"]
    if "session_name" in value:
        out["SessionName"] = value["session_name"]
    if "streaming_status" in value:
        out["StreamingStatus"] = value["streaming_status"]
    if "authentication_result" in value:
        import capo_voice_id.types.authentication_result

        out["AuthenticationResult"] = (
            capo_voice_id.types.authentication_result.serialize_aws_json_1_0(
                value["authentication_result"]
            )
        )
    if "fraud_detection_result" in value:
        import capo_voice_id.types.fraud_detection_result

        out["FraudDetectionResult"] = (
            capo_voice_id.types.fraud_detection_result.serialize_aws_json_1_0(
                value["fraud_detection_result"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> EvaluateSessionResponse:
    out: EvaluateSessionResponse = {}  # type: ignore[typeddict-item]
    if data.get("DomainId") is not None:
        out["domain_id"] = data["DomainId"]
    if data.get("SessionId") is not None:
        out["session_id"] = data["SessionId"]
    if data.get("SessionName") is not None:
        out["session_name"] = data["SessionName"]
    if data.get("StreamingStatus") is not None:
        out["streaming_status"] = data["StreamingStatus"]
    if data.get("AuthenticationResult") is not None:
        import capo_voice_id.types.authentication_result

        out["authentication_result"] = (
            capo_voice_id.types.authentication_result.deserialize_aws_json_1_0(
                data["AuthenticationResult"]
            )
        )
    if data.get("FraudDetectionResult") is not None:
        import capo_voice_id.types.fraud_detection_result

        out["fraud_detection_result"] = (
            capo_voice_id.types.fraud_detection_result.deserialize_aws_json_1_0(
                data["FraudDetectionResult"]
            )
        )
    return out


def redact_sensitive(value: EvaluateSessionResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "authentication_result" in value:
        import capo_voice_id.types.authentication_result

        out["authentication_result"] = (
            capo_voice_id.types.authentication_result.redact_sensitive(
                value["authentication_result"]
            )
        )
    return out
