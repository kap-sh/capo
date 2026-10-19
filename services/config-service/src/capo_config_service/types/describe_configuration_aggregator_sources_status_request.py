"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationAggregatorSourcesStatusRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.aggregated_source_status_type_list
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.limit
    import capo_config_service.types.string


class DescribeConfigurationAggregatorSourcesStatusRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    update_status: NotRequired[
        "capo_config_service.types.aggregated_source_status_type_list.AggregatedSourceStatusTypeList"
    ]
    """<p>Filters the status type.</p> <ul> <li> <p>Valid value FAILED indicates errors while moving data.</p> </li> <li> <p>Valid value SUCCEEDED indicates the data was successfully moved.</p> </li> <li> <p>Valid value OUTDATED indicates the data is not the most recent.</p> </li> </ul>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of AggregatorSourceStatus returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeConfigurationAggregatorSourcesStatusRequest,
) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "update_status" in value:
        import capo_config_service.types.aggregated_source_status_type_list

        out["UpdateStatus"] = (
            capo_config_service.types.aggregated_source_status_type_list.serialize_aws_json_1_1(
                value["update_status"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeConfigurationAggregatorSourcesStatusRequest:
    out: DescribeConfigurationAggregatorSourcesStatusRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        raise DeserializationError(
            "DescribeConfigurationAggregatorSourcesStatusRequest.configuration_aggregator_name required"
        )
    if data.get("UpdateStatus") is not None:
        import capo_config_service.types.aggregated_source_status_type_list

        out["update_status"] = (
            capo_config_service.types.aggregated_source_status_type_list.deserialize_aws_json_1_1(
                data["UpdateStatus"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
