"""Generated from Smithy shape ``com.amazonaws.lambdamicrovms#ListMicrovmsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_lambda_microvms.errors import DeserializationError

if TYPE_CHECKING:
    import capo_lambda_microvms.types.microvm_item_list
    import capo_lambda_microvms.types.string


class ListMicrovmsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_lambda_microvms.types.string.String"]
    """<p>The pagination token to use in a subsequent request to retrieve the next page of results. This value is null when there are no more results to return.</p>"""
    items: "capo_lambda_microvms.types.microvm_item_list.MicrovmItemList"
    """<p>The list of MicroVMs.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListMicrovmsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_lambda_microvms.types.microvm_item_list

    out["items"] = capo_lambda_microvms.types.microvm_item_list.serialize_json(
        value["items"]
    )
    return out


def deserialize_json(data: dict) -> ListMicrovmsResponse:
    out: ListMicrovmsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("items") is not None:
        import capo_lambda_microvms.types.microvm_item_list

        out["items"] = capo_lambda_microvms.types.microvm_item_list.deserialize_json(
            data["items"]
        )
    else:
        raise DeserializationError("ListMicrovmsResponse.items required")
    return out
