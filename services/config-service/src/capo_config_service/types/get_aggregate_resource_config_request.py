"""Generated from Smithy shape ``com.amazonaws.configservice#GetAggregateResourceConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_config_service.errors import DeserializationError

if TYPE_CHECKING:
    import capo_config_service.types.aggregate_resource_identifier
    import capo_config_service.types.configuration_aggregator_name


class GetAggregateResourceConfigRequest(TypedDict, closed=True):
    configuration_aggregator_name: "capo_config_service.types.configuration_aggregator_name.ConfigurationAggregatorName"
    """<p>The name of the configuration aggregator.</p>"""
    resource_identifier: "capo_config_service.types.aggregate_resource_identifier.AggregateResourceIdentifier"
    """<p>An object that identifies aggregate resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetAggregateResourceConfigRequest) -> dict:
    out: dict = {}
    out["ConfigurationAggregatorName"] = value["configuration_aggregator_name"]
    import capo_config_service.types.aggregate_resource_identifier

    out["ResourceIdentifier"] = (
        capo_config_service.types.aggregate_resource_identifier.serialize_aws_json_1_1(
            value["resource_identifier"]
        )
    )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetAggregateResourceConfigRequest:
    out: GetAggregateResourceConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("ConfigurationAggregatorName") is not None:
        out["configuration_aggregator_name"] = data["ConfigurationAggregatorName"]
    else:
        out["configuration_aggregator_name"] = ""
    if data.get("ResourceIdentifier") is not None:
        import capo_config_service.types.aggregate_resource_identifier

        out["resource_identifier"] = (
            capo_config_service.types.aggregate_resource_identifier.deserialize_aws_json_1_1(
                data["ResourceIdentifier"]
            )
        )
    else:
        raise DeserializationError(
            "GetAggregateResourceConfigRequest.resource_identifier required"
        )
    return out
