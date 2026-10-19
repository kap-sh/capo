"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateDetectorVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.list_of_model_versions
    import capo_frauddetector.types.list_of_strings
    import capo_frauddetector.types.rule_execution_mode
    import capo_frauddetector.types.rule_list
    import capo_frauddetector.types.whole_number_version_string


class UpdateDetectorVersionRequest(TypedDict, closed=True):
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The parent detector ID for the detector version you want to update.</p>"""
    detector_version_id: (
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    )
    """<p>The detector version ID. </p>"""
    external_model_endpoints: "capo_frauddetector.types.list_of_strings.ListOfStrings"
    """<p>The Amazon SageMaker model endpoints to include in the detector version.</p>"""
    rules: "capo_frauddetector.types.rule_list.RuleList"
    """<p>The rules to include in the detector version.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The detector version description. </p>"""
    model_versions: NotRequired[
        "capo_frauddetector.types.list_of_model_versions.ListOfModelVersions"
    ]
    """<p>The model versions to include in the detector version.</p>"""
    rule_execution_mode: NotRequired[
        "capo_frauddetector.types.rule_execution_mode.RuleExecutionMode"
    ]
    """<p>The rule execution mode to add to the detector.</p> <p>If you specify <code>FIRST_MATCHED</code>, Amazon Fraud Detector evaluates rules sequentially, first to last, stopping at the first matched rule. Amazon Fraud dectector then provides the outcomes for that single rule.</p> <p>If you specifiy <code>ALL_MATCHED</code>, Amazon Fraud Detector evaluates all rules and returns the outcomes for all matched rules. You can define and edit the rule mode at the detector version level, when it is in draft status.</p> <p>The default behavior is <code>FIRST_MATCHED</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateDetectorVersionRequest) -> dict:
    out: dict = {}
    out["detectorId"] = value["detector_id"]
    out["detectorVersionId"] = value["detector_version_id"]
    import capo_frauddetector.types.list_of_strings

    out["externalModelEndpoints"] = (
        capo_frauddetector.types.list_of_strings.serialize_aws_json_1_1(
            value["external_model_endpoints"]
        )
    )
    import capo_frauddetector.types.rule_list

    out["rules"] = capo_frauddetector.types.rule_list.serialize_aws_json_1_1(
        value["rules"]
    )
    if "description" in value:
        out["description"] = value["description"]
    if "model_versions" in value:
        import capo_frauddetector.types.list_of_model_versions

        out["modelVersions"] = (
            capo_frauddetector.types.list_of_model_versions.serialize_aws_json_1_1(
                value["model_versions"]
            )
        )
    if "rule_execution_mode" in value:
        import capo_frauddetector.types.rule_execution_mode

        out["ruleExecutionMode"] = (
            capo_frauddetector.types.rule_execution_mode.serialize_aws_json_1_1(
                value["rule_execution_mode"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> UpdateDetectorVersionRequest:
    out: UpdateDetectorVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("detectorVersionId") is not None:
        out["detector_version_id"] = data["detectorVersionId"]
    else:
        out["detector_version_id"] = ""
    if data.get("externalModelEndpoints") is not None:
        import capo_frauddetector.types.list_of_strings

        out["external_model_endpoints"] = (
            capo_frauddetector.types.list_of_strings.deserialize_aws_json_1_1(
                data["externalModelEndpoints"]
            )
        )
    else:
        out["external_model_endpoints"] = []
    if data.get("rules") is not None:
        import capo_frauddetector.types.rule_list

        out["rules"] = capo_frauddetector.types.rule_list.deserialize_aws_json_1_1(
            data["rules"]
        )
    else:
        out["rules"] = []
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("modelVersions") is not None:
        import capo_frauddetector.types.list_of_model_versions

        out["model_versions"] = (
            capo_frauddetector.types.list_of_model_versions.deserialize_aws_json_1_1(
                data["modelVersions"]
            )
        )
    if data.get("ruleExecutionMode") is not None:
        import capo_frauddetector.types.rule_execution_mode

        out["rule_execution_mode"] = (
            capo_frauddetector.types.rule_execution_mode.deserialize_aws_json_1_1(
                data["ruleExecutionMode"]
            )
        )
    return out
