"""Generated from Smithy shape ``com.amazonaws.connectcases#ListTemplatesResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.next_token
    import capo_connectcases.types.template_summary_list


class ListTemplatesResponse(TypedDict, closed=True):
    templates: "capo_connectcases.types.template_summary_list.TemplateSummaryList"
    """<p>List of template summary objects.</p>"""
    next_token: NotRequired["capo_connectcases.types.next_token.NextToken"]
    """<p>The token for the next set of results. This is null if there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListTemplatesResponse) -> dict:
    out: dict = {}
    import capo_connectcases.types.template_summary_list

    out["templates"] = capo_connectcases.types.template_summary_list.serialize_json(
        value["templates"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListTemplatesResponse:
    out: ListTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("templates") is not None:
        import capo_connectcases.types.template_summary_list

        out["templates"] = (
            capo_connectcases.types.template_summary_list.deserialize_json(
                data["templates"]
            )
        )
    else:
        out["templates"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
