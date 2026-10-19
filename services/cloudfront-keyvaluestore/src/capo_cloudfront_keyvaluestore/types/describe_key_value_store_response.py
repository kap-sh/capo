"""Generated from Smithy shape ``com.amazonaws.cloudfrontkeyvaluestore#DescribeKeyValueStoreResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_cloudfront_keyvaluestore.types.etag
    import capo_cloudfront_keyvaluestore.types.kvs_arn


class DescribeKeyValueStoreResponse(TypedDict, closed=True):
    item_count: "int"
    """<p>Number of key value pairs in the Key Value Store.</p>"""
    total_size_in_bytes: "int"
    """<p>Total size of the Key Value Store in bytes.</p>"""
    kvs_arn: "capo_cloudfront_keyvaluestore.types.kvs_arn.KvsARN"
    """<p>The Amazon Resource Name (ARN) of the Key Value Store.</p>"""
    created: "datetime.datetime"
    """<p>Date and time when the Key Value Store was created.</p>"""
    e_tag: "capo_cloudfront_keyvaluestore.types.etag.Etag"
    """<p>The version identifier for the current version of the Key Value Store.</p>"""
    last_modified: NotRequired["datetime.datetime"]
    """<p>Date and time when the key value pairs in the Key Value Store was last modified.</p>"""
    status: NotRequired["str"]
    """<p>The current status of the Key Value Store.</p>"""
    failure_reason: NotRequired["str"]
    """<p>The reason for Key Value Store creation failure.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DescribeKeyValueStoreResponse) -> dict:
    out: dict = {}
    out["ItemCount"] = value["item_count"]
    out["TotalSizeInBytes"] = value["total_size_in_bytes"]
    out["KvsARN"] = value["kvs_arn"]
    import capo_cloudfront_keyvaluestore.types._prelude.timestamp

    out["Created"] = (
        capo_cloudfront_keyvaluestore.types._prelude.timestamp.serialize_json(
            value["created"]
        )
    )
    if "last_modified" in value:
        import capo_cloudfront_keyvaluestore.types._prelude.timestamp

        out["LastModified"] = (
            capo_cloudfront_keyvaluestore.types._prelude.timestamp.serialize_json(
                value["last_modified"]
            )
        )
    if "status" in value:
        out["Status"] = value["status"]
    if "failure_reason" in value:
        out["FailureReason"] = value["failure_reason"]
    return out


def deserialize_json(data: dict) -> DescribeKeyValueStoreResponse:
    out: DescribeKeyValueStoreResponse = {}  # type: ignore[typeddict-item]
    if data.get("ItemCount") is not None:
        out["item_count"] = data["ItemCount"]
    else:
        out["item_count"] = 0
    if data.get("TotalSizeInBytes") is not None:
        out["total_size_in_bytes"] = data["TotalSizeInBytes"]
    else:
        out["total_size_in_bytes"] = 0
    if data.get("KvsARN") is not None:
        out["kvs_arn"] = data["KvsARN"]
    else:
        out["kvs_arn"] = ""
    if data.get("Created") is not None:
        import capo_cloudfront_keyvaluestore.types._prelude.timestamp

        out["created"] = (
            capo_cloudfront_keyvaluestore.types._prelude.timestamp.deserialize_json(
                data["Created"]
            )
        )
    else:
        import datetime

        out["created"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("LastModified") is not None:
        import capo_cloudfront_keyvaluestore.types._prelude.timestamp

        out["last_modified"] = (
            capo_cloudfront_keyvaluestore.types._prelude.timestamp.deserialize_json(
                data["LastModified"]
            )
        )
    if data.get("Status") is not None:
        out["status"] = data["Status"]
    if data.get("FailureReason") is not None:
        out["failure_reason"] = data["FailureReason"]
    return out
