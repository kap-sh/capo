"""Generated from Smithy shape ``com.amazonaws.socialmessaging#ListWhatsAppFlowsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_socialmessaging.types.meta_flow_summary_list
    import capo_socialmessaging.types.next_token


class ListWhatsAppFlowsOutput(TypedDict, closed=True):
    flows: "capo_socialmessaging.types.meta_flow_summary_list.MetaFlowSummaryList"
    """<p>A list of Flow summaries.</p>"""
    next_token: NotRequired["capo_socialmessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results, if any.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListWhatsAppFlowsOutput) -> dict:
    out: dict = {}
    import capo_socialmessaging.types.meta_flow_summary_list

    out["flows"] = capo_socialmessaging.types.meta_flow_summary_list.serialize_json(
        value["flows"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListWhatsAppFlowsOutput:
    out: ListWhatsAppFlowsOutput = {}  # type: ignore[typeddict-item]
    if data.get("flows") is not None:
        import capo_socialmessaging.types.meta_flow_summary_list

        out["flows"] = (
            capo_socialmessaging.types.meta_flow_summary_list.deserialize_json(
                data["flows"]
            )
        )
    else:
        out["flows"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
