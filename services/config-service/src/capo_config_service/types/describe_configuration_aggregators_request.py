"""Generated from Smithy shape ``com.amazonaws.configservice#DescribeConfigurationAggregatorsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator_name_list
    import capo_config_service.types.limit
    import capo_config_service.types.string


class DescribeConfigurationAggregatorsRequest(TypedDict, closed=True):
    configuration_aggregator_names: NotRequired[
        "capo_config_service.types.configuration_aggregator_name_list.ConfigurationAggregatorNameList"
    ]
    """<p>The name of the configuration aggregators.</p>"""
    next_token: NotRequired["capo_config_service.types.string.String"]
    """<p>The <code>nextToken</code> string returned on a previous page that you use to get the next page of results in a paginated response.</p>"""
    limit: NotRequired["capo_config_service.types.limit.Limit"]
    """<p>The maximum number of configuration aggregators returned on each page. The default is maximum. If you specify 0, Config uses the default.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeConfigurationAggregatorsRequest) -> dict:
    out: dict = {}
    if "configuration_aggregator_names" in value:
        import capo_config_service.types.configuration_aggregator_name_list

        out["ConfigurationAggregatorNames"] = (
            capo_config_service.types.configuration_aggregator_name_list.serialize_aws_json_1_1(
                value["configuration_aggregator_names"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "limit" in value:
        out["Limit"] = value["limit"]
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeConfigurationAggregatorsRequest:
    out: DescribeConfigurationAggregatorsRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorNames") is not None:
        import capo_config_service.types.configuration_aggregator_name_list

        out["configuration_aggregator_names"] = (
            capo_config_service.types.configuration_aggregator_name_list.deserialize_aws_json_1_1(
                data["ConfigurationAggregatorNames"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Limit") is not None:
        out["limit"] = data["Limit"]
    return out
