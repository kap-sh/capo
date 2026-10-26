"""Generated from Smithy shape ``com.amazonaws.quicksight#PhysicalTable``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_quicksight.errors import DeserializationError, SerializationError
from capo_quicksight.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_quicksight.types.custom_sql
    import capo_quicksight.types.file_source
    import capo_quicksight.types.relational_table
    import capo_quicksight.types.s3_source
    import capo_quicksight.types.saa_s_table


class _PhysicalTable_RelationalTable(TypedDict, closed=True):
    RelationalTable: "capo_quicksight.types.relational_table.RelationalTable"


class _PhysicalTable_CustomSql(TypedDict, closed=True):
    CustomSql: "capo_quicksight.types.custom_sql.CustomSql"


class _PhysicalTable_S3Source(TypedDict, closed=True):
    S3Source: "capo_quicksight.types.s3_source.S3Source"


class _PhysicalTable_SaaSTable(TypedDict, closed=True):
    SaaSTable: "capo_quicksight.types.saa_s_table.SaaSTable"


class _PhysicalTable_FileSource(TypedDict, closed=True):
    FileSource: "capo_quicksight.types.file_source.FileSource"


PhysicalTable: TypeAlias = (
    _PhysicalTable_RelationalTable
    | _PhysicalTable_CustomSql
    | _PhysicalTable_S3Source
    | _PhysicalTable_SaaSTable
    | _PhysicalTable_FileSource
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: PhysicalTable) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"PhysicalTable: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "RelationalTable" in value:
        import capo_quicksight.types.relational_table

        return {
            "RelationalTable": capo_quicksight.types.relational_table.serialize_json(
                value["RelationalTable"]
            )
        }
    elif "CustomSql" in value:
        import capo_quicksight.types.custom_sql

        return {
            "CustomSql": capo_quicksight.types.custom_sql.serialize_json(
                value["CustomSql"]
            )
        }
    elif "S3Source" in value:
        import capo_quicksight.types.s3_source

        return {
            "S3Source": capo_quicksight.types.s3_source.serialize_json(
                value["S3Source"]
            )
        }
    elif "SaaSTable" in value:
        import capo_quicksight.types.saa_s_table

        return {
            "SaaSTable": capo_quicksight.types.saa_s_table.serialize_json(
                value["SaaSTable"]
            )
        }
    elif "FileSource" in value:
        import capo_quicksight.types.file_source

        return {
            "FileSource": capo_quicksight.types.file_source.serialize_json(
                value["FileSource"]
            )
        }
    else:
        raise SerializationError("PhysicalTable: no variant present")


def deserialize_json(data: dict) -> PhysicalTable:
    if data.get("RelationalTable") is not None:
        import capo_quicksight.types.relational_table

        return {
            "RelationalTable": capo_quicksight.types.relational_table.deserialize_json(
                data["RelationalTable"]
            )
        }
    elif data.get("CustomSql") is not None:
        import capo_quicksight.types.custom_sql

        return {
            "CustomSql": capo_quicksight.types.custom_sql.deserialize_json(
                data["CustomSql"]
            )
        }
    elif data.get("S3Source") is not None:
        import capo_quicksight.types.s3_source

        return {
            "S3Source": capo_quicksight.types.s3_source.deserialize_json(
                data["S3Source"]
            )
        }
    elif data.get("SaaSTable") is not None:
        import capo_quicksight.types.saa_s_table

        return {
            "SaaSTable": capo_quicksight.types.saa_s_table.deserialize_json(
                data["SaaSTable"]
            )
        }
    elif data.get("FileSource") is not None:
        import capo_quicksight.types.file_source

        return {
            "FileSource": capo_quicksight.types.file_source.deserialize_json(
                data["FileSource"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("PhysicalTable: no recognized variant key")


def redact_sensitive(value: PhysicalTable) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "CustomSql" in value:
        import capo_quicksight.types.custom_sql

        out["CustomSql"] = capo_quicksight.types.custom_sql.redact_sensitive(
            value["CustomSql"]
        )
    return out
