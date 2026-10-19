"""Generated from Smithy shape ``com.amazonaws.iotsitewise#ComputeNodeExecutionStateDetails``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_iotsitewise.types.compute_node_error_code
    import capo_iotsitewise.types.detailed_error_list


class ComputeNodeExecutionStateDetails(TypedDict, closed=True):
    code: "capo_iotsitewise.types.compute_node_error_code.ComputeNodeErrorCode"
    """<p>Classification of the failure.</p>"""
    message: "str"
    """<p>Human-readable description of why the compute node failed.</p>"""
    details: NotRequired["capo_iotsitewise.types.detailed_error_list.DetailedErrorList"]
    """<p>Detailed error entries to help diagnose the failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ComputeNodeExecutionStateDetails) -> dict:
    out: dict = {}
    import capo_iotsitewise.types.compute_node_error_code

    out["code"] = capo_iotsitewise.types.compute_node_error_code.serialize_json(
        value["code"]
    )
    out["message"] = value["message"]
    if "details" in value:
        import capo_iotsitewise.types.detailed_error_list

        out["details"] = capo_iotsitewise.types.detailed_error_list.serialize_json(
            value["details"]
        )
    return out


def deserialize_json(data: dict) -> ComputeNodeExecutionStateDetails:
    out: ComputeNodeExecutionStateDetails = {}  # type: ignore[typeddict-item]
    if data.get("code") is not None:
        import capo_iotsitewise.types.compute_node_error_code

        out["code"] = capo_iotsitewise.types.compute_node_error_code.deserialize_json(
            data["code"]
        )
    else:
        import typing

        out["code"] = typing.cast(
            "capo_iotsitewise.types.compute_node_error_code.ComputeNodeErrorCode", ""
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
