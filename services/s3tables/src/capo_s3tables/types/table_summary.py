"""Generated from Smithy shape ``com.amazonaws.s3tables#TableSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.namespace_id
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_id
    import capo_s3tables.types.table_name
    import capo_s3tables.types.table_type


class TableSummary(TypedDict, closed=True):
    namespace: "capo_s3tables.types.namespace_list.NamespaceList"
    """<p>The name of the namespace.</p>"""
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    type: "capo_s3tables.types.table_type.TableType"
    """<p>The type of the table.</p>"""
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the table was created at.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the table was last modified at.</p>"""
    managed_by_service: NotRequired["str"]
    """<p>The Amazon Web Services service managing this table, if applicable. For example, a replicated table is managed by the S3 Tables replication service.</p>"""
    namespace_id: NotRequired["capo_s3tables.types.namespace_id.NamespaceId"]
    """<p>The unique identifier for the namespace that contains this table.</p>"""
    table_bucket_id: NotRequired["capo_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The unique identifier for the table bucket that contains this table.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: TableSummary) -> dict:
    out: dict = {}
    import capo_s3tables.types.namespace_list

    out["namespace"] = capo_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    out["name"] = value["name"]
    import capo_s3tables.types.table_type

    out["type"] = capo_s3tables.types.table_type.serialize_json(value["type"])
    out["tableARN"] = value["table_arn"]
    import capo_s3tables._protocol.serialize

    out["createdAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    import capo_s3tables._protocol.serialize

    out["modifiedAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["modified_at"]
    )
    if "managed_by_service" in value:
        out["managedByService"] = value["managed_by_service"]
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    return out


def deserialize_json(data: dict) -> TableSummary:
    out: TableSummary = {}  # type: ignore[typeddict-item]
    if data.get("namespace") is not None:
        import capo_s3tables.types.namespace_list

        out["namespace"] = capo_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        out["namespace"] = []
    if data.get("name") is not None:
        out["name"] = data["name"]
    else:
        out["name"] = ""
    if data.get("type") is not None:
        import capo_s3tables.types.table_type

        out["type"] = capo_s3tables.types.table_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_s3tables.types.table_type.TableType", "")
    if data.get("tableARN") is not None:
        out["table_arn"] = data["tableARN"]
    else:
        out["table_arn"] = ""
    if data.get("createdAt") is not None:
        import datetime

        out["created_at"] = datetime.datetime.fromisoformat(
            data["createdAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("modifiedAt") is not None:
        import datetime

        out["modified_at"] = datetime.datetime.fromisoformat(
            data["modifiedAt"].replace("Z", "+00:00")
        )
    else:
        import datetime

        out["modified_at"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("managedByService") is not None:
        out["managed_by_service"] = data["managedByService"]
    if data.get("namespaceId") is not None:
        out["namespace_id"] = data["namespaceId"]
    if data.get("tableBucketId") is not None:
        out["table_bucket_id"] = data["tableBucketId"]
    return out
