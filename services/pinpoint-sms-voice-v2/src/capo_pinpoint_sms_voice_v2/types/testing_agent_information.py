"""Generated from Smithy shape ``com.amazonaws.pinpointsmsvoicev2#TestingAgentInformation``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pinpoint_sms_voice_v2.types.testing_agent_status


class TestingAgentInformation(TypedDict, closed=True):
    status: "capo_pinpoint_sms_voice_v2.types.testing_agent_status.TestingAgentStatus"
    """<p>The current status of the testing agent.</p>"""
    testing_agent_id: NotRequired["str"]
    """<p>The unique identifier for the testing agent.</p>"""
    registration_id: "str"
    """<p>The unique identifier of the registration associated with the testing agent.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: TestingAgentInformation) -> dict:
    out: dict = {}
    out["Status"] = value["status"]
    if "testing_agent_id" in value:
        out["TestingAgentId"] = value["testing_agent_id"]
    out["RegistrationId"] = value["registration_id"]
    return out


def deserialize_aws_json_1_0(data: dict) -> TestingAgentInformation:
    out: TestingAgentInformation = {}  # type: ignore[typeddict-item]
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    else:
        out["status"] = ""
    if data.get("TestingAgentId") is not None:
        out["testing_agent_id"] = data["TestingAgentId"]
    if data.get("RegistrationId") is not None:
        out["registration_id"] = data["RegistrationId"]
    else:
        out["registration_id"] = ""
    return out
