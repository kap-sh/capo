"""Generated from Smithy shape ``com.amazonaws.pipes#PipeTargetHttpParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.header_parameters_map
    import capo_pipes.types.path_parameter_list
    import capo_pipes.types.query_string_parameters_map


class PipeTargetHttpParameters(TypedDict, closed=True):
    path_parameter_values: NotRequired[
        "capo_pipes.types.path_parameter_list.PathParameterList"
    ]
    """<p>The path parameter values to be used to populate API Gateway REST API or EventBridge ApiDestination path wildcards ("*").</p>"""
    header_parameters: NotRequired[
        "capo_pipes.types.header_parameters_map.HeaderParametersMap"
    ]
    """<p>The headers that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.</p>"""
    query_string_parameters: NotRequired[
        "capo_pipes.types.query_string_parameters_map.QueryStringParametersMap"
    ]
    """<p>The query string keys/values that need to be sent as part of request invoking the API Gateway REST API or EventBridge ApiDestination.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeTargetHttpParameters) -> dict:
    out: dict = {}
    if "path_parameter_values" in value:
        import capo_pipes.types.path_parameter_list

        out["PathParameterValues"] = (
            capo_pipes.types.path_parameter_list.serialize_json(
                value["path_parameter_values"]
            )
        )
    if "header_parameters" in value:
        import capo_pipes.types.header_parameters_map

        out["HeaderParameters"] = capo_pipes.types.header_parameters_map.serialize_json(
            value["header_parameters"]
        )
    if "query_string_parameters" in value:
        import capo_pipes.types.query_string_parameters_map

        out["QueryStringParameters"] = (
            capo_pipes.types.query_string_parameters_map.serialize_json(
                value["query_string_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeTargetHttpParameters:
    out: PipeTargetHttpParameters = {}  # type: ignore[typeddict-item]
    if data.get("PathParameterValues") is not None:
        import capo_pipes.types.path_parameter_list

        out["path_parameter_values"] = (
            capo_pipes.types.path_parameter_list.deserialize_json(
                data["PathParameterValues"]
            )
        )
    if data.get("HeaderParameters") is not None:
        import capo_pipes.types.header_parameters_map

        out["header_parameters"] = (
            capo_pipes.types.header_parameters_map.deserialize_json(
                data["HeaderParameters"]
            )
        )
    if data.get("QueryStringParameters") is not None:
        import capo_pipes.types.query_string_parameters_map

        out["query_string_parameters"] = (
            capo_pipes.types.query_string_parameters_map.deserialize_json(
                data["QueryStringParameters"]
            )
        )
    return out
