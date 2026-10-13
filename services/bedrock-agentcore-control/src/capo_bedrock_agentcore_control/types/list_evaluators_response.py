"""Generated from Smithy shape ``com.amazonaws.bedrockagentcorecontrol#ListEvaluatorsResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_bedrock_agentcore_control.errors import DeserializationError

if TYPE_CHECKING:
    import capo_bedrock_agentcore_control.types.evaluator_summary_list


class ListEvaluatorsResponse(TypedDict, closed=True):
    evaluators: "capo_bedrock_agentcore_control.types.evaluator_summary_list.EvaluatorSummaryList"
    """<p> The list of evaluator summaries containing basic information about each evaluator. </p>"""
    next_token: NotRequired["str"]
    """<p> The pagination token to use in a subsequent request to retrieve the next page of results. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEvaluatorsResponse) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore_control.types.evaluator_summary_list

    out["evaluators"] = (
        capo_bedrock_agentcore_control.types.evaluator_summary_list.serialize_json(
            value["evaluators"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEvaluatorsResponse:
    out: ListEvaluatorsResponse = {}  # type: ignore[typeddict-item]
    if data.get("evaluators") is not None:
        import capo_bedrock_agentcore_control.types.evaluator_summary_list

        out["evaluators"] = (
            capo_bedrock_agentcore_control.types.evaluator_summary_list.deserialize_json(
                data["evaluators"]
            )
        )
    else:
        raise DeserializationError("ListEvaluatorsResponse.evaluators required")
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListEvaluatorsResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "evaluators" in value:
        import capo_bedrock_agentcore_control.types.evaluator_summary_list

        out["evaluators"] = (
            capo_bedrock_agentcore_control.types.evaluator_summary_list.redact_sensitive(
                value["evaluators"]
            )
        )
    return out
