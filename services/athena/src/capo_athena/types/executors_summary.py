"""Generated from Smithy shape ``com.amazonaws.athena#ExecutorsSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_athena.types.executor_id
    import capo_athena.types.executor_state
    import capo_athena.types.executor_type
    import capo_athena.types.long


class ExecutorsSummary(TypedDict, closed=True):
    executor_id: "capo_athena.types.executor_id.ExecutorId"
    """<p>The UUID of the executor.</p>"""
    executor_type: NotRequired["capo_athena.types.executor_type.ExecutorType"]
    """<p>The type of executor used for the application (<code>COORDINATOR</code>, <code>GATEWAY</code>, or <code>WORKER</code>).</p>"""
    start_date_time: NotRequired["capo_athena.types.long.Long"]
    """<p>The date and time that the executor started.</p>"""
    termination_date_time: NotRequired["capo_athena.types.long.Long"]
    """<p>The date and time that the executor was terminated.</p>"""
    executor_state: NotRequired["capo_athena.types.executor_state.ExecutorState"]
    """<p>The processing state of the executor. A description of each state follows.</p> <p> <code>CREATING</code> - The executor is being started, including acquiring resources.</p> <p> <code>CREATED</code> - The executor has been started.</p> <p> <code>REGISTERED</code> - The executor has been registered.</p> <p> <code>TERMINATING</code> - The executor is in the process of shutting down.</p> <p> <code>TERMINATED</code> - The executor is no longer running.</p> <p> <code>FAILED</code> - Due to a failure, the executor is no longer running.</p>"""
    executor_size: NotRequired["capo_athena.types.long.Long"]
    """<p>The smallest unit of compute that a session can request from Athena. Size is measured in data processing unit (DPU) values, a relative measure of processing power.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutorsSummary) -> dict:
    out: dict = {}
    out["ExecutorId"] = value["executor_id"]
    if "executor_type" in value:
        import capo_athena.types.executor_type

        out["ExecutorType"] = capo_athena.types.executor_type.serialize_aws_json_1_1(
            value["executor_type"]
        )
    if "start_date_time" in value:
        out["StartDateTime"] = value["start_date_time"]
    if "termination_date_time" in value:
        out["TerminationDateTime"] = value["termination_date_time"]
    if "executor_state" in value:
        import capo_athena.types.executor_state

        out["ExecutorState"] = capo_athena.types.executor_state.serialize_aws_json_1_1(
            value["executor_state"]
        )
    if "executor_size" in value:
        out["ExecutorSize"] = value["executor_size"]
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutorsSummary:
    out: ExecutorsSummary = {}  # type: ignore[typeddict-item]
    if data.get("ExecutorId") is not None:
        out["executor_id"] = data["ExecutorId"]
    else:
        out["executor_id"] = ""
    if data.get("ExecutorType") is not None:
        import capo_athena.types.executor_type

        out["executor_type"] = capo_athena.types.executor_type.deserialize_aws_json_1_1(
            data["ExecutorType"]
        )
    if data.get("StartDateTime") is not None:
        out["start_date_time"] = data["StartDateTime"]
    if data.get("TerminationDateTime") is not None:
        out["termination_date_time"] = data["TerminationDateTime"]
    if data.get("ExecutorState") is not None:
        import capo_athena.types.executor_state

        out["executor_state"] = (
            capo_athena.types.executor_state.deserialize_aws_json_1_1(
                data["ExecutorState"]
            )
        )
    if data.get("ExecutorSize") is not None:
        out["executor_size"] = data["ExecutorSize"]
    return out
