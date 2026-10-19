"""Generated from Smithy shape ``com.amazonaws.pi#ListAvailableResourceDimensionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pi.types.authorized_actions_list
    import capo_pi.types.dimensions_metric_list
    import capo_pi.types.identifier_string
    import capo_pi.types.max_results
    import capo_pi.types.next_token
    import capo_pi.types.service_type


class ListAvailableResourceDimensionsRequest(TypedDict, closed=True):
    service_type: "capo_pi.types.service_type.ServiceType"
    """<p>The Amazon Web Services service for which Performance Insights returns metrics.</p>"""
    identifier: "capo_pi.types.identifier_string.IdentifierString"
    """<p>An immutable identifier for a data source that is unique within an Amazon Web Services Region. Performance Insights gathers metrics from this data source. To use an Amazon RDS DB instance as a data source, specify its <code>DbiResourceId</code> value. For example, specify <code>db-ABCDEFGHIJKLMNOPQRSTU1VWZ</code>. </p>"""
    metrics: "capo_pi.types.dimensions_metric_list.DimensionsMetricList"
    """<p>The types of metrics for which to retrieve dimensions. Valid values include <code>db.load</code>.</p>"""
    max_results: NotRequired["capo_pi.types.max_results.MaxResults"]
    """<p>The maximum number of items to return in the response. If more items exist than the specified <code>MaxRecords</code> value, a pagination token is included in the response so that the remaining results can be retrieved.</p>"""
    next_token: NotRequired["capo_pi.types.next_token.NextToken"]
    """<p>An optional pagination token provided by a previous request. If this parameter is specified, the response includes only records beyond the token, up to the value specified by <code>MaxRecords</code>. </p>"""
    authorized_actions: NotRequired[
        "capo_pi.types.authorized_actions_list.AuthorizedActionsList"
    ]
    """<p>The actions to discover the dimensions you are authorized to access. If you specify multiple actions, then the response will contain the dimensions common for all the actions.</p> <p>When you don't specify this request parameter or provide an empty list, the response contains all the available dimensions for the target database engine whether or not you are authorized to access them.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ListAvailableResourceDimensionsRequest) -> dict:
    out: dict = {}
    import capo_pi.types.service_type

    out["ServiceType"] = capo_pi.types.service_type.serialize_aws_json_1_1(
        value["service_type"]
    )
    out["Identifier"] = value["identifier"]
    import capo_pi.types.dimensions_metric_list

    out["Metrics"] = capo_pi.types.dimensions_metric_list.serialize_aws_json_1_1(
        value["metrics"]
    )
    if "max_results" in value:
        out["MaxResults"] = value["max_results"]
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "authorized_actions" in value:
        import capo_pi.types.authorized_actions_list

        out["AuthorizedActions"] = (
            capo_pi.types.authorized_actions_list.serialize_aws_json_1_1(
                value["authorized_actions"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ListAvailableResourceDimensionsRequest:
    out: ListAvailableResourceDimensionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ServiceType") is not None:
        import capo_pi.types.service_type

        out["service_type"] = capo_pi.types.service_type.deserialize_aws_json_1_1(
            data["ServiceType"]
        )
    else:
        import typing

        out["service_type"] = typing.cast("capo_pi.types.service_type.ServiceType", "")
    if data.get("Identifier") is not None:
        out["identifier"] = data["Identifier"]
    else:
        out["identifier"] = ""
    if data.get("Metrics") is not None:
        import capo_pi.types.dimensions_metric_list

        out["metrics"] = capo_pi.types.dimensions_metric_list.deserialize_aws_json_1_1(
            data["Metrics"]
        )
    else:
        out["metrics"] = []
    if data.get("MaxResults") is not None:
        out["max_results"] = data["MaxResults"]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("AuthorizedActions") is not None:
        import capo_pi.types.authorized_actions_list

        out["authorized_actions"] = (
            capo_pi.types.authorized_actions_list.deserialize_aws_json_1_1(
                data["AuthorizedActions"]
            )
        )
    return out
