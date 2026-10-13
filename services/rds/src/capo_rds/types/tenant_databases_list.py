"""Generated from Smithy shape ``com.amazonaws.rds#TenantDatabasesList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.tenant_database

TenantDatabasesList: TypeAlias = list["capo_rds.types.tenant_database.TenantDatabase"]


# --- awsQuery ser/de ---
def serialize_query(
    value: TenantDatabasesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.tenant_database

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.tenant_database.serialize_query(
            item, pairs, f"{prefix}.TenantDatabase.{n}"
        )


def deserialize_query(el: Element) -> TenantDatabasesList:
    import capo_rds.types.tenant_database

    out: TenantDatabasesList = []
    for child in el.findall("TenantDatabase"):
        out.append(capo_rds.types.tenant_database.deserialize_query(child))
    return out


def serialize_query_flat(
    value: TenantDatabasesList, pairs: list[tuple[str, str]], prefix: str
) -> None:
    import capo_rds.types.tenant_database

    if not value:
        pairs.append((prefix, ""))
        return
    for n, item in enumerate(value, 1):
        capo_rds.types.tenant_database.serialize_query(item, pairs, f"{prefix}.{n}")


def deserialize_query_flat(parent: Element, tag: str) -> TenantDatabasesList:
    import capo_rds.types.tenant_database

    out: TenantDatabasesList = []
    for child in parent.findall(tag):
        out.append(capo_rds.types.tenant_database.deserialize_query(child))
    return out


def redact_sensitive(value: TenantDatabasesList) -> list[Any]:
    import capo_rds.types.tenant_database

    return [capo_rds.types.tenant_database.redact_sensitive(item) for item in value]
