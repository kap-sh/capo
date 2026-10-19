"""Generated from Smithy shape ``com.amazonaws.frauddetector#CreateRuleRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.identifier
    import capo_frauddetector.types.language
    import capo_frauddetector.types.non_empty_list_of_strings
    import capo_frauddetector.types.rule_expression
    import capo_frauddetector.types.tag_list


class CreateRuleRequest(TypedDict, closed=True):
    rule_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The rule ID.</p>"""
    detector_id: "capo_frauddetector.types.identifier.identifier"
    """<p>The detector ID for the rule's parent detector.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The rule description.</p>"""
    expression: "capo_frauddetector.types.rule_expression.ruleExpression"
    """<p>The rule expression.</p>"""
    language: "capo_frauddetector.types.language.Language"
    """<p>The language of the rule.</p>"""
    outcomes: "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    """<p>The outcome or outcomes returned when the rule expression matches.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>A collection of key and value pairs.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRuleRequest) -> dict:
    out: dict = {}
    out["ruleId"] = value["rule_id"]
    out["detectorId"] = value["detector_id"]
    if "description" in value:
        out["description"] = value["description"]
    out["expression"] = value["expression"]
    import capo_frauddetector.types.language

    out["language"] = capo_frauddetector.types.language.serialize_aws_json_1_1(
        value["language"]
    )
    import capo_frauddetector.types.non_empty_list_of_strings

    out["outcomes"] = (
        capo_frauddetector.types.non_empty_list_of_strings.serialize_aws_json_1_1(
            value["outcomes"]
        )
    )
    if "tags" in value:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.serialize_aws_json_1_1(
            value["tags"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRuleRequest:
    out: CreateRuleRequest = {}  # type: ignore[typeddict-item]
    if data.get("ruleId") is not None:
        out["rule_id"] = data["ruleId"]
    else:
        out["rule_id"] = ""
    if data.get("detectorId") is not None:
        out["detector_id"] = data["detectorId"]
    else:
        out["detector_id"] = ""
    if data.get("description") is not None:
        out["description"] = data["description"]
    if data.get("expression") is not None:
        out["expression"] = data["expression"]
    else:
        out["expression"] = ""
    if data.get("language") is not None:
        import capo_frauddetector.types.language

        out["language"] = capo_frauddetector.types.language.deserialize_aws_json_1_1(
            data["language"]
        )
    else:
        import typing

        out["language"] = typing.cast("capo_frauddetector.types.language.Language", "")
    if data.get("outcomes") is not None:
        import capo_frauddetector.types.non_empty_list_of_strings

        out["outcomes"] = (
            capo_frauddetector.types.non_empty_list_of_strings.deserialize_aws_json_1_1(
                data["outcomes"]
            )
        )
    else:
        out["outcomes"] = []
    if data.get("tags") is not None:
        import capo_frauddetector.types.tag_list

        out["tags"] = capo_frauddetector.types.tag_list.deserialize_aws_json_1_1(
            data["tags"]
        )
    return out


def redact_sensitive(value: CreateRuleRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
