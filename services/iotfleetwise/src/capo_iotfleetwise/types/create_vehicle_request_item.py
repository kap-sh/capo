"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#CreateVehicleRequestItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.attributes_map
    import capo_iotfleetwise.types.state_template_associations
    import capo_iotfleetwise.types.tag_list
    import capo_iotfleetwise.types.vehicle_association_behavior
    import capo_iotfleetwise.types.vehicle_name


class CreateVehicleRequestItem(TypedDict, closed=True):
    vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName"
    """<p>The unique ID of the vehicle to create.</p>"""
    model_manifest_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The ARN of the vehicle model (model manifest) to create the vehicle from.</p>"""
    decoder_manifest_arn: "capo_iotfleetwise.types.arn.arn"
    """<p>The Amazon Resource Name (ARN) of a decoder manifest associated with the vehicle to create. </p>"""
    attributes: NotRequired["capo_iotfleetwise.types.attributes_map.attributesMap"]
    """<p>Static information about a vehicle in a key-value pair. For example: <code>"engine Type"</code> : <code>"v6"</code> </p>"""
    association_behavior: NotRequired[
        "capo_iotfleetwise.types.vehicle_association_behavior.VehicleAssociationBehavior"
    ]
    """<p>An option to create a new Amazon Web Services IoT thing when creating a vehicle, or to validate an existing thing as a vehicle.</p>"""
    tags: NotRequired["capo_iotfleetwise.types.tag_list.TagList"]
    """<p>Metadata which can be used to manage the vehicle.</p>"""
    state_templates: NotRequired[
        "capo_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>Associate state templates to track the state of the vehicle. State templates determine which signal updates the vehicle sends to the cloud.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: CreateVehicleRequestItem) -> dict:
    out: dict = {}
    out["vehicleName"] = value["vehicle_name"]
    out["modelManifestArn"] = value["model_manifest_arn"]
    out["decoderManifestArn"] = value["decoder_manifest_arn"]
    if "attributes" in value:
        import capo_iotfleetwise.types.attributes_map

        out["attributes"] = (
            capo_iotfleetwise.types.attributes_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "association_behavior" in value:
        import capo_iotfleetwise.types.vehicle_association_behavior

        out["associationBehavior"] = (
            capo_iotfleetwise.types.vehicle_association_behavior.serialize_aws_json_1_0(
                value["association_behavior"]
            )
        )
    if "tags" in value:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.serialize_aws_json_1_0(
            value["tags"]
        )
    if "state_templates" in value:
        import capo_iotfleetwise.types.state_template_associations

        out["stateTemplates"] = (
            capo_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> CreateVehicleRequestItem:
    out: CreateVehicleRequestItem = {}  # type: ignore[typeddict-item]
    if data.get("vehicleName") is not None:
        out["vehicle_name"] = data["vehicleName"]
    else:
        raise DeserializationError("CreateVehicleRequestItem.vehicle_name required")
    if data.get("modelManifestArn") is not None:
        out["model_manifest_arn"] = data["modelManifestArn"]
    else:
        raise DeserializationError(
            "CreateVehicleRequestItem.model_manifest_arn required"
        )
    if data.get("decoderManifestArn") is not None:
        out["decoder_manifest_arn"] = data["decoderManifestArn"]
    else:
        raise DeserializationError(
            "CreateVehicleRequestItem.decoder_manifest_arn required"
        )
    if data.get("attributes") is not None:
        import capo_iotfleetwise.types.attributes_map

        out["attributes"] = (
            capo_iotfleetwise.types.attributes_map.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    if data.get("associationBehavior") is not None:
        import capo_iotfleetwise.types.vehicle_association_behavior

        out["association_behavior"] = (
            capo_iotfleetwise.types.vehicle_association_behavior.deserialize_aws_json_1_0(
                data["associationBehavior"]
            )
        )
    if data.get("tags") is not None:
        import capo_iotfleetwise.types.tag_list

        out["tags"] = capo_iotfleetwise.types.tag_list.deserialize_aws_json_1_0(
            data["tags"]
        )
    if data.get("stateTemplates") is not None:
        import capo_iotfleetwise.types.state_template_associations

        out["state_templates"] = (
            capo_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplates"]
            )
        )
    return out
