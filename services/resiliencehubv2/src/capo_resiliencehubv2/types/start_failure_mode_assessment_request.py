"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StartFailureModeAssessmentRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.client_token


class StartFailureModeAssessmentRequest(TypedDict, closed=True):
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    client_token: NotRequired["capo_resiliencehubv2.types.client_token.ClientToken"]


# --- restJson1 ser/de ---
def serialize_json(value: StartFailureModeAssessmentRequest) -> dict:
    out: dict = {}
    out["serviceArn"] = value["service_arn"]
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StartFailureModeAssessmentRequest:
    out: StartFailureModeAssessmentRequest = {}  # type: ignore[typeddict-item]
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    return out
