"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableBucketResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.account_id
    import capo_s3tables.types.table_bucket_arn
    import capo_s3tables.types.table_bucket_id
    import capo_s3tables.types.table_bucket_name
    import capo_s3tables.types.table_bucket_type


class GetTableBucketResponse(TypedDict, closed=True):
    arn: "capo_s3tables.types.table_bucket_arn.TableBucketARN"
    """<p>The Amazon Resource Name (ARN) of the table bucket.</p>"""
    name: "capo_s3tables.types.table_bucket_name.TableBucketName"
    """<p>The name of the table bucket</p>"""
    owner_account_id: "capo_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that owns the table bucket.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the table bucket was created.</p>"""
    table_bucket_id: NotRequired["capo_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The unique identifier of the table bucket.</p>"""
    type: NotRequired["capo_s3tables.types.table_bucket_type.TableBucketType"]
    """<p>The type of the table bucket.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableBucketResponse) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["name"] = value["name"]
    out["ownerAccountId"] = value["owner_account_id"]
    import capo_s3tables._protocol.serialize

    out["createdAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    if "type" in value:
        import capo_s3tables.types.table_bucket_type

        out["type"] = capo_s3tables.types.table_bucket_type.serialize_json(
            value["type"]
        )
    return out


def deserialize_json(data: dict) -> GetTableBucketResponse:
    out: GetTableBucketResponse = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("tableBucketId") is not None:
        out["table_bucket_id"] = data["tableBucketId"]
    if data.get("type") is not None:
        import capo_s3tables.types.table_bucket_type

        out["type"] = capo_s3tables.types.table_bucket_type.deserialize_json(
            data["type"]
        )
    return out
