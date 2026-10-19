"""Generated from Smithy shape ``com.amazonaws.lambda#ListFunctionUrlConfigsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.function_url_config_list
    import capo_lambda.types.string


class ListFunctionUrlConfigsResponse(TypedDict, closed=True):
    function_url_configs: (
        "capo_lambda.types.function_url_config_list.FunctionUrlConfigList"
    )
    """<p>A list of function URL configurations.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListFunctionUrlConfigsResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.function_url_config_list

    out["FunctionUrlConfigs"] = (
        capo_lambda.types.function_url_config_list.serialize_json(
            value["function_url_configs"]
        )
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListFunctionUrlConfigsResponse:
    out: ListFunctionUrlConfigsResponse = {}  # type: ignore[typeddict-item]
    if data.get("FunctionUrlConfigs") is not None:
        import capo_lambda.types.function_url_config_list

        out["function_url_configs"] = (
            capo_lambda.types.function_url_config_list.deserialize_json(
                data["FunctionUrlConfigs"]
            )
        )
    else:
        out["function_url_configs"] = []
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
