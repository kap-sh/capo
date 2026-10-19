"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#StartTrainedModelExportJobRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cleanroomsml.errors import DeserializationError

if TYPE_CHECKING:
    import capo_cleanroomsml.types.name_string
    import capo_cleanroomsml.types.resource_description
    import capo_cleanroomsml.types.trained_model_arn
    import capo_cleanroomsml.types.trained_model_export_output_configuration
    import capo_cleanroomsml.types.uuid


class StartTrainedModelExportJobRequest(TypedDict, closed=True):
    name: "capo_cleanroomsml.types.name_string.NameString"
    """<p>The name of the trained model export job.</p>"""
    trained_model_arn: "capo_cleanroomsml.types.trained_model_arn.TrainedModelArn"
    """<p>The Amazon Resource Name (ARN) of the trained model that you want to export.</p>"""
    trained_model_version_identifier: NotRequired["capo_cleanroomsml.types.uuid.UUID"]
    """<p>The version identifier of the trained model to export. This specifies which version of the trained model should be exported to the specified destination.</p>"""
    membership_identifier: "capo_cleanroomsml.types.uuid.UUID"
    """<p>The membership ID of the member that is receiving the exported trained model artifacts.</p>"""
    output_configuration: "capo_cleanroomsml.types.trained_model_export_output_configuration.TrainedModelExportOutputConfiguration"
    """<p>The output configuration information for the trained model export job.</p>"""
    description: NotRequired[
        "capo_cleanroomsml.types.resource_description.ResourceDescription"
    ]
    """<p>The description of the trained model export job.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartTrainedModelExportJobRequest) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    if "trained_model_version_identifier" in value:
        out["trainedModelVersionIdentifier"] = value["trained_model_version_identifier"]
    import capo_cleanroomsml.types.trained_model_export_output_configuration

    out["outputConfiguration"] = (
        capo_cleanroomsml.types.trained_model_export_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    if "description" in value:
        out["description"] = value["description"]
    return out


def deserialize_json(data: dict) -> StartTrainedModelExportJobRequest:
    out: StartTrainedModelExportJobRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("trainedModelVersionIdentifier") is not None:
        out["trained_model_version_identifier"] = data["trainedModelVersionIdentifier"]
    if data.get("outputConfiguration") is not None:
        import capo_cleanroomsml.types.trained_model_export_output_configuration

        out["output_configuration"] = (
            capo_cleanroomsml.types.trained_model_export_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        raise DeserializationError(
            "StartTrainedModelExportJobRequest.output_configuration required"
        )
    if data.get("description") is not None:
        out["description"] = data["description"]
    return out
