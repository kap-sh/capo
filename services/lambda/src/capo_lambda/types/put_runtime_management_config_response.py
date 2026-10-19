"""Generated from Smithy shape ``com.amazonaws.lambda#PutRuntimeManagementConfigResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_arn
    import capo_lambda.types.runtime_version_arn
    import capo_lambda.types.update_runtime_on


class PutRuntimeManagementConfigResponse(TypedDict, closed=True):
    update_runtime_on: "capo_lambda.types.update_runtime_on.UpdateRuntimeOn"
    """<p>The runtime update mode.</p>"""
    function_arn: "capo_lambda.types.function_arn.FunctionArn"
    """<p>The ARN of the function</p>"""
    runtime_version_arn: NotRequired[
        "capo_lambda.types.runtime_version_arn.RuntimeVersionArn"
    ]
    """<p>The ARN of the runtime the function is configured to use. If the runtime update mode is <b>manual</b>, the ARN is returned, otherwise <code>null</code> is returned.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutRuntimeManagementConfigResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.update_runtime_on

    out["UpdateRuntimeOn"] = capo_lambda.types.update_runtime_on.serialize_json(
        value["update_runtime_on"]
    )
    out["FunctionArn"] = value["function_arn"]
    if "runtime_version_arn" in value:
        out["RuntimeVersionArn"] = value["runtime_version_arn"]
    return out


def deserialize_json(data: dict) -> PutRuntimeManagementConfigResponse:
    out: PutRuntimeManagementConfigResponse = {}  # type: ignore[typeddict-item]
    if data.get("UpdateRuntimeOn") is not None:
        import capo_lambda.types.update_runtime_on

        out["update_runtime_on"] = capo_lambda.types.update_runtime_on.deserialize_json(
            data["UpdateRuntimeOn"]
        )
    else:
        import typing

        out["update_runtime_on"] = typing.cast(
            "capo_lambda.types.update_runtime_on.UpdateRuntimeOn", ""
        )
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    else:
        out["function_arn"] = ""
    if data.get("RuntimeVersionArn") is not None:
        out["runtime_version_arn"] = data["RuntimeVersionArn"]
    return out
