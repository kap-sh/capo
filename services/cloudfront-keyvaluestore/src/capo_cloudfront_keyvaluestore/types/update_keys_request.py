"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#UpdateKeysRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cloudfront_keyvaluestore.types.delete_key_requests_list
    import capo_cloudfront_keyvaluestore.types.etag
    import capo_cloudfront_keyvaluestore.types.kvs_arn
    import capo_cloudfront_keyvaluestore.types.put_key_requests_list


class UpdateKeysRequest(TypedDict, closed=True):
    kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    if_match: "capo_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The current version (ETag) of the Key Value Store that you are updating keys of, which you can get using DescribeKeyValueStore.</p>"""
    puts: NotRequired[
        "capo_cloudfront_keyvaluestore.types.put_key_requests_list.PutKeyRequestsList"
    ]
    """<p>List of key value pairs to put.</p>"""
    deletes: NotRequired[
        "capo_cloudfront_keyvaluestore.types.delete_key_requests_list.DeleteKeyRequestsList"
    ]
    """<p>List of keys to delete.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateKeysRequest) -> dict:
    out: dict = {}
    if "puts" in value:
        import capo_cloudfront_keyvaluestore.types.put_key_requests_list

        out["Puts"] = (
            capo_cloudfront_keyvaluestore.types.put_key_requests_list.serialize_json(
                value["puts"]
            )
        )
    if "deletes" in value:
        import capo_cloudfront_keyvaluestore.types.delete_key_requests_list

        out["Deletes"] = (
            capo_cloudfront_keyvaluestore.types.delete_key_requests_list.serialize_json(
                value["deletes"]
            )
        )
    return out


def deserialize_json(data: dict) -> UpdateKeysRequest:
    out: UpdateKeysRequest = {}  # type: ignore[typeddict-item]
    if data.get("Puts") is not None:
        import capo_cloudfront_keyvaluestore.types.put_key_requests_list

        out["puts"] = (
            capo_cloudfront_keyvaluestore.types.put_key_requests_list.deserialize_json(
                data["Puts"]
            )
        )
    if data.get("Deletes") is not None:
        import capo_cloudfront_keyvaluestore.types.delete_key_requests_list

        out["deletes"] = (
            capo_cloudfront_keyvaluestore.types.delete_key_requests_list.deserialize_json(
                data["Deletes"]
            )
        )
    return out


def redact_sensitive(value: UpdateKeysRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "puts" in value:
        import capo_cloudfront_keyvaluestore.types.put_key_requests_list

        out["puts"] = (
            capo_cloudfront_keyvaluestore.types.put_key_requests_list.redact_sensitive(
                value["puts"]
            )
        )
    return out
