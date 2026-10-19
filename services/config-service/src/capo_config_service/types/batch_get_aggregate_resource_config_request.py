"""Generated from Smithy shape ``com.amazonaws.configservice#BatchGetAggregateResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.configuration_aggregator_name
    import capo_config_service.types.resource_identifiers_list


class BatchGetAggregateResourceConfigRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    resource_identifiers: (
        "capo_config_service.types.resource_identifiers_list.ResourceIdentifiersList"
    )
    """<p>A list of aggregate ResourceIdentifiers objects. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: BatchGetAggregateResourceConfigRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    import capo_config_service.types.resource_identifiers_list

    out["ResourceIdentifiers"] = (
        capo_config_service.types.resource_identifiers_list.serialize_aws_json_1_1(
            value["resource_identifiers"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> BatchGetAggregateResourceConfigRequest:
    out: BatchGetAggregateResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        out["configuration_aggregator_name"] = ""
    if data.get("ResourceIdentifiers") is not None:
        import capo_config_service.types.resource_identifiers_list

        out["resource_identifiers"] = (
            capo_config_service.types.resource_identifiers_list.deserialize_aws_json_1_1(
                data["ResourceIdentifiers"]
            )
        )
    else:
        out["resource_identifiers"] = []
    return out
