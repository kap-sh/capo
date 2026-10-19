"""Generated from Smithy shape ``com.amazonaws.bcmdataexports#ExecutionReference``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_bcm_data_exports.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bcm_data_exports.types.execution_status
    import capo_bcm_data_exports.types.generic_string


class ExecutionReference(TypedDict, closed=True):
    execution_id: "capo_bcm_data_exports.types.generic_string.GenericString"
    """<p>The ID for this specific execution.</p>"""
    execution_status: "capo_bcm_data_exports.types.execution_status.ExecutionStatus"
    """<p>The status of this specific execution.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExecutionReference) -> dict:
    out: dict = {}
    out["ExecutionId"] = value["execution_id"]
    import capo_bcm_data_exports.types.execution_status

    out["ExecutionStatus"] = (
        capo_bcm_data_exports.types.execution_status.serialize_aws_json_1_1(
            value["execution_status"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> ExecutionReference:
    out: ExecutionReference = {}  # type: ignore[typeddict-item]
    if data.get("ExecutionId") is not None:
        out["execution_id"] = data["ExecutionId"]
    else:
        out["execution_id"] = ""
    if data.get("ExecutionStatus") is not None:
        import capo_bcm_data_exports.types.execution_status

        out["execution_status"] = (
            capo_bcm_data_exports.types.execution_status.deserialize_aws_json_1_1(
                data["ExecutionStatus"]
            )
        )
    else:
        raise DeserializationError("ExecutionReference.execution_status required")
    return out
