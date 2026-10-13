"""Generated from Smithy shape ``com.amazonaws.rds#TenantDatabasesMessage``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_rds._protocol.xml import Element

if TYPE_CHECKING:
    import capo_rds.types.string
    import capo_rds.types.tenant_databases_list


class TenantDatabasesMessage(TypedDict, closed=True):
    marker: NotRequired["capo_rds.types.string.String"]
    """<p>An optional pagination token provided by a previous <code>DescribeTenantDatabases</code> request. If this parameter is specified, the response includes only records beyond the marker, up to the value specified by <code>MaxRecords</code>.</p>"""
    tenant_databases: NotRequired[
        "capo_rds.types.tenant_databases_list.TenantDatabasesList"
    ]
    """<p>An array of the tenant databases requested by the <code>DescribeTenantDatabases</code> operation.</p>"""


# --- awsQuery ser/de ---
def serialize_query(
    value: TenantDatabasesMessage, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "marker" in value:
        pairs.append((f"{key_prefix}Marker", str(value["marker"])))
    if "tenant_databases" in value:
        import capo_rds.types.tenant_databases_list

        capo_rds.types.tenant_databases_list.serialize_query(
            value["tenant_databases"], pairs, f"{key_prefix}TenantDatabases"
        )


def deserialize_query(el: Element) -> TenantDatabasesMessage:
    out: TenantDatabasesMessage = {}  # type: ignore[typeddict-item]
    child_marker = el.find("Marker")
    if child_marker is not None:
        out["marker"] = str(child_marker.text or "")
    child_tenant_databases = el.find("TenantDatabases")
    if child_tenant_databases is not None:
        import capo_rds.types.tenant_databases_list

        out["tenant_databases"] = (
            capo_rds.types.tenant_databases_list.deserialize_query(
                child_tenant_databases
            )
        )
    return out


def redact_sensitive(value: TenantDatabasesMessage) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "tenant_databases" in value:
        import capo_rds.types.tenant_databases_list

        out["tenant_databases"] = capo_rds.types.tenant_databases_list.redact_sensitive(
            value["tenant_databases"]
        )
    return out
