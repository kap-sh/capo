"""Generated from Smithy shape ``com.amazonaws.frauddetector#UpdateRuleVersionRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_frauddetector.errors import DeserializationError

if TYPE_CHECKING:
    import capo_frauddetector.types.description
    import capo_frauddetector.types.language
    import capo_frauddetector.types.non_empty_list_of_strings
    import capo_frauddetector.types.rule
    import capo_frauddetector.types.rule_expression
    import capo_frauddetector.types.tag_list


class UpdateRuleVersionRequest(TypedDict, closed=True):
    rule: "capo_frauddetector.types.rule.Rule"
    """<p>The rule to update.</p>"""
    description: NotRequired["capo_frauddetector.types.description.description"]
    """<p>The description.</p>"""
    expression: "capo_frauddetector.types.rule_expression.ruleExpression"
    """<p>The rule expression.</p>"""
    language: "capo_frauddetector.types.language.Language"
    """<p>The language.</p>"""
    outcomes: "capo_frauddetector.types.non_empty_list_of_strings.NonEmptyListOfStrings"
    """<p>The outcomes.</p>"""
    tags: NotRequired["capo_frauddetector.types.tag_list.tagList"]
    """<p>The tags to assign to the rule version.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: UpdateRuleVersionRequest) -> dict:
    out: dict = {}
    import capo_frauddetector.types.rule

    out["rule"] = capo_frauddetector.types.rule.serialize_aws_json_1_1(value["rule"])
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


def deserialize_aws_json_1_1(data: dict) -> UpdateRuleVersionRequest:
    out: UpdateRuleVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("rule") is not None:
        import capo_frauddetector.types.rule

        out["rule"] = capo_frauddetector.types.rule.deserialize_aws_json_1_1(
            data["rule"]
        )
    else:
        raise DeserializationError("UpdateRuleVersionRequest.rule required")
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


def redact_sensitive(value: UpdateRuleVersionRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "expression" in value:
        out["expression"] = "*** Sensitive Data Redacted ***"
    return out
