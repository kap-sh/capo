"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateStateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.description
    import capo_iotfleetwise.types.resource_name
    import capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list
    import capo_iotfleetwise.types.state_template_properties
    import capo_iotfleetwise.types.tag_list


class CreateStateTemplateRequest(TypedDict, closed=True):
    name: "capo_iotfleetwise.types.resource_name.resourceName"
    """<p>The name of the state template.</p>"""
    description: NotRequired["capo_iotfleetwise.types.description.description"]
    """<p>A brief description of the state template.</p>"""
    signal_catalog_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The ARN of the signal catalog associated with the state template.</p>"""
    state_template_properties: (
        "capo_iotfleetwise.types.state_template_properties.StateTemplateProperties"
    )
    """<p>A list of signals from which data is collected. The state template properties contain the fully qualified names of the signals.</p>"""
    data_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.state_template_data_extra_dimension_node_path_list.StateTemplateDataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with the payload published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will enrich the protobuf encoded payload with those attributes in the <code>extraDimensions</code> field.</p>"""
    metadata_extra_dimensions: NotRequired[
        "capo_iotfleetwise.types.state_template_metadata_extra_dimension_node_path_list.StateTemplateMetadataExtraDimensionNodePathList"
    ]
    """<p>A list of vehicle attributes to associate with user properties of the messages published on the state template's MQTT topic. (See <a href="https://docs.aws.amazon.com/iot-fleetwise/latest/developerguide/process-visualize-data.html#process-last-known-state-vehicle-data"> Processing last known state vehicle data using MQTT messaging</a>). For example, if you add <code>Vehicle.Attributes.Make</code> and <code>Vehicle.Attributes.Model</code> attributes, Amazon Web Services IoT FleetWise will include these attributes as User Properties with the MQTT message.</p> <p>Default: An empty array</p>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata that can be used to manage the state template.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateStateTemplateRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "description" in value:
        out["description"] = value["description"]
    out["signalCatalogArn"] = value["signal_catalog_arn"]
    import capo_iotfleetwise.types.state_template_properties

    out["stateTemplateProperties"] = (
        capo_iotfleetwise.types.state_template_properties.serialize_aws_json_1_0(
            value["state_template_properties"]
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
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateStateTemplateRequest:
    out: CreateStateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        raise DeserializationError("CreateStateTemplateRequest.name required")
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("signalCatalogArn") is not None:
        out["signal_catalog_arn"] = data["signalCatalogArn"]
    else:
        raise DeserializationError(
            "CreateStateTemplateRequest.signal_catalog_arn required"
        )
    if data.get("stateTemplateProperties") is not None:
        import capo_iotfleetwise.types.state_template_properties

        out["state_template_properties"] = (
            capo_iotfleetwise.types.state_template_properties.deserialize_aws_json_1_0(
                data["stateTemplateProperties"]
            )
        )
    else:
        raise DeserializationError(
            "CreateStateTemplateRequest.state_template_properties required"
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
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    return out
