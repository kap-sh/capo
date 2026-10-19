"""Generated from Smithy shape ``com.amazonaws.configservice#PutConfigurationAggregatorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.account_aggregation_source_list
    import capo_config_service.types.aggregator_filters
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.organization_aggregation_source
    import capo_config_service.types.tags_list


class PutConfigurationAggregatorRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    account_aggregation_sources: NotRequired[
        "capo_config_service.types.account_aggregation_source_list.AccountAggregationSourceList"
    ]
    """<p>A list of AccountAggregationSource object. </p>"""
    organization_aggregation_source: NotRequired[
        "capo_config_service.types.organization_aggregation_source.OrganizationAggregationSource"
    ]
    """<p>An OrganizationAggregationSource object.</p>"""
    tags: NotRequired["capo_config_service.types.tags_list.TagsList"]
    """<p>An array of tag object.</p>"""
    aggregator_filters: NotRequired[
        "capo_config_service.types.aggregator_filters.AggregatorFilters"
    ]
    """<p>An object to filter configuration recorders in an aggregator. Either <code>ResourceType</code> or <code>ServicePrincipal</code> is required.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: PutConfigurationAggregatorRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    if "account_aggregation_sources" in value:
        import capo_config_service.types.account_aggregation_source_list

        out["AccountAggregationSources"] = (
            capo_config_service.types.account_aggregation_source_list.serialize_aws_json_1_1(
                value["account_aggregation_sources"]
            )
        )
    if "organization_aggregation_source" in value:
        import capo_config_service.types.organization_aggregation_source

        out["OrganizationAggregationSource"] = (
            capo_config_service.types.organization_aggregation_source.serialize_aws_json_1_1(
                value["organization_aggregation_source"]
            )
        )
    if "tags" in value:
        import capo_config_service.types.tags_list

        out["Tags"] = capo_config_service.types.tags_list.serialize_aws_json_1_1(
            value["tags"]
        )
    if "aggregator_filters" in value:
        import capo_config_service.types.aggregator_filters

        out["AggregatorFilters"] = (
            capo_config_service.types.aggregator_filters.serialize_aws_json_1_1(
                value["aggregator_filters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> PutConfigurationAggregatorRequest:
    out: PutConfigurationAggregatorRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        out["configuration_aggregator_name"] = ""
    if data.get("AccountAggregationSources") is not None:
        import capo_config_service.types.account_aggregation_source_list

        out["account_aggregation_sources"] = (
            capo_config_service.types.account_aggregation_source_list.deserialize_aws_json_1_1(
                data["AccountAggregationSources"]
            )
        )
    if data.get("OrganizationAggregationSource") is not None:
        import capo_config_service.types.organization_aggregation_source

        out["organization_aggregation_source"] = (
            capo_config_service.types.organization_aggregation_source.deserialize_aws_json_1_1(
                data["OrganizationAggregationSource"]
            )
        )
    if data.get("Tags") is not None:
        import capo_config_service.types.tags_list

        out["tags"] = capo_config_service.types.tags_list.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("AggregatorFilters") is not None:
        import capo_config_service.types.aggregator_filters

        out["aggregator_filters"] = (
            capo_config_service.types.aggregator_filters.deserialize_aws_json_1_1(
                data["AggregatorFilters"]
            )
        )
    return out
