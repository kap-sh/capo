"""Generated from Smithy shape ``com.amazonaws.frauddetector#RuleDetail``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.fraud_detector_arn
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.language
    import capo_frauddetector.types.non_empty_list_of_strings
    import capo_frauddetector.types.rule_expression
    import capo_frauddetector.types.time
    import capo_frauddetector.types.whole_number_version_string


class RuleDetail(TypedDict, closed=True):
    rule_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The rule ID.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The rule description.</p>"""
    detector_id: NotRequired["capo_frauddetector.types.identifier.identifier"]
    """<p>The detector for which the rule is associated.</p>"""
    rule_version: NotRequired[
        "capo_frauddetector.types.whole_number_version_string.wholeNumberVersionString"
    ]
    """<p>The rule version.</p>"""
    expression: NotRequired["capo_frauddetector.types.rule_expression.ruleExpression"]
    """<p>The rule expression.</p>"""
    language: NotRequired["capo_frauddetector.types.language.Language"]
    """<p>The rule language.</p>"""
    outcomes: NotRequired[
        "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    ]
    """<p>The rule outcomes.</p>"""
    last_updated_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>Timestamp of the last time the rule was updated.</p>"""
    created_time: NotRequired["capo_frauddetector.types.time.time"]
    """<p>The timestamp of when the rule was created.</p>"""
    arn: NotRequired["capo_frauddetector.types.fraud_detector_arn.fraudDetectorArn"]
    """<p>The rule ARN.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: RuleDetail) -> dict:
    out: dict = {}
    if "rule_id" in value:
        out["ruleId"] = value["rule_id"]
    if "description" in value:
        out["description"] = value["description"]
    if "detector_id" in value:
        out["detectorId"] = value["detector_id"]
    if "rule_version" in value:
        out["ruleVersion"] = value["rule_version"]
    if "expression" in value:
        out["expression"] = value["expression"]
    if "language" in value:
        import capo_frauddetector.types.language

        out["language"] = capo_frauddetector.types.language.serialize_aws_json_1_1(
            value["language"]
        )
    if "outcomes" in value:
        import capo_frauddetector.types.non_empty_list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.non_empty_list_of_strings.serialize_aws_json_1_1(
                value["outcomes"]
            )
        )
    if "last_updated_time" in value:
        out["lastUpdatedTime"] = value["last_updated_time"]
    if "created_time" in value:
        out["createdTime"] = value["created_time"]
    if "arn" in value:
        out["arn"] = value["arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> RuleDetail:
    out: RuleDetail = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    if data.get("ruleVersion") is not None:
        out["rule_version"] = data["ruleVersion"]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    if data.get("language") is not None:
        import capo_frauddetector.types.language

        out["language"] = capo_frauddetector.types.language.deserialize_aws_json_1_1(
            data["language"]
        )
    if data.get("outcomes") is not None:
        import capo_frauddetector.types.non_empty_list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.non_empty_list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    if data.get("lastUpdatedTime") is not None:
        out["last_updated_time"] = data["lastUpdatedTime"]
    if data.get("createdTime") is not None:
        out["created_time"] = data["createdTime"]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    return out


def redact_sensitive(value: RuleDetail) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
