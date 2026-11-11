"""Generated from Smithy shape ``com.amazonaws.lakeformation#GetGlueFunctionSessionContextRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lakeformation.types.resource_arn_list
    import capo_lakeformation.types.session_duration_second_integer


class GetGlueFunctionSessionContextRequest(TypedDict, closed=True):
    user_defined_function_arns: (
        "capo_lakeformation.types.resource_arn_list.ResourceArnList"
    )
    """<p>The ARNs of one or more user-defined functions to include in the session context, each in the format <code>arn:aws:glue:<i>region</i>:<i>account-id</i>:userDefinedFunction/<i>database-name</i>/<i>function-name</i> </code>.</p>"""
    duration_seconds: NotRequired[
        "capo_lakeformation.types.session_duration_second_integer.SessionDurationSecondInteger"
    ]
    """<p>The number of seconds the session context is valid. The default is 86,400 (24 hours).</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetGlueFunctionSessionContextRequest) -> dict:
    out: dict = {}
    import capo_lakeformation.types.resource_arn_list

    out["UserDefinedFunctionArns"] = (
        capo_lakeformation.types.resource_arn_list.serialize_json(
            value["user_defined_function_arns"]
        )
    )
    if "duration_seconds" in value:
        out["DurationSeconds"] = value["duration_seconds"]
    return out


def deserialize_json(data: dict) -> GetGlueFunctionSessionContextRequest:
    out: GetGlueFunctionSessionContextRequest = {}  # type: ignore[typeddict-item]
    if data.get("UserDefinedFunctionArns") is not None:
        import capo_lakeformation.types.resource_arn_list

        out["user_defined_function_arns"] = (
            capo_lakeformation.types.resource_arn_list.deserialize_json(
                data["UserDefinedFunctionArns"]
            )
        )
    else:
        out["user_defined_function_arns"] = []
    if data.get("DurationSeconds") is not None:
        out["duration_seconds"] = data["DurationSeconds"]
    return out
