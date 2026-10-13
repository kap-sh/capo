"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#ListKeysResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.list_keys_response_list


class ListKeysResponse(TypedDict, closed=True):
    next_token: NotRequired["str"]
    """<p>If nextToken is returned in the response, there are more results available. Make the next call using the returned token to retrieve the next page.</p>"""
    items: NotRequired[
        "capo_cloudfront_keyvaluestore.types.list_keys_response_list.ListKeysResponseList"
    ]
    """<p>Key value pairs</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    if "items" in value:
        import capo_cloudfront_keyvaluestore.types.list_keys_response_list

        out["Items"] = (
            capo_cloudfront_keyvaluestore.types.list_keys_response_list.serialize_json(
                value["items"]
            )
        )
    return out


def deserialize_json(data: dict) -> ListKeysResponse:
    out: ListKeysResponse = {}  # type: ignore[typeddict-item]
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    if data.get("Items") is not None:
        import capo_cloudfront_keyvaluestore.types.list_keys_response_list

        out["items"] = (
            capo_cloudfront_keyvaluestore.types.list_keys_response_list.deserialize_json(
                data["Items"]
            )
        )
    return out


def redact_sensitive(value: ListKeysResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "items" in value:
        import capo_cloudfront_keyvaluestore.types.list_keys_response_list

        out["items"] = (
            capo_cloudfront_keyvaluestore.types.list_keys_response_list.redact_sensitive(
                value["items"]
            )
        )
    return out
