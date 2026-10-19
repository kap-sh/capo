"""Generated from Smithy shape ``com.amazonaws.lambda#FunctionVersionsByCapacityProviderListItem``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.name_spaced_function_arn
    import capo_lambda.types.state


class FunctionVersionsByCapacityProviderListItem(TypedDict, closed=True):
    function_arn: "capo_lambda.types.name_spaced_function_arn.NameSpacedFunctionArn"
    """<p>The Amazon Resource Name (ARN) of the function version.</p>"""
    state: "capo_lambda.types.state.State"
    """<p>The current state of the function version.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FunctionVersionsByCapacityProviderListItem) -> dict:
    out: dict = {}
    out["FunctionArn"] = value["function_arn"]
    import capo_lambda.types.state

    out["State"] = capo_lambda.types.state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> FunctionVersionsByCapacityProviderListItem:
    out: FunctionVersionsByCapacityProviderListItem = {}  # type: ignore[typeddict-item]
    if data.get("FunctionArn") is not None:
        out["function_arn"] = data["FunctionArn"]
    else:
        out["function_arn"] = ""
    if data.get("State") is not None:
        import capo_lambda.types.state

        out["state"] = capo_lambda.types.state.deserialize_json(data["State"])
    else:
        import typing

        out["state"] = typing.cast("capo_lambda.types.state.State", "")
    return out
