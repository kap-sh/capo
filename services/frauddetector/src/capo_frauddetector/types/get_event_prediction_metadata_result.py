"""Generated from Smithy shape ``com.amazonaws.frauddetector#GetEventPredictionMetadataResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.evaluated_rule_list
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.list_of_evaluated_external_models
    import capo_frauddetector.types.list_of_evaluated_model_versions
    import capo_frauddetector.types.list_of_event_variable_summaries
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.rule_execution_mode
    import capo_frauddetector.types.string
    import capo_frauddetector.types.time
    import capo_frauddetector.types.whole_number_version_string


class GetEventPredictionMetadataResult(TypedDict, closed=True):
    event_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The event ID. </p>"""
    event_type_name: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The event type associated with the detector specified for this prediction. </p>"""
    entity_id: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The entity ID. </p>"""
    entity_type: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The entity type. </p>"""
    event_timestamp: NotRequired["capo_frauddetector.types.time.time"]
    """<p> The timestamp for when the prediction was generated for the associated event ID. </p>"""
    detector_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p> The detector ID. </p>"""
    detector_version_id: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p> The detector version ID. </p>"""
    detector_version_status: NotRequired["capo_frauddetector.types.string.string"]
    """<p> The status of the detector version. </p>"""
    event_variables: NotRequired[
        "capo_frauddetector.types.list_of_event_variable_summaries.ListOfEventVariableSummaries"
    ]
    """<p> A list of event variables that influenced the prediction scores. </p>"""
    rules: NotRequired["capo_frauddetector.types.evaluated_rule_list.EvaluatedRuleList"]
    """<p> List of rules associated with the detector version that were used for evaluating variable values. </p>"""
    rule_execution_mode: NotRequired[
        "capo_frauddetector.types.rule_execution_mode.RuleExecutionMode"
    ]
    """<p> The execution mode of the rule used for evaluating variable values. </p>"""
    outcomes: NotRequired["capo_frauddetector.types.list_of_strings.ListOfStrings"]
    """<p> The outcomes of the matched rule, based on the rule execution mode. </p>"""
    evaluated_model_versions: NotRequired[
        "capo_frauddetector.types.list_of_evaluated_model_versions.ListOfEvaluatedModelVersions"
    ]
    """<p> Model versions that were evaluated for generating predictions. </p>"""
    evaluated_external_models: NotRequired[
        "capo_frauddetector.types.list_of_evaluated_external_models.ListOfEvaluatedExternalModels"
    ]
    """<p> External (Amazon SageMaker) models that were evaluated for generating predictions. </p>"""
    prediction_timestamp: NotRequired["capo_frauddetector.types.time.time"]
    """<p>The timestamp that defines when the prediction was generated. </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: GetEventPredictionMetadataResult) -> dict:
    out: dict = {}
    if "event_id" in value:
        out["eventId"] = value["event_id"]
    if "event_type_name" in value:
        out["eventTypeName"] = value["event_type_name"]
    if "entity_id" in value:
        out["entityId"] = value["entity_id"]
    if "entity_type" in value:
        out["entityType"] = value["entity_type"]
    if "event_timestamp" in value:
        out["eventTimestamp"] = value["event_timestamp"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "detector_version_id" in value:
        out["detectorVersionId"] = value["detector_version_id"]
    if "detector_version_status" in value:
        out["detectorVersionStatus"] = value["detector_version_status"]
    if "event_variables" in value:
        import capo_frauddetector.types.list_of_event_variable_summaries

        out["eventVariables"] = (
            capo_frauddetector.types.list_of_event_variable_summaries.serialize_aws_json_1_1(
                value["event_variables"]
            )
        )
    if "rules" in value:
        import capo_frauddetector.types.evaluated_rule_list

        out["rules"] = (
            capo_frauddetector.types.evaluated_rule_list.serialize_aws_json_1_1(
                value["rules"]
            )
        )
    if "rule_execution_mode" in value:
        import capo_frauddetector.types.rule_execution_mode

        out["ruleExecutionMode"] = (
            capo_frauddetector.types.rule_execution_mode.serialize_aws_json_1_1(
                value["rule_execution_mode"]
            )
        )
    if "outcomes" in value:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "evaluated_model_versions" in value:
        import capo_frauddetector.types.list_of_evaluated_model_versions

        out["evaluatedModelVersions"] = (
            capo_frauddetector.types.list_of_evaluated_model_versions.serialize_aws_json_1_1(
                value["evaluated_model_versions"]
            )
        )
    if "evaluated_external_models" in value:
        import capo_frauddetector.types.list_of_evaluated_external_models

        out["evaluatedExternalModels"] = (
            capo_frauddetector.types.list_of_evaluated_external_models.serialize_aws_json_1_1(
                value["evaluated_external_models"]
            )
        )
    if "prediction_timestamp" in value:
        out["predictionTimestamp"] = value["prediction_timestamp"]
    return out


def deserialize_aws_json_1_1(data: dict) -> GetEventPredictionMetadataResult:
    out: GetEventPredictionMetadataResult = {}  # type: ignore[typeddict-item]
    if data.get("eventId") is not None:
        out["event_id"] = data["eventId"]
    if data.get("eventTypeName") is not None:
        out["event_type_name"] = data["eventTypeName"]
    if data.get("entityId") is not None:
        out["entity_id"] = data["entityId"]
    if data.get("entityType") is not None:
        out["entity_type"] = data["entityType"]
    if data.get("eventTimestamp") is not None:
        out["event_timestamp"] = data["eventTimestamp"]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    if data.get("detectorVersionStatus") is not None:
        out["detector_version_status"] = data["detectorVersionStatus"]
    if data.get("eventVariables") is not None:
        import capo_frauddetector.types.list_of_event_variable_summaries

        out["event_variables"] = (
            capo_frauddetector.types.list_of_event_variable_summaries.deserialize_aws_json_1_1(
                data["eventVariables"]
            )
        )
    if data.get("rules") is not None:
        import capo_frauddetector.types.evaluated_rule_list

        out["rules"] = (
            capo_frauddetector.types.evaluated_rule_list.deserialize_aws_json_1_1(
                data["rules"]
            )
        )
    if data.get("ruleExecutionMode") is not None:
        import capo_frauddetector.types.rule_execution_mode

        out["rule_execution_mode"] = (
            capo_frauddetector.types.rule_execution_mode.deserialize_aws_json_1_1(
                data["ruleExecutionMode"]
            )
        )
    if data.get("outcomes") is not None:
        import capo_frauddetector.types.list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if data.get("evaluatedModelVersions") is not None:
        import capo_frauddetector.types.list_of_evaluated_model_versions

        out["evaluated_model_versions"] = (
            capo_frauddetector.types.list_of_evaluated_model_versions.deserialize_aws_json_1_1(
                data["evaluatedModelVersions"]
            )
        )
    if data.get("evaluatedExternalModels") is not None:
        import capo_frauddetector.types.list_of_evaluated_external_models

        out["evaluated_external_models"] = (
            capo_frauddetector.types.list_of_evaluated_external_models.deserialize_aws_json_1_1(
                data["evaluatedExternalModels"]
            )
        )
    if data.get("predictionTimestamp") is not None:
        out["prediction_timestamp"] = data["predictionTimestamp"]
    return out


def redact_sensitive(value: GetEventPredictionMetadataResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "event_variables" in value:
        import capo_frauddetector.types.list_of_event_variable_summaries

        out["event_variables"] = (
            capo_frauddetector.types.list_of_event_variable_summaries.redact_sensitive(
                value["event_variables"]
            )
        )
    if "rules" in value:
        import capo_frauddetector.types.evaluated_rule_list

        out["rules"] = capo_frauddetector.types.evaluated_rule_list.redact_sensitive(
            value["rules"]
        )
    if "evaluated_external_models" in value:
        import capo_frauddetector.types.list_of_evaluated_external_models

        out["evaluated_external_models"] = (
            capo_frauddetector.types.list_of_evaluated_external_models.redact_sensitive(
                value["evaluated_external_models"]
            )
        )
    return out
