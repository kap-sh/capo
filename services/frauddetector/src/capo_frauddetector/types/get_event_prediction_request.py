"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventPredictionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.event_variable_map
    import capo_frauddetector.types.external_model_endpoint_data_blob_map
    import capo_frauddetector.types.list_of_entities
    import capo_frauddetector.types.string
    import capo_frauddetector.types.utc_timestamp_iso8601
    import capo_frauddetector.types.whole_number_version_string


class GetEventPredictionRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.string.string"
    """<p>The detector ID.</p>"""
    detector_version_id: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The detector version ID.</p>"""
    event_id: "capo_frauddetector.types.string.string"
    """<p>The unique ID used to identify the event.</p>"""
    event_type_name: "capo_frauddetector.types.string.string"
    """<p>The event type associated with the detector specified for the prediction.</p>"""
    entities: "capo_frauddetector.types.list_of_entities.listOfEntities"
    """<p>The entity type (associated with the detector's event type) and specific entity ID representing who performed the event. If an entity id is not available, use "UNKNOWN."</p>"""
    event_timestamp: (
        "capo_frauddetector.types.utc_timestamp_iso8601.utcTimestampISO8601"
    )
    """<p>Timestamp that defines when the event under evaluation occurred. The timestamp must be specified using ISO 8601 standard in UTC.</p>"""
    event_variables: "capo_frauddetector.types.event_variable_map.EventVariableMap"
    """<p>Names of the event type's variables you defined in Amazon Fraud Detector to represent data elements and their corresponding values for the event you are sending for evaluation.</p> <important> <p>You must provide at least one eventVariable</p> </important> <p>To ensure most accurate fraud prediction and to simplify your data preparation, Amazon Fraud Detector will replace all missing variables or values as follows:</p> <p> <b>For Amazon Fraud Detector trained models:</b> </p> <p>If a null value is provided explicitly for a variable or if a variable is missing, model will replace the null value or the missing variable (no variable name in the eventVariables map) with calculated default mean/medians for numeric variables and with special values for categorical variables.</p> <p> <b>For imported SageMaker models:</b> </p> <p>If a null value is provided explicitly for a variable, the model and rules will use “null” as the value. If a variable is not provided (no variable name in the eventVariables map), model and rules will use the default value that is provided for the variable. </p>"""
    external_model_endpoint_data_blobs: NotRequired[
        "capo_frauddetector.types.external_model_endpoint_data_blob_map.ExternalModelEndpointDataBlobMap"
    ]
    """<p>The Amazon SageMaker model endpoint input data blobs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventPredictionRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    out["eventId"] = value["event_id"]
    out["eventTypeName"] = value["event_type_name"]
    import capo_frauddetector.types.list_of_entities

    out["entities"] = capo_frauddetector.types.list_of_entities.serialize_aws_json_1_1(
        value["entities"]
    )
    out["eventTimestamp"] = value["event_timestamp"]
    import capo_frauddetector.types.event_variable_map

    out["eventVariables"] = (
        capo_frauddetector.types.event_variable_map.serialize_aws_json_1_1(
            value["event_variables"]
        )
    )
    if "external_model_endpoint_data_blobs" in value:
        import capo_frauddetector.types.external_model_endpoint_data_blob_map

        out["externalModelEndpointDataBlobs"] = (
            capo_frauddetector.types.external_model_endpoint_data_blob_map.serialize_aws_json_1_1(
                value["external_model_endpoint_data_blobs"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventPredictionRequest:
    out: GetEventPredictionRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        raise DeserializationError("GetEventPredictionRequest.detector_id required")
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    else:
        raise DeserializationError("GetEventPredictionRequest.event_id required")
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    else:
        raise DeserializationError("GetEventPredictionRequest.event_type_name required")
    if data.get("entities") is not None:
        import capo_frauddetector.types.list_of_entities

        out["entities"] = (
            capo_frauddetector.types.list_of_entities.deserialize_aws_json_1_1(
                data["entities"]
            )
        )
    else:
        raise DeserializationError("GetEventPredictionRequest.entities required")
    if data.get("eventTimestamp") is not None:
        out["event_timestamp"] = data["eventTimestamp"]
    else:
        raise DeserializationError("GetEventPredictionRequest.event_timestamp required")
    if data.get("eventVariables") is not None:
        import capo_frauddetector.types.event_variable_map

        out["event_variables"] = (
            capo_frauddetector.types.event_variable_map.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    else:
        raise DeserializationError("GetEventPredictionRequest.event_variables required")
    if data.get("externalModelEndpointDataBlobs") is not None:
        import capo_frauddetector.types.external_model_endpoint_data_blob_map

        out["external_model_endpoint_data_blobs"] = (
            capo_frauddetector.types.external_model_endpoint_data_blob_map.deserialize_aws_json_1_1(
                data["externalModelEndpointDataBlobs"]
            )
        )
    return out
