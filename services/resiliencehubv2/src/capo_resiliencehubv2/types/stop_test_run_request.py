"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#StopTestRunRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.arn
    import capo_resiliencehubv2.types.test_run_id


class StopTestRunRequest(TypedDict, closed=True):
    test_run_id: "capo_resiliencehubv2.types.test_run_id.TestRunId"
    """<p>The identifier of the test run to stop.</p>"""
    service_arn: "capo_resiliencehubv2.types.arn.Arn"
    """<p>The ARN of the service the test run belongs to.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopTestRunRequest) -> dict:
    out: dict = {}
    out["testRunId"] = value["test_run_id"]
    out["serviceArn"] = value["service_arn"]
    return out


def deserialize_json(data: dict) -> StopTestRunRequest:
    out: StopTestRunRequest = {}  # type: ignore[typeddict-item]
    if data.get("testRunId") is not None:
        out["test_run_id"] = data["testRunId"]
    else:
        out["test_run_id"] = ""
    if data.get("serviceArn") is not None:
        out["service_arn"] = data["serviceArn"]
    else:
        out["service_arn"] = ""
    return out
