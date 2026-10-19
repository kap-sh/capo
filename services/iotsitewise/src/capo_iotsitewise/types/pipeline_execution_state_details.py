"""Generated from Smithy shape ``com.amazonaws.iotsitewise#PipelineExecutionStateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.detailed_error_list
    import capo_iotsitewise.types.pipeline_error_code


class PipelineExecutionStateDetails(TypedDict, closed=True):
    code: NotRequired["capo_iotsitewise.types.pipeline_error_code.PipelineErrorCode"]
    """<p>Classification of the failure. Present when the execution failed.</p>"""
    message: "str"
    """<p>Human-readable description of the outcome. For a failed execution, this describes why it failed; for a cancelled execution, this is the reason you supplied when calling CancelPipelineExecution.</p>"""
    details: NotRequired["capo_iotsitewise.types.detailed_error_list.DetailedErrorList"]
    """<p>Per-step error entries to help diagnose a failed execution. Present when the execution failed.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipelineExecutionStateDetails) -> dict:
    out: dict = {}
    if "code" in value:
        import capo_iotsitewise.types.pipeline_error_code

        out["code"] = capo_iotsitewise.types.pipeline_error_code.serialize_json(
            value["code"]
        )
    out["message"] = value["message"]
    if "details" in value:
        import capo_iotsitewise.types.detailed_error_list

        out["details"] = capo_iotsitewise.types.detailed_error_list.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> PipelineExecutionStateDetails:
    out: PipelineExecutionStateDetails = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.pipeline_error_code

        out["code"] = capo_iotsitewise.types.pipeline_error_code.deserialize_json(
            data["code"]
        )
    if data.get("message") is not None:
        out["message"] = data["message"]
    else:
        out["message"] = ""
    if data.get("details") is not None:
        import capo_iotsitewise.types.detailed_error_list

        out["details"] = capo_iotsitewise.types.detailed_error_list.deserialize_json(
            data["details"]
        )
    return out
