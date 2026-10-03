"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#TelemetryConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.account_identifier
    import capo_observabilityadmin.types.resource_identifier
    import capo_observabilityadmin.types.resource_type
    import capo_observabilityadmin.types.tag_map_output
    import capo_observabilityadmin.types.telemetry_configuration_state
    import capo_observabilityadmin.types.telemetry_source_type


class TelemetryConfiguration(TypedDict, closed=True):
    account_identifier: NotRequired[
        "capo_observabilityadmin.types.account_identifier.AccountIdentifier"
    ]
    """<p> The account ID which contains the resource managed in telemetry configuration. An example of a valid account ID is <code>012345678901</code>. </p>"""
    telemetry_configuration_state: NotRequired[
        "capo_observabilityadmin.types.telemetry_configuration_state.TelemetryConfigurationState"
    ]
    """<p> The configuration state for the resource, for example <code>{ Logs: NotApplicable; Metrics: Enabled; Traces: NotApplicable; }</code>. </p>"""
    resource_type: NotRequired[
        "capo_observabilityadmin.types.resource_type.ResourceType"
    ]
    """<p> The type of resource, for example <code>Amazon Web Services::EC2::Instance</code>, or <code>Amazon Web Services::EKS::Cluster</code>, etc. </p>"""
    resource_identifier: NotRequired[
        "capo_observabilityadmin.types.resource_identifier.ResourceIdentifier"
    ]
    """<p> The identifier of the resource, for example for Amazon VPC, it would be <code>vpc-1a2b3c4d5e6f1a2b3</code>. </p>"""
    resource_tags: NotRequired[
        "capo_observabilityadmin.types.tag_map_output.TagMapOutput"
    ]
    """<p> Tags associated with the resource, for example <code>{ Name: "ExampleInstance", Environment: "Development" }</code>. </p>"""
    last_update_time_stamp: NotRequired["int"]
    """<p> The timestamp of the last change to the telemetry configuration for the resource. For example, <code>1728679196318</code>. </p>"""
    telemetry_source_type: NotRequired[
        "capo_observabilityadmin.types.telemetry_source_type.TelemetrySourceType"
    ]


# --- restJson1 ser/de ---
def serialize_json(value: TelemetryConfiguration) -> dict:
    out: dict = {}
    if "account_identifier" in value:
        out["AccountIdentifier"] = value["account_identifier"]
    if "telemetry_configuration_state" in value:
        import capo_observabilityadmin.types.telemetry_configuration_state

        out["TelemetryConfigurationState"] = (
            capo_observabilityadmin.types.telemetry_configuration_state.serialize_json(
                value["telemetry_configuration_state"]
            )
        )
    if "resource_type" in value:
        import capo_observabilityadmin.types.resource_type

        out["ResourceType"] = (
            capo_observabilityadmin.types.resource_type.serialize_json(
                value["resource_type"]
            )
        )
    if "resource_identifier" in value:
        out["ResourceIdentifier"] = value["resource_identifier"]
    if "resource_tags" in value:
        import capo_observabilityadmin.types.tag_map_output

        out["ResourceTags"] = (
            capo_observabilityadmin.types.tag_map_output.serialize_json(
                value["resource_tags"]
            )
        )
    if "last_update_time_stamp" in value:
        out["LastUpdateTimeStamp"] = value["last_update_time_stamp"]
    if "telemetry_source_type" in value:
        import capo_observabilityadmin.types.telemetry_source_type

        out["TelemetrySourceType"] = (
            capo_observabilityadmin.types.telemetry_source_type.serialize_json(
                value["telemetry_source_type"]
            )
        )
    return out


def deserialize_json(data: dict) -> TelemetryConfiguration:
    out: TelemetryConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("AccountIdentifier") is not None:
        out["account_identifier"] = data["AccountIdentifier"]
    if data.get("TelemetryConfigurationState") is not None:
        import capo_observabilityadmin.types.telemetry_configuration_state

        out["telemetry_configuration_state"] = (
            capo_observabilityadmin.types.telemetry_configuration_state.deserialize_json(
                data["TelemetryConfigurationState"]
            )
        )
    if data.get("ResourceType") is not None:
        import capo_observabilityadmin.types.resource_type

        out["resource_type"] = (
            capo_observabilityadmin.types.resource_type.deserialize_json(
                data["ResourceType"]
            )
        )
    if data.get("ResourceIdentifier") is not None:
        out["resource_identifier"] = data["ResourceIdentifier"]
    if data.get("ResourceTags") is not None:
        import capo_observabilityadmin.types.tag_map_output

        out["resource_tags"] = (
            capo_observabilityadmin.types.tag_map_output.deserialize_json(
                data["ResourceTags"]
            )
        )
    if data.get("LastUpdateTimeStamp") is not None:
        out["last_update_time_stamp"] = data["LastUpdateTimeStamp"]
    if data.get("TelemetrySourceType") is not None:
        import capo_observabilityadmin.types.telemetry_source_type

        out["telemetry_source_type"] = (
            capo_observabilityadmin.types.telemetry_source_type.deserialize_json(
                data["TelemetrySourceType"]
            )
        )
    return out
