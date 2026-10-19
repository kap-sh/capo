"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StartTestRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.test_id


class StartTestRunRequest(TypedDict, closed=True):
    test_id: "capo_resiliencehubv2.types.test_id.TestId"
    """<p>The identifier of the test to run.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTestRunRequest) -> dict:
    out: dict = {}
    out["testId"] = value["test_id"]
    out["serviceArn"] = value["service_arn"]
    return out


def deserialize_json(data: dict) -> StartTestRunRequest:
    out: StartTestRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("testId") is not None:
        out["test_id"] = data["testId"]
    else:
        out["test_id"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    return out
