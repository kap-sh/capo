"""Generated from Smithy shape ``com.amazonaws.connect#StopTestCaseExecutionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.client_token
    import capo_connect.types.instance_id
    import capo_connect.types.test_case_execution_id
    import capo_connect.types.test_case_id


class StopTestCaseExecutionRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Amazon Connect instance.</p>"""
    test_case_execution_id: (
        "capo_connect.types.test_case_execution_id.TestCaseExecutionId"
    )
    """<p>The identifier of the test case execution to stop.</p>"""
    test_case_id: "capo_connect.types.test_case_id.TestCaseId"
    """<p>The identifier of the test case.</p>"""
    client_token: NotRequired["capo_connect.types.client_token.ClientToken"]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the Amazon Web Services SDK populates this field. For more information about idempotency, see <a href="https://aws.amazon.com/builders-library/making-retries-safe-with-idempotent-APIs/">Making retries safe with idempotent APIs</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StopTestCaseExecutionRequest) -> dict:
    out: dict = {}
    if "client_token" in value:
        out["ClientToken"] = value["client_token"]
    return out


def deserialize_json(data: dict) -> StopTestCaseExecutionRequest:
    out: StopTestCaseExecutionRequest = {}  # type: ignore[typeddict-item]
    if data.get("ClientToken") is not None:
        out["client_token"] = data["ClientToken"]
    return out
