"""Generated from Smithy shape ``com.amazonaws.connect#ListExtractionDefinitionsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.extraction_definition_summary_list
    import capo_connect.types.next_token


class ListExtractionDefinitionsResponse(TypedDict, closed=True):
    extraction_definition_summary_list: "capo_connect.types.extraction_definition_summary_list.ExtractionDefinitionSummaryList"
    """<p>Information about the extraction definitions.</p>"""
    next_token: NotRequired["capo_connect.types.next_token.NextToken"]
    """<p>If there are additional results, this is the token for the next set of results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListExtractionDefinitionsResponse) -> dict:
    out: dict = {}
    import capo_connect.types.extraction_definition_summary_list

    out["ExtractionDefinitionSummaryList"] = (
        capo_connect.types.extraction_definition_summary_list.serialize_json(
            value["extraction_definition_summary_list"]
        )
    )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListExtractionDefinitionsResponse:
    out: ListExtractionDefinitionsResponse = {}  # type: ignore[typeddict-item]
    if data.get("ExtractionDefinitionSummaryList") is not None:
        import capo_connect.types.extraction_definition_summary_list

        out["extraction_definition_summary_list"] = (
            capo_connect.types.extraction_definition_summary_list.deserialize_json(
                data["ExtractionDefinitionSummaryList"]
            )
        )
    else:
        out["extraction_definition_summary_list"] = []
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
