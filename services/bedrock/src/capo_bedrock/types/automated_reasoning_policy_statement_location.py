"""Generated from Smithy shape ``com.amazonaws.bedrock#AutomatedReasoningPolicyStatementLocation``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock.types.automated_reasoning_policy_line_number_list


class AutomatedReasoningPolicyStatementLocation(TypedDict, closed=True):
    lines: "capo_bedrock.types.automated_reasoning_policy_line_number_list.AutomatedReasoningPolicyLineNumberList"
    """<p>The line numbers in the source document where this statement appears.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AutomatedReasoningPolicyStatementLocation) -> dict:
    out: dict = {}
    import capo_bedrock.types.automated_reasoning_policy_line_number_list

    out["lines"] = (
        capo_bedrock.types.automated_reasoning_policy_line_number_list.serialize_json(
            value["lines"]
        )
    )
    return out


def deserialize_json(data: dict) -> AutomatedReasoningPolicyStatementLocation:
    out: AutomatedReasoningPolicyStatementLocation = {}  # type: ignore[typeddict-item]
    if data.get("lines") is not None:
        import capo_bedrock.types.automated_reasoning_policy_line_number_list

        out["lines"] = (
            capo_bedrock.types.automated_reasoning_policy_line_number_list.deserialize_json(
                data["lines"]
            )
        )
    else:
        out["lines"] = []
    return out
