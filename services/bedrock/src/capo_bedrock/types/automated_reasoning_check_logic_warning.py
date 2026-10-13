"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningCheckLogicWarning``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_check_logic_warning_type
    import capo_bedrock.types.automated_reasoning_logic_statement_list


class AutomatedReasoningCheckLogicWarning(TypedDict, closed=True):
    type: NotRequired[
        "capo_bedrock.types.automated_reasoning_check_logic_warning_type.AutomatedReasoningCheckLogicWarningType"
    ]
    """<p>The category of the detected logical issue, such as statements that are always true or always false.</p>"""
    premises: NotRequired[
        "capo_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>The logical statements that serve as premises under which the claims are validated.</p>"""
    claims: NotRequired[
        "capo_bedrock.types.automated_reasoning_logic_statement_list.AutomatedReasoningLogicStatementList"
    ]
    """<p>The logical statements that are validated while assuming the policy and premises.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningCheckLogicWarning) -> dict:
    out: dict = {}
    if "type" in value:
        import capo_bedrock.types.automated_reasoning_check_logic_warning_type

        out["type"] = (
            capo_bedrock.types.automated_reasoning_check_logic_warning_type.serialize_json(
                value["type"]
            )
        )
    if "premises" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["premises"]
            )
        )
    if "claims" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.serialize_json(
                value["claims"]
            )
        )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningCheckLogicWarning:
    out: AutomatedReasoningCheckLogicWarning = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_bedrock.types.automated_reasoning_check_logic_warning_type

        out["type"] = (
            capo_bedrock.types.automated_reasoning_check_logic_warning_type.deserialize_json(
                data["type"]
            )
        )
    if data.get("premises") is not None:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["premises"]
            )
        )
    if data.get("claims") is not None:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.deserialize_json(
                data["claims"]
            )
        )
    return out


def redact_sensitive(value: AutomatedReasoningCheckLogicWarning) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "premises" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["premises"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.redact_sensitive(
                value["premises"]
            )
        )
    if "claims" in value:
        import capo_bedrock.types.automated_reasoning_logic_statement_list

        out["claims"] = (
            capo_bedrock.types.automated_reasoning_logic_statement_list.redact_sensitive(
                value["claims"]
            )
        )
    return out
