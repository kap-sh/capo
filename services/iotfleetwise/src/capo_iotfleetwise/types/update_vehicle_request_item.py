"""Generated from Smithy shape ``com.amazonaws.iotfleetwise#UpdateVehicleRequestItem``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_iotfleetwise.errors import DeserializationError

if TYPE_CHECKING:
    import capo_iotfleetwise.types.arn
    import capo_iotfleetwise.types.attributes_map
    import capo_iotfleetwise.types.state_template_association_identifiers
    import capo_iotfleetwise.types.state_template_associations
    import capo_iotfleetwise.types.update_mode
    import capo_iotfleetwise.types.vehicle_name


class UpdateVehicleRequestItem(TypedDict, closed=True):
    vehicle_name: "capo_iotfleetwise.types.vehicle_name.vehicleName"
    """<p>The unique ID of the vehicle to update.</p>"""
    model_manifest_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the vehicle model (model manifest) associated with the vehicle to update.</p>"""
    decoder_manifest_arn: NotRequired["capo_iotfleetwise.types.arn.arn"]
    """<p>The ARN of the signal decoder manifest associated with the vehicle to update.</p>"""
    attributes: NotRequired["capo_iotfleetwise.types.attributes_map.attributesMap"]
    """<p>Static information about a vehicle in a key-value pair. For example:</p> <p> <code>"engineType"</code> : <code>"1.3 L R2"</code> </p>"""
    attribute_update_mode: NotRequired["capo_iotfleetwise.types.update_mode.UpdateMode"]
    """<p>The method the specified attributes will update the existing attributes on the vehicle. Use<code>Overwite</code> to replace the vehicle attributes with the specified attributes. Or use <code>Merge</code> to combine all attributes.</p> <p>This is required if attributes are present in the input.</p>"""
    state_templates_to_add: NotRequired[
        "capo_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>Associate additional state templates to track the state of the vehicle. State templates determine which signal updates the vehicle sends to the cloud.</p>"""
    state_templates_to_remove: NotRequired[
        "capo_iotfleetwise.types.state_template_association_identifiers.StateTemplateAssociationIdentifiers"
    ]
    """<p>Remove existing state template associations from the vehicle.</p>"""
    state_templates_to_update: NotRequired[
        "capo_iotfleetwise.types.state_template_associations.StateTemplateAssociations"
    ]
    """<p>Change the <code>stateTemplateUpdateStrategy</code> of state templates already associated with the vehicle.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: UpdateVehicleRequestItem) -> dict:
    out: dict = {}
    out["vehicleName"] = value["vehicle_name"]
    if "model_manifest_arn" in value:
        out["modelManifestArn"] = value["model_manifest_arn"]
    if "decoder_manifest_arn" in value:
        out["decoderManifestArn"] = value["decoder_manifest_arn"]
    if "attributes" in value:
        import capo_iotfleetwise.types.attributes_map

        out["attributes"] = (
            capo_iotfleetwise.types.attributes_map.serialize_aws_json_1_0(
                value["attributes"]
            )
        )
    if "attribute_update_mode" in value:
        import capo_iotfleetwise.types.update_mode

        out["attributeUpdateMode"] = (
            capo_iotfleetwise.types.update_mode.serialize_aws_json_1_0(
                value["attribute_update_mode"]
            )
        )
    if "state_templates_to_add" in value:
        import capo_iotfleetwise.types.state_template_associations

        out["stateTemplatesToAdd"] = (
            capo_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates_to_add"]
            )
        )
    if "state_templates_to_remove" in value:
        import capo_iotfleetwise.types.state_template_association_identifiers

        out["stateTemplatesToRemove"] = (
            capo_iotfleetwise.types.state_template_association_identifiers.serialize_aws_json_1_0(
                value["state_templates_to_remove"]
            )
        )
    if "state_templates_to_update" in value:
        import capo_iotfleetwise.types.state_template_associations

        out["stateTemplatesToUpdate"] = (
            capo_iotfleetwise.types.state_template_associations.serialize_aws_json_1_0(
                value["state_templates_to_update"]
            )
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> UpdateVehicleRequestItem:
    out: UpdateVehicleRequestItem = {}  # type: ignore[typeddict-item]
    if data.get("vehicleName") is not None:
        out["vehicle_name"] = data["vehicleName"]
    else:
        raise DeserializationError("UpdateVehicleRequestItem.vehicle_name required")
    if data.get("modelManifestArn") is not None:
        out["model_manifest_arn"] = data["modelManifestArn"]
    if data.get("decoderManifestArn") is not None:
        out["decoder_manifest_arn"] = data["decoderManifestArn"]
    if data.get("attributes") is not None:
        import capo_iotfleetwise.types.attributes_map

        out["attributes"] = (
            capo_iotfleetwise.types.attributes_map.deserialize_aws_json_1_0(
                data["attributes"]
            )
        )
    if data.get("attributeUpdateMode") is not None:
        import capo_iotfleetwise.types.update_mode

        out["attribute_update_mode"] = (
            capo_iotfleetwise.types.update_mode.deserialize_aws_json_1_0(
                data["attributeUpdateMode"]
            )
        )
    if data.get("stateTemplatesToAdd") is not None:
        import capo_iotfleetwise.types.state_template_associations

        out["state_templates_to_add"] = (
            capo_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplatesToAdd"]
            )
        )
    if data.get("stateTemplatesToRemove") is not None:
        import capo_iotfleetwise.types.state_template_association_identifiers

        out["state_templates_to_remove"] = (
            capo_iotfleetwise.types.state_template_association_identifiers.deserialize_aws_json_1_0(
                data["stateTemplatesToRemove"]
            )
        )
    if data.get("stateTemplatesToUpdate") is not None:
        import capo_iotfleetwise.types.state_template_associations

        out["state_templates_to_update"] = (
            capo_iotfleetwise.types.state_template_associations.deserialize_aws_json_1_0(
                data["stateTemplatesToUpdate"]
            )
        )
    return out
