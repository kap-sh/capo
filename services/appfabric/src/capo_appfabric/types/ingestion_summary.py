"""Generated from Smithy shape ``com.amazonaws.appfabric#IngestionSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.arn
    import capo_appfabric.types.ingestion_state
    import capo_appfabric.types.string255
    import capo_appfabric.types.tenant_identifier


class IngestionSummary(TypedDict, closed=True):
    arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion.</p>"""
    app: "capo_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant_id: "capo_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    state: "capo_appfabric.types.ingestion_state.IngestionState"
    """<p>The status of the ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IngestionSummary) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    import capo_appfabric.types.ingestion_state

    out["state"] = capo_appfabric.types.ingestion_state.serialize_json(value["state"])
    return out


def deserialize_json(data: dict) -> IngestionSummary:
    out: IngestionSummary = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("app") is not None:
        out["app"] = data["app"]
    else:
        out["app"] = ""
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    else:
        out["tenant_id"] = ""
    if data.get("state") is not None:
        import capo_appfabric.types.ingestion_state

        out["state"] = capo_appfabric.types.ingestion_state.deserialize_json(
            data["state"]
        )
    else:
        import typing

        out["state"] = typing.cast(
            "capo_appfabric.types.ingestion_state.IngestionState", ""
        )
    return out
