"""Generated from Smithy shape ``com.amazonaws.cloudwatchlogs#QueryParameter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudwatch_logs.types.query_parameter_default_value
    import capo_cloudwatch_logs.types.query_parameter_description
    import capo_cloudwatch_logs.types.query_parameter_name


class QueryParameter(TypedDict, closed=True):
    name: "capo_cloudwatch_logs.types.query_parameter_name.QueryParameterName"
    """<p>The name of the query parameter. A query parameter name must start with a letter or underscore, and contain only letters, digits, and underscores.</p>"""
    default_value: NotRequired[
        "capo_cloudwatch_logs.types.query_parameter_default_value.QueryParameterDefaultValue"
    ]
    """<p>The default value to use for this query parameter if no value is supplied at execution time.</p>"""
    description: NotRequired[
        "capo_cloudwatch_logs.types.query_parameter_description.QueryParameterDescription"
    ]
    """<p>A description of the query parameter that explains its purpose or expected values.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: QueryParameter) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "default_value" in value:
        out["defaultValue"] = value["default_value"]
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_aws_json_1_1(data: dict) -> QueryParameter:
    out: QueryParameter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("defaultValue") is not None:
        out["default_value"] = data["defaultValue"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
