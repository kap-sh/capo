"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateIngestionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.identifier
    import capo_appfabric.types.ingestion_type
    import capo_appfabric.types.string255
    import capo_appfabric.types.tag_list
    import capo_appfabric.types.tenant_identifier
    import capo_appfabric.types.uuid


class CreateIngestionRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    app: "capo_appfabric.types.string255.String255"
    """<p>The name of the application.</p> <p>Valid values are:</p> <ul> <li> <p> <code>SLACK</code> </p> </li> <li> <p> <code>ASANA</code> </p> </li> <li> <p> <code>JIRA</code> </p> </li> <li> <p> <code>M365</code> </p> </li> <li> <p> <code>M365AUDITLOGS</code> </p> </li> <li> <p> <code>ZOOM</code> </p> </li> <li> <p> <code>ZENDESK</code> </p> </li> <li> <p> <code>OKTA</code> </p> </li> <li> <p> <code>GOOGLE</code> </p> </li> <li> <p> <code>DROPBOX</code> </p> </li> <li> <p> <code>SMARTSHEET</code> </p> </li> <li> <p> <code>CISCO</code> </p> </li> </ul>"""
    tenant_id: "capo_appfabric.types.tenant_identifier.TenantIdentifier"
    """<p>The ID of the application tenant.</p>"""
    ingestion_type: "capo_appfabric.types.ingestion_type.IngestionType"
    """<p>The ingestion type.</p>"""
    client_token: NotRequired["capo_appfabric.types.uuid.UUID"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_appfabric.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateIngestionRequest) -> dict:
    out: dict = {}
    out["app"] = value["app"]
    out["tenantId"] = value["tenant_id"]
    import capo_appfabric.types.ingestion_type

    out["ingestionType"] = capo_appfabric.types.ingestion_type.serialize_json(
        value["ingestion_type"]
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateIngestionRequest:
    out: CreateIngestionRequest = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        out["app"] = data["app"]
    else:
        raise DeserializationError("CreateIngestionRequest.app required")
    if data.get("tenantId") is not None:
        out["tenant_id"] = data["tenantId"]
    else:
        raise DeserializationError("CreateIngestionRequest.tenant_id required")
    if data.get("ingestionType") is not None:
        import capo_appfabric.types.ingestion_type

        out["ingestion_type"] = capo_appfabric.types.ingestion_type.deserialize_json(
            data["ingestionType"]
        )
    else:
        raise DeserializationError("CreateIngestionRequest.ingestion_type required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.deserialize_json(data["tags"])
    return out
