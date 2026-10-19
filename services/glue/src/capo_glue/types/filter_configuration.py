"""Generated from Smithy shape ``com.amazonaws.glue#FilterConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_glue.types.between_configuration
    import capo_glue.types.bool
    import capo_glue.types.connection_string_to_string_map
    import capo_glue.types.filter_mode
    import capo_glue.types.filter_string_configuration


class FilterConfiguration(TypedDict, closed=True):
    filter_mode: "capo_glue.types.filter_mode.FilterMode"
    """<p>The strategy for applying filters to requests. Use <code>QUERY_PARAMS</code> to pass filters as individual query parameters, or <code>FILTER_STRING</code> to construct a single filter expression string.</p>"""
    operator_mappings: NotRequired[
        "capo_glue.types.connection_string_to_string_map.ConnectionStringToStringMap"
    ]
    """<p>A map of logical filter operators to their API-specific string representations. Supported operator keys are: <code>EQUAL_TO</code>, <code>NOT_EQUAL_TO</code>, <code>LESS_THAN</code>, <code>GREATER_THAN</code>, <code>LESS_THAN_OR_EQUAL_TO</code>, <code>GREATER_THAN_OR_EQUAL_TO</code>, <code>CONTAINS</code>, <code>BETWEEN</code>, <code>AND</code>, and <code>OR</code>.</p>"""
    date_time_format: NotRequired["str"]
    """<p>The global date and time format for filter expressions. Accepts Java <code>DateTimeFormatter</code> patterns (for example, <code>EEE, d MMM yyyy HH:mm:ss Z</code>), <code>EPOCH_SECONDS</code> for Unix epoch seconds, or <code>EPOCH_MILLIS</code> for Unix epoch milliseconds. If not specified, values are passed as-is in ISO-8601 format.</p>"""
    strip_quotes: NotRequired["capo_glue.types.bool.Bool"]
    """<p>Indicates whether surrounding double quotes should be stripped from filter values before processing.</p>"""
    between_configuration: NotRequired[
        "capo_glue.types.between_configuration.BetweenConfiguration"
    ]
    """<p>Configuration for handling BETWEEN range filter operations.</p>"""
    filter_string_configuration: NotRequired[
        "capo_glue.types.filter_string_configuration.FilterStringConfiguration"
    ]
    """<p>Configuration for constructing filter expressions when <code>FilterMode</code> is set to <code>FILTER_STRING</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: FilterConfiguration) -> dict:
    out: dict = {}
    import capo_glue.types.filter_mode

    out["FilterMode"] = capo_glue.types.filter_mode.serialize_aws_json_1_1(
        value["filter_mode"]
    )
    if "operator_mappings" in value:
        import capo_glue.types.connection_string_to_string_map

        out["OperatorMappings"] = (
            capo_glue.types.connection_string_to_string_map.serialize_aws_json_1_1(
                value["operator_mappings"]
            )
        )
    if "date_time_format" in value:
        out["DateTimeFormat"] = value["date_time_format"]
    if "strip_quotes" in value:
        out["StripQuotes"] = value["strip_quotes"]
    if "between_configuration" in value:
        import capo_glue.types.between_configuration

        out["BetweenConfiguration"] = (
            capo_glue.types.between_configuration.serialize_aws_json_1_1(
                value["between_configuration"]
            )
        )
    if "filter_string_configuration" in value:
        import capo_glue.types.filter_string_configuration

        out["FilterStringConfiguration"] = (
            capo_glue.types.filter_string_configuration.serialize_aws_json_1_1(
                value["filter_string_configuration"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> FilterConfiguration:
    out: FilterConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("FilterMode") is not None:
        import capo_glue.types.filter_mode

        out["filter_mode"] = capo_glue.types.filter_mode.deserialize_aws_json_1_1(
            data["FilterMode"]
        )
    else:
        import typing

        out["filter_mode"] = typing.cast("capo_glue.types.filter_mode.FilterMode", "")
    if data.get("OperatorMappings") is not None:
        import capo_glue.types.connection_string_to_string_map

        out["operator_mappings"] = (
            capo_glue.types.connection_string_to_string_map.deserialize_aws_json_1_1(
                data["OperatorMappings"]
            )
        )
    if data.get("DateTimeFormat") is not None:
        out["date_time_format"] = data["DateTimeFormat"]
    if data.get("StripQuotes") is not None:
        out["strip_quotes"] = data["StripQuotes"]
    if data.get("BetweenConfiguration") is not None:
        import capo_glue.types.between_configuration

        out["between_configuration"] = (
            capo_glue.types.between_configuration.deserialize_aws_json_1_1(
                data["BetweenConfiguration"]
            )
        )
    if data.get("FilterStringConfiguration") is not None:
        import capo_glue.types.filter_string_configuration

        out["filter_string_configuration"] = (
            capo_glue.types.filter_string_configuration.deserialize_aws_json_1_1(
                data["FilterStringConfiguration"]
            )
        )
    return out
