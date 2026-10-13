"""Generated from Smithy shape ``com.amazonaws.rds#DeleteDBInstanceResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.db_instance


class DeleteDBInstanceResult(TypedDict, closed=True):
    db_instance: NotRequired["capo_rds.types.db_instance.DBInstance"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteDBInstanceResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "db_instance" in value:
        import capo_rds.types.db_instance

        capo_rds.types.db_instance.serialize_query(
            value["db_instance"], pairs, f"{key_prefix}DBInstance"
        )


def deserialize_query(el: Element) -> DeleteDBInstanceResult:
    out: DeleteDBInstanceResult = {}  # type: ignore[typeddict-item]
    child_db_instance = el.find("DBInstance")
    if child_db_instance is not None:
        import capo_rds.types.db_instance

        out["db_instance"] = capo_rds.types.db_instance.deserialize_query(
            child_db_instance
        )
    return out


def redact_sensitive(value: DeleteDBInstanceResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "db_instance" in value:
        import capo_rds.types.db_instance

        out["db_instance"] = capo_rds.types.db_instance.redact_sensitive(
            value["db_instance"]
        )
    return out
