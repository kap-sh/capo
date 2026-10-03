"""Generated from Smithy shape ``com.amazonaws.synthetics#CanaryRunStatus``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_synthetics.types.canary_run_state
    import capo_synthetics.types.canary_run_state_reason_code
    import capo_synthetics.types.canary_run_test_result
    import capo_synthetics.types.string


class CanaryRunStatus(TypedDict, closed=True):
    state: NotRequired["capo_synthetics.types.canary_run_state.CanaryRunState"]
    """<p>The current state of the run.</p>"""
    state_reason: NotRequired["capo_synthetics.types.string.String"]
    """<p>If run of the canary failed, this field contains the reason for the error.</p>"""
    state_reason_code: NotRequired[
        "capo_synthetics.types.canary_run_state_reason_code.CanaryRunStateReasonCode"
    ]
    """<p>If this value is <code>CANARY_FAILURE</code>, either the canary script failed or Synthetics ran into a fatal error when running the canary. For example, a canary timeout misconfiguration setting can cause the canary to timeout before Synthetics can evaluate its status. </p> <p> If this value is <code>EXECUTION_FAILURE</code>, a non-critical failure occurred such as failing to save generated debug artifacts (for example, screenshots or har files).</p> <p>If both types of failures occurred, the <code>CANARY_FAILURE</code> takes precedence. To understand the exact error, use the <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunStatus.html">StateReason</a> API.</p>"""
    test_result: NotRequired[
        "capo_synthetics.types.canary_run_test_result.CanaryRunTestResult"
    ]
    """<p>Specifies the status of canary script for this run. When Synthetics tries to determine the status but fails, the result is marked as <code>UNKNOWN</code>. For the overall status of canary run, see <a href="https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_CanaryRunStatus.html">State</a>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CanaryRunStatus) -> dict:
    out: dict = {}
    if "state" in value:
        import capo_synthetics.types.canary_run_state

        out["State"] = capo_synthetics.types.canary_run_state.serialize_json(
            value["state"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_code" in value:
        import capo_synthetics.types.canary_run_state_reason_code

        out["StateReasonCode"] = (
            capo_synthetics.types.canary_run_state_reason_code.serialize_json(
                value["state_reason_code"]
            )
        )
    if "test_result" in value:
        import capo_synthetics.types.canary_run_test_result

        out["TestResult"] = capo_synthetics.types.canary_run_test_result.serialize_json(
            value["test_result"]
        )
    return out


def deserialize_json(data: dict) -> CanaryRunStatus:
    out: CanaryRunStatus = {}  # type: ignore[typeddict-item]
    if data.get("State") is not None:
        import capo_synthetics.types.canary_run_state

        out["state"] = capo_synthetics.types.canary_run_state.deserialize_json(
            data["State"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonCode") is not None:
        import capo_synthetics.types.canary_run_state_reason_code

        out["state_reason_code"] = (
            capo_synthetics.types.canary_run_state_reason_code.deserialize_json(
                data["StateReasonCode"]
            )
        )
    if data.get("TestResult") is not None:
        import capo_synthetics.types.canary_run_test_result

        out["test_result"] = (
            capo_synthetics.types.canary_run_test_result.deserialize_json(
                data["TestResult"]
            )
        )
    return out
