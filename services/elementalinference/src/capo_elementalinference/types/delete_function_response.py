"""Generated from Smithy shape ``com.amazonaws.elementalinference#DeleteFunctionResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_elementalinference.types.function_arn
    import capo_elementalinference.types.function_id
    import capo_elementalinference.types.function_status


class DeleteFunctionResponse(TypedDict, closed=True):
    arn: "capo_elementalinference.types.function_arn.FunctionArn"
    """<p>The ARN of the function.</p>"""
    id: "capo_elementalinference.types.function_id.FunctionId"
    """<p>The ID of the function.</p>"""
    status: "capo_elementalinference.types.function_status.FunctionStatus"
    """<p>The status of the function. A successful request returns DELETING. Elemental Inference removes the function before it returns the response. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DeleteFunctionResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["id"] = value["id"]
    import capo_elementalinference.types.function_status

    out["status"] = capo_elementalinference.types.function_status.serialize_json(
        value["status"]
    )
    return out


def deserialize_json(data: dict) -> DeleteFunctionResponse:
    out: DeleteFunctionResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("status") is not None:
        import capo_elementalinference.types.function_status

        out["status"] = capo_elementalinference.types.function_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_elementalinference.types.function_status.FunctionStatus", ""
        )
    return out
