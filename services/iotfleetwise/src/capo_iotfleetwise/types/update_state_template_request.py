"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateStateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.resource_identifier
    import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_properties


class UpdateStateTemplateRequest(TypedDict, closed=True):
    identifier: "capo_iotfleetwise.types.resource_identifier.ResourceIdentifier"
    """<p>The unique ID of the state template.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the state template.</p>"""
    state_template_properties_to_add: NotRequired[
        "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    ]
    """<p>Add signals from which data is collected as part of the state template.</p>"""
    state_template_properties_to_remove: NotRequired[
        "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    ]
    """<p>Remove signals from which data is collected as part of the state template.</p>"""
    data_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p> <p>Default: An empty array</p>"""
    metadata_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateStateTemplateRequest) -> dict:
    out: dict = {}
    out["identifier"] = value["identifier"]
    if "description" in value:
        out["description"] = value["description"]
    if "state_template_properties_to_add" in value:
        import capo_iotfleetwise.types.state_template_properties

        out["stateTemplatePropertiesToAdd"] = (
            capo_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
                value["state_template_properties_to_add"]
            )
        )
    if "state_template_properties_to_remove" in value:
        import capo_iotfleetwise.types.state_template_properties

        out["stateTemplatePropertiesToRemove"] = (
            capo_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
                value["state_template_properties_to_remove"]
            )
        )
    if "data_extra_dimensions" in value:
        import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list

        out["dataExtraDimensions"] = (
            capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["data_extra_dimensions"]
            )
        )
    if "metadata_extra_dimensions" in value:
        import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list

        out["metadataExtraDimensions"] = (
            capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.serialize_aws_json_1_0(
                value["metadata_extra_dimensions"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateStateTemplateRequest:
    out: UpdateStateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("identifier") is not None:
        out["identifier"] = data["identifier"]
    else:
        raise DeserializationError("UpdateStateTemplateRequest.identifier required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("stateTemplatePropertiesToAdd") is not None:
        import capo_iotfleetwise.types.state_template_properties

        out["state_template_properties_to_add"] = (
            capo_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplatePropertiesToAdd"]
            )
        )
    if data.get("stateTemplatePropertiesToRemove") is not None:
        import capo_iotfleetwise.types.state_template_properties

        out["state_template_properties_to_remove"] = (
            capo_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplatePropertiesToRemove"]
            )
        )
    if data.get("dataExtraDimensions") is not None:
        import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list

        out["data_extra_dimensions"] = (
            capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["dataExtraDimensions"]
            )
        )
    if data.get("metadataExtraDimensions") is not None:
        import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list

        out["metadata_extra_dimensions"] = (
            capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.deserialize_aws_json_1_0(
                data["metadataExtraDimensions"]
            )
        )
    return out
