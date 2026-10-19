"""Generated from Smithy shape ``com.amazonaws.s3tables#GetNamespaceResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.account_id
    import capo_s3tables.types.namespace_id
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.table_bucket_id


class GetNamespaceResponse(TypedDict, closed=True):
    namespace: "capo_s3tables.types.namespace_list.NamespaceList"
    """<p>The name of the namespace.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the namespace was created at.</p>"""
    created_by: "capo_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that created the namespace.</p>"""
    owner_account_id: "capo_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that owns the namespcace.</p>"""
    namespace_id: NotRequired["capo_s3tables.types.namespace_id.NamespaceId"]
    """<p>The unique identifier of the namespace.</p>"""
    table_bucket_id: NotRequired["capo_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The unique identifier of the table bucket containing this namespace.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetNamespaceResponse) -> dict:
    out: dict = {}
    import capo_s3tables.types.namespace_list

    out["namespace"] = capo_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    import capo_s3tables._protocol.serialize

    out["createdAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    out["ownerAccountId"] = value["owner_account_id"]
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    return out


def deserialize_json(data: dict) -> GetNamespaceResponse:
    out: GetNamespaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        import capo_s3tables.types.namespace_list

        out["namespace"] = capo_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        out["namespace"] = []
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("createdBy") is not None:
        out["created_by"] = data["createdBy"]
    else:
        out["created_by"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    if data.get("namespaceId") is not None:
        out["namespace_id"] = data["namespaceId"]
    if data.get("tableBucketId") is not None:
        out["table_bucket_id"] = data["tableBucketId"]
    return out
