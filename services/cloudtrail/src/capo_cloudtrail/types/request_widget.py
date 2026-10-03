"""Generated from Smithy shape ``com.amazonaws.cloudtrail#RequestWidget``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudtrail.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cloudtrail.types.query_parameters
    import capo_cloudtrail.types.query_statement
    import capo_cloudtrail.types.view_properties_map


class RequestWidget(TypedDict, closed=True):
    query_statement: "capo_cloudtrail.types.query_statement.QueryStatement"
    """<p> The query statement for the widget. For custom dashboard widgets, you can query across multiple event data stores as long as all event data stores exist in your account. </p> <note> <p>When a query uses <code>?</code> with <code>eventTime</code>, <code>?</code> must be surrounded by single quotes as follows: <code>'?'</code>.</p> </note>"""
    query_parameters: NotRequired[
        "capo_cloudtrail.types.query_parameters.QueryParameters"
    ]
    """<p> The optional query parameters. The following query parameters are valid: <code>$StartTime$</code>, <code>$EndTime$</code>, and <code>$Period$</code>. </p>"""
    view_properties: "capo_cloudtrail.types.view_properties_map.ViewPropertiesMap"
    """<p> The view properties for the widget. For more information about view properties, see <a href="https://docs.aws.amazon.com/awscloudtrail/latest/userguide/lake-widget-properties.html"> View properties for widgets </a> in the <i>CloudTrail User Guide</i>. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RequestWidget) -> dict:
    out: dict = {}
    out["QueryStatement"] = value["query_statement"]
    if "query_parameters" in value:
        import capo_cloudtrail.types.query_parameters

        out["QueryParameters"] = (
            capo_cloudtrail.types.query_parameters.serialize_aws_json_1_1(
                value["query_parameters"]
            )
        )
    import capo_cloudtrail.types.view_properties_map

    out["ViewProperties"] = (
        capo_cloudtrail.types.view_properties_map.serialize_aws_json_1_1(
            value["view_properties"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> RequestWidget:
    out: RequestWidget = {}  # type: ignore[typeddict-item]
    if data.get("QueryStatement") is not None:
        out["query_statement"] = data["QueryStatement"]
    else:
        raise DeserializationError("RequestWidget.query_statement required")
    if data.get("QueryParameters") is not None:
        import capo_cloudtrail.types.query_parameters

        out["query_parameters"] = (
            capo_cloudtrail.types.query_parameters.deserialize_aws_json_1_1(
                data["QueryParameters"]
            )
        )
    if data.get("ViewProperties") is not None:
        import capo_cloudtrail.types.view_properties_map

        out["view_properties"] = (
            capo_cloudtrail.types.view_properties_map.deserialize_aws_json_1_1(
                data["ViewProperties"]
            )
        )
    else:
        raise DeserializationError("RequestWidget.view_properties required")
    return out
