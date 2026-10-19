"""Generated from Smithy shape ``com.amazonaws.ssmincidents#ListRelatedItemsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ssm_incidents.types.next_token
    import capo_ssm_incidents.types.related_item_list


class ListRelatedItemsOutput(TypedDict, closed=True):
    related_items: "capo_ssm_incidents.types.related_item_list.RelatedItemList"
    """<p>Details about each related item.</p>"""
    next_token: NotRequired["capo_ssm_incidents.types.next_token.NextToken"]
    """<p>The pagination token to use when requesting the next set of items. If there are no additional items to return, the string is null.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRelatedItemsOutput) -> dict:
    out: dict = {}
    import capo_ssm_incidents.types.related_item_list

    out["relatedItems"] = capo_ssm_incidents.types.related_item_list.serialize_json(
        value["related_items"]
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRelatedItemsOutput:
    out: ListRelatedItemsOutput = {}  # type: ignore[typeddict-item]
    if data.get("relatedItems") is not None:
        import capo_ssm_incidents.types.related_item_list

        out["related_items"] = (
            capo_ssm_incidents.types.related_item_list.deserialize_json(
                data["relatedItems"]
            )
        )
    else:
        out["related_items"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
