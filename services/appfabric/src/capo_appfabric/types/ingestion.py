"""Generated from Smithy shape ``com.amazonaws.appfabric#Ingestion``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appfabric.types.arn
    import capo_appfabric.types.date_time
    import capo_appfabric.types.ingestion_state
    import capo_appfabric.types.ingestion_type
    import capo_appfabric.types.string255
    import capo_appfabric.types.tenant_identifier


class Ingestion(TypedDict, closed=True):
    arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the ingestion.</p>"""
    app_bundle_arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app bundle for the ingestion.</p>"""
    app: "capo_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant_id: "capo_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    created_at: "capo_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the ingestion was created.</p>"""
    updated_at: "capo_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the ingestion was last updated.</p>"""
    state: "capo_appfabric.types.ingestion_state.IngestionState"
    """<p>The status of the ingestion.</p>"""
    ingestion_type: "capo_appfabric.types.ingestion_type.IngestionType"
    """<p>The type of the ingestion.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: Ingestion) -> dict:
    out: dict = {}
    out["arn"] = value["arn"]
    out["appBundleArn"] = value["app_bundle_arn"]
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    import capo_appfabric.types.date_time

    out["createdAt"] = capo_appfabric.types.date_time.serialize_json(
        value["created_at"]
    )
    import capo_appfabric.types.date_time

    out["updatedAt"] = capo_appfabric.types.date_time.serialize_json(
        value["updated_at"]
    )
    import capo_appfabric.types.ingestion_state

    out["state"] = capo_appfabric.types.ingestion_state.serialize_json(value["state"])
    import capo_appfabric.types.ingestion_type

    out["ingestionType"] = capo_appfabric.types.ingestion_type.serialize_json(
        value["ingestion_type"]
    )
    return out


def deserialize_json(data: dict) -> Ingestion:
    out: Ingestion = {}  # type: ignore[typeddict-item]
    if data.get("arn") is not None:
        out["arn"] = data["arn"]
    else:
        out["arn"] = ""
    if data.get("appBundleArn") is not None:
        out["app_bundle_arn"] = data["appBundleArn"]
    else:
        out["app_bundle_arn"] = ""
    if data.get("app") is not None:
        out["app"] = data["app"]
    else:
        out["app"] = ""
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    else:
        out["tenant_id"] = ""
    if data.get("createdAt") is not None:
        import capo_appfabric.types.date_time

        out["created_at"] = capo_appfabric.types.date_time.deserialize_json(
            data["createdAt"]
        )
    else:
        import datetime

        out["created_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
    if data.get("updatedAt") is not None:
        import capo_appfabric.types.date_time

        out["updated_at"] = capo_appfabric.types.date_time.deserialize_json(
            data["updatedAt"]
        )
    else:
        import datetime

        out["updated_at"] = datetime.datetime.fromtimestamp(0, tz=datetime.timezone.utc)
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
    if data.get("ingestionType") is not None:
        import capo_appfabric.types.ingestion_type

        out["ingestion_type"] = capo_appfabric.types.ingestion_type.deserialize_json(
            data["ingestionType"]
        )
    else:
        import typing

        out["ingestion_type"] = typing.cast(
            "capo_appfabric.types.ingestion_type.IngestionType", ""
        )
    return out
