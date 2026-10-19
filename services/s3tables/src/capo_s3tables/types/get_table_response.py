"""Generated from Smithy shape ``com.amazonaws.s3tables#GetTableResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import datetime

    import capo_s3tables.types.account_id
    import capo_s3tables.types.managed_table_information
    import capo_s3tables.types.metadata_location
    import capo_s3tables.types.namespace_id
    import capo_s3tables.types.namespace_list
    import capo_s3tables.types.open_table_format
    import capo_s3tables.types.table_arn
    import capo_s3tables.types.table_bucket_id
    import capo_s3tables.types.table_name
    import capo_s3tables.types.table_type
    import capo_s3tables.types.version_token
    import capo_s3tables.types.warehouse_location


class GetTableResponse(TypedDict, closed=True):
    name: "capo_s3tables.types.table_name.TableName"
    """<p>The name of the table.</p>"""
    type: "capo_s3tables.types.table_type.TableType"
    """<p>The type of the table.</p>"""
    table_arn: "capo_s3tables.types.table_arn.TableARN"
    """<p>The Amazon Resource Name (ARN) of the table.</p>"""
    namespace: "capo_s3tables.types.namespace_list.NamespaceList"
    """<p>The namespace associated with the table.</p>"""
    namespace_id: NotRequired["capo_s3tables.types.namespace_id.NamespaceId"]
    """<p>The unique identifier of the namespace containing this table.</p>"""
    version_token: "capo_s3tables.types.version_token.VersionToken"
    """<p>The version token of the table.</p>"""
    metadata_location: NotRequired[
        "capo_s3tables.types.metadata_location.MetadataLocation"
    ]
    """<p>The metadata location of the table.</p>"""
    warehouse_location: "capo_s3tables.types.warehouse_location.WarehouseLocation"
    """<p>The warehouse location of the table.</p>"""
    created_at: "datetime.datetime"
    """<p>The date and time the table bucket was created at.</p>"""
    created_by: "capo_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that created the table.</p>"""
    managed_by_service: NotRequired["str"]
    """<p>The service that manages the table.</p>"""
    modified_at: "datetime.datetime"
    """<p>The date and time the table was last modified on.</p>"""
    modified_by: "capo_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that last modified the table.</p>"""
    owner_account_id: "capo_s3tables.types.account_id.AccountId"
    """<p>The ID of the account that owns the table.</p>"""
    format: "capo_s3tables.types.open_table_format.OpenTableFormat"
    """<p>The format of the table.</p>"""
    table_bucket_id: NotRequired["capo_s3tables.types.table_bucket_id.TableBucketId"]
    """<p>The unique identifier of the table bucket containing this table.</p>"""
    managed_table_information: NotRequired[
        "capo_s3tables.types.managed_table_information.ManagedTableInformation"
    ]
    """<p>If this table is managed by S3 Tables, contains additional information such as replication details.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetTableResponse) -> dict:
    out: dict = {}
    out["name"] = value["name"]
    import capo_s3tables.types.table_type

    out["type"] = capo_s3tables.types.table_type.serialize_json(value["type"])
    out["tableARN"] = value["table_arn"]
    import capo_s3tables.types.namespace_list

    out["namespace"] = capo_s3tables.types.namespace_list.serialize_json(
        value["namespace"]
    )
    if "namespace_id" in value:
        out["namespaceId"] = value["namespace_id"]
    out["versionToken"] = value["version_token"]
    if "metadata_location" in value:
        out["metadataLocation"] = value["metadata_location"]
    out["warehouseLocation"] = value["warehouse_location"]
    import capo_s3tables._protocol.serialize

    out["createdAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["created_at"]
    )
    out["createdBy"] = value["created_by"]
    if "managed_by_service" in value:
        out["managedByService"] = value["managed_by_service"]
    import capo_s3tables._protocol.serialize

    out["modifiedAt"] = capo_s3tables._protocol.serialize.fmt_date_time(
        value["modified_at"]
    )
    out["modifiedBy"] = value["modified_by"]
    out["ownerAccountId"] = value["owner_account_id"]
    import capo_s3tables.types.open_table_format

    out["format"] = capo_s3tables.types.open_table_format.serialize_json(
        value["format"]
    )
    if "table_bucket_id" in value:
        out["tableBucketId"] = value["table_bucket_id"]
    if "managed_table_information" in value:
        import capo_s3tables.types.managed_table_information

        out["managedTableInformation"] = (
            capo_s3tables.types.managed_table_information.serialize_json(
                value["managed_table_information"]
            )
        )
    return out


def deserialize_json(data: dict) -> GetTableResponse:
    out: GetTableResponse = {}  # type: ignore[typeddict-item]
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
    if data.get("namespace") is not None:
        import capo_s3tables.types.namespace_list

        out["namespace"] = capo_s3tables.types.namespace_list.deserialize_json(
            data["namespace"]
        )
    else:
        out["namespace"] = []
    if data.get("namespaceId") is not None:
        out["namespace_id"] = data["namespaceId"]
    if data.get("versionToken") is not None:
        out["version_token"] = data["versionToken"]
    else:
        out["version_token"] = ""
    if data.get("metadataLocation") is not None:
        out["metadata_location"] = data["metadataLocation"]
    if data.get("warehouseLocation") is not None:
        out["warehouse_location"] = data["warehouseLocation"]
    else:
        out["warehouse_location"] = ""
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
    if data.get("managedByService") is not None:
        out["managed_by_service"] = data["managedByService"]
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
    if data.get("modifiedBy") is not None:
        out["modified_by"] = data["modifiedBy"]
    else:
        out["modified_by"] = ""
    if data.get("ownerAccountId") is not None:
        out["owner_account_id"] = data["ownerAccountId"]
    else:
        out["owner_account_id"] = ""
    if data.get("format") is not None:
        import capo_s3tables.types.open_table_format

        out["format"] = capo_s3tables.types.open_table_format.deserialize_json(
            data["format"]
        )
    else:
        import typing

        out["format"] = typing.cast(
            "capo_s3tables.types.open_table_format.OpenTableFormat", ""
        )
    if data.get("tableBucketId") is not None:
        out["table_bucket_id"] = data["tableBucketId"]
    if data.get("managedTableInformation") is not None:
        import capo_s3tables.types.managed_table_information

        out["managed_table_information"] = (
            capo_s3tables.types.managed_table_information.deserialize_json(
                data["managedTableInformation"]
            )
        )
    return out
