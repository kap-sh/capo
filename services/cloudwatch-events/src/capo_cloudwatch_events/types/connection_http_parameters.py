"""Generated from Smithy shape ``com.amazonaws.cloudwatchevents#ConnectionHttpParameters``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_events.types.connection_body_parameters_list
    import capo_cloudwatch_events.types.connection_header_parameters_list
    import capo_cloudwatch_events.types.connection_query_string_parameters_list


class ConnectionHttpParameters(TypedDict, closed=True):
    header_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_header_parameters_list.ConnectionHeaderParametersList"
    ]
    """<p>Contains additional header parameters for the connection.</p>"""
    query_string_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_query_string_parameters_list.ConnectionQueryStringParametersList"
    ]
    """<p>Contains additional query string parameters for the connection.</p>"""
    body_parameters: NotRequired[
        "capo_cloudwatch_events.types.connection_body_parameters_list.ConnectionBodyParametersList"
    ]
    """<p>Contains additional body string parameters for the connection.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConnectionHttpParameters) -> dict:
    out: dict = {}
    if "header_parameters" in value:
        import capo_cloudwatch_events.types.connection_header_parameters_list

        out["HeaderParameters"] = (
            capo_cloudwatch_events.types.connection_header_parameters_list.serialize_aws_json_1_1(
                value["header_parameters"]
            )
        )
    if "query_string_parameters" in value:
        import capo_cloudwatch_events.types.connection_query_string_parameters_list

        out["QueryStringParameters"] = (
            capo_cloudwatch_events.types.connection_query_string_parameters_list.serialize_aws_json_1_1(
                value["query_string_parameters"]
            )
        )
    if "body_parameters" in value:
        import capo_cloudwatch_events.types.connection_body_parameters_list

        out["BodyParameters"] = (
            capo_cloudwatch_events.types.connection_body_parameters_list.serialize_aws_json_1_1(
                value["body_parameters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConnectionHttpParameters:
    out: ConnectionHttpParameters = {}  # type: ignore[typeddict-item]
    if data.get("HeaderParameters") is not None:
        import capo_cloudwatch_events.types.connection_header_parameters_list

        out["header_parameters"] = (
            capo_cloudwatch_events.types.connection_header_parameters_list.deserialize_aws_json_1_1(
                data["HeaderParameters"]
            )
        )
    if data.get("QueryStringParameters") is not None:
        import capo_cloudwatch_events.types.connection_query_string_parameters_list

        out["query_string_parameters"] = (
            capo_cloudwatch_events.types.connection_query_string_parameters_list.deserialize_aws_json_1_1(
                data["QueryStringParameters"]
            )
        )
    if data.get("BodyParameters") is not None:
        import capo_cloudwatch_events.types.connection_body_parameters_list

        out["body_parameters"] = (
            capo_cloudwatch_events.types.connection_body_parameters_list.deserialize_aws_json_1_1(
                data["BodyParameters"]
            )
        )
    return out


def redact_sensitive(value: ConnectionHttpParameters) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "header_parameters" in value:
        import capo_cloudwatch_events.types.connection_header_parameters_list

        out["header_parameters"] = (
            capo_cloudwatch_events.types.connection_header_parameters_list.redact_sensitive(
                value["header_parameters"]
            )
        )
    if "query_string_parameters" in value:
        import capo_cloudwatch_events.types.connection_query_string_parameters_list

        out["query_string_parameters"] = (
            capo_cloudwatch_events.types.connection_query_string_parameters_list.redact_sensitive(
                value["query_string_parameters"]
            )
        )
    if "body_parameters" in value:
        import capo_cloudwatch_events.types.connection_body_parameters_list

        out["body_parameters"] = (
            capo_cloudwatch_events.types.connection_body_parameters_list.redact_sensitive(
                value["body_parameters"]
            )
        )
    return out
