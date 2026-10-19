"""Generated from Smithy shape ``com.amazonaws.rekognition#UpdateStreamProcessorRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_rekognition.types.regions_of_interest
    import capo_rekognition.types.stream_processor_data_sharing_preference
    import capo_rekognition.types.stream_processor_name
    import capo_rekognition.types.stream_processor_parameters_to_delete
    import capo_rekognition.types.stream_processor_settings_for_update


class UpdateStreamProcessorRequest(TypedDict, closed=True):
    name: "capo_rekognition.types.stream_processor_name.StreamProcessorName"
    """<p> Name of the stream processor that you want to update. </p>"""
    settings_for_update: NotRequired[
        "capo_rekognition.types.stream_processor_settings_for_update.StreamProcessorSettingsForUpdate"
    ]
    """<p> The stream processor settings that you want to update. Label detection settings can be updated to detect different labels with a different minimum confidence. </p>"""
    regions_of_interest_for_update: NotRequired[
        "capo_rekognition.types.regions_of_interest.RegionsOfInterest"
    ]
    """<p> Specifies locations in the frames where Amazon Rekognition checks for objects or people. This is an optional parameter for label detection stream processors. </p>"""
    data_sharing_preference_for_update: NotRequired[
        "capo_rekognition.types.stream_processor_data_sharing_preference.StreamProcessorDataSharingPreference"
    ]
    """<p> Shows whether you are sharing data with Rekognition to improve model performance. You can choose this option at the account level or on a per-stream basis. Note that if you opt out at the account level this setting is ignored on individual streams. </p>"""
    parameters_to_delete: NotRequired[
        "capo_rekognition.types.stream_processor_parameters_to_delete.StreamProcessorParametersToDelete"
    ]
    """<p> A list of parameters you want to delete from the stream processor. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateStreamProcessorRequest) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    if "settings_for_update" in value:
        import capo_rekognition.types.stream_processor_settings_for_update

        out["SettingsForUpdate"] = (
            capo_rekognition.types.stream_processor_settings_for_update.serialize_aws_json_1_1(
                value["settings_for_update"]
            )
        )
    if "regions_of_interest_for_update" in value:
        import capo_rekognition.types.regions_of_interest

        out["RegionsOfInterestForUpdate"] = (
            capo_rekognition.types.regions_of_interest.serialize_aws_json_1_1(
                value["regions_of_interest_for_update"]
            )
        )
    if "data_sharing_preference_for_update" in value:
        import capo_rekognition.types.stream_processor_data_sharing_preference

        out["DataSharingPreferenceForUpdate"] = (
            capo_rekognition.types.stream_processor_data_sharing_preference.serialize_aws_json_1_1(
                value["data_sharing_preference_for_update"]
            )
        )
    if "parameters_to_delete" in value:
        import capo_rekognition.types.stream_processor_parameters_to_delete

        out["ParametersToDelete"] = (
            capo_rekognition.types.stream_processor_parameters_to_delete.serialize_aws_json_1_1(
                value["parameters_to_delete"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateStreamProcessorRequest:
    out: UpdateStreamProcessorRequest = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("SettingsForUpdate") is not None:
        import capo_rekognition.types.stream_processor_settings_for_update

        out["settings_for_update"] = (
            capo_rekognition.types.stream_processor_settings_for_update.deserialize_aws_json_1_1(
                data["SettingsForUpdate"]
            )
        )
    if data.get("RegionsOfInterestForUpdate") is not None:
        import capo_rekognition.types.regions_of_interest

        out["regions_of_interest_for_update"] = (
            capo_rekognition.types.regions_of_interest.deserialize_aws_json_1_1(
                data["RegionsOfInterestForUpdate"]
            )
        )
    if data.get("DataSharingPreferenceForUpdate") is not None:
        import capo_rekognition.types.stream_processor_data_sharing_preference

        out["data_sharing_preference_for_update"] = (
            capo_rekognition.types.stream_processor_data_sharing_preference.deserialize_aws_json_1_1(
                data["DataSharingPreferenceForUpdate"]
            )
        )
    if data.get("ParametersToDelete") is not None:
        import capo_rekognition.types.stream_processor_parameters_to_delete

        out["parameters_to_delete"] = (
            capo_rekognition.types.stream_processor_parameters_to_delete.deserialize_aws_json_1_1(
                data["ParametersToDelete"]
            )
        )
    return out
