"""Generated from Smithy shape ``com.amazonaws.bedrockagentcore#InvokeWebSearchOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bedrock_agentcore.types.web_search_result_list


class InvokeWebSearchOutput(TypedDict, closed=True):
    results: "capo_bedrock_agentcore.types.web_search_result_list.WebSearchResultList"
    """<p>The search results, in ranked order.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: InvokeWebSearchOutput) -> dict:
    out: dict = {}
    import capo_bedrock_agentcore.types.web_search_result_list

    out["results"] = capo_bedrock_agentcore.types.web_search_result_list.serialize_json(
        value["results"]
    )
    return out


def deserialize_json(data: dict) -> InvokeWebSearchOutput:
    out: InvokeWebSearchOutput = {}  # type: ignore[typeddict-item]
    if data.get("results") is not None:
        import capo_bedrock_agentcore.types.web_search_result_list

        out["results"] = (
            capo_bedrock_agentcore.types.web_search_result_list.deserialize_json(
                data["results"]
            )
        )
    else:
        out["results"] = []
    return out
