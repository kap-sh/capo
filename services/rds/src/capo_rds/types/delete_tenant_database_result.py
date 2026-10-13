"""Generated from Smithy shape ``com.amazonaws.rds#DeleteTenantDatabaseResult``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.tenant_database


class DeleteTenantDatabaseResult(TypedDict, closed=True):
    tenant_database: NotRequired["capo_rds.types.tenant_database.TenantDatabase"]


# --- awsQuery ser/de ---
def serialize_query(
    value: DeleteTenantDatabaseResult, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "tenant_database" in value:
        import capo_rds.types.tenant_database

        capo_rds.types.tenant_database.serialize_query(
            value["tenant_database"], pairs, f"{key_prefix}TenantDatabase"
        )


def deserialize_query(el: Element) -> DeleteTenantDatabaseResult:
    out: DeleteTenantDatabaseResult = {}  # type: ignore[typeddict-item]
    child_tenant_database = el.find("TenantDatabase")
    if child_tenant_database is not None:
        import capo_rds.types.tenant_database

        out["tenant_database"] = capo_rds.types.tenant_database.deserialize_query(
            child_tenant_database
        )
    return out


def redact_sensitive(value: DeleteTenantDatabaseResult) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tenant_database" in value:
        import capo_rds.types.tenant_database

        out["tenant_database"] = capo_rds.types.tenant_database.redact_sensitive(
            value["tenant_database"]
        )
    return out
