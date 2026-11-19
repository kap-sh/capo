"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionRuntimeConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_runtime_alias
    import capo_lambda.types.function_runtime_arn


class FunctionRuntimeConfig(TypedDict, closed=True):
    runtime_arn: "capo_lambda.types.function_runtime_arn.FunctionRuntimeArn"
    """<p>The Amazon Resource Name (ARN) of the customer-managed runtime that your function uses.</p>"""
    runtime_alias: "capo_lambda.types.function_runtime_alias.FunctionRuntimeAlias"
    """<p>The name of the customer-managed runtime alias that your function uses. A runtime alias is a name that points to a runtime version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionRuntimeConfig) -> dict:
    out: dict = {}
    out["RuntimeArn"] = value["runtime_arn"]
    out["RuntimeAlias"] = value["runtime_alias"]
    return out


def deserialize_json(data: dict) -> FunctionRuntimeConfig:
    out: FunctionRuntimeConfig = {}  # type: ignore[typeddict-item]
    if data.get("RuntimeArn") is not None:
        out["runtime_arn"] = data["RuntimeArn"]
    else:
        out["runtime_arn"] = ""
    if data.get("RuntimeAlias") is not None:
        out["runtime_alias"] = data["RuntimeAlias"]
    else:
        out["runtime_alias"] = ""
    return out
