"""Generated from Smithy shape ``com.amazonaws.personalizeevents#PutItemsRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_personalize_events.types.arn
    import capo_personalize_events.types.item_list


class PutItemsRequest(TypedDict, closed=True):
    dataset_arn: "capo_personalize_events.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the Items dataset you are adding the item or items to.</p>"""
    items: "capo_personalize_events.types.item_list.ItemList"
    """<p>A list of item data.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PutItemsRequest) -> dict:
    out: dict = {}
    out["datasetArn"] = value["dataset_arn"]
    import capo_personalize_events.types.item_list

    out["items"] = capo_personalize_events.types.item_list.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> PutItemsRequest:
    out: PutItemsRequest = {}  # type: ignore[typeddict-item]
    if data.get("datasetArn") is not None:
        out["dataset_arn"] = data["datasetArn"]
    else:
        out["dataset_arn"] = ""
    if data.get("items") is not None:
        import capo_personalize_events.types.item_list

        out["items"] = capo_personalize_events.types.item_list.deserialize_json(
            data["items"]
        )
    else:
        out["items"] = []
    return out


def redact_sensitive(value: PutItemsRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_personalize_events.types.item_list

        out["items"] = capo_personalize_events.types.item_list.redact_sensitive(
            value["items"]
        )
    return out
