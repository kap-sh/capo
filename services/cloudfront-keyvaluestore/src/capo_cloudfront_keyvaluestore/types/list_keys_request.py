"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#ListKeysRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.kvs_arn


class ListKeysRequest(TypedDict, closed=True):
    kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    next_token: NotRequired["str"]
    """<p>If nextToken is returned in the response, there are more results available. Make the next call using the returned token to retrieve the next page.</p>"""
    max_results: NotRequired["int"]
    """<p>Maximum number of results that are returned per call. The default is 10 and maximum allowed page is 50.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListKeysRequest) -> dict:
    out: dict = {}
    return out


def deserialize_json(data: dict) -> ListKeysRequest:
    out: ListKeysRequest = {}  # type: ignore[typeddict-item]
    return out
