"""Generated from Smithy shape ``com.amazonaws.appfabric#CreateAppAuthorizationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.auth_type
    import capo_appfabric.types.credential
    import capo_appfabric.types.identifier
    import capo_appfabric.types.string255
    import capo_appfabric.types.tag_list
    import capo_appfabric.types.tenant
    import capo_appfabric.types.uuid


class CreateAppAuthorizationRequest(TypedDict, closed=True):
    app_bundle_identifier: "capo_appfabric.types.identifier.Identifier"
    """<p>The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the app bundle to use for the request.</p>"""
    app: "capo_appfabric.types.string255.String255"
    """<p>The name of the application.</p> <p>Valid values are:</p> <ul> <li> <p> <code>SLACK</code> </p> </li> <li> <p> <code>ASANA</code> </p> </li> <li> <p> <code>JIRA</code> </p> </li> <li> <p> <code>M365</code> </p> </li> <li> <p> <code>M365AUDITLOGS</code> </p> </li> <li> <p> <code>ZOOM</code> </p> </li> <li> <p> <code>ZENDESK</code> </p> </li> <li> <p> <code>OKTA</code> </p> </li> <li> <p> <code>GOOGLE</code> </p> </li> <li> <p> <code>DROPBOX</code> </p> </li> <li> <p> <code>SMARTSHEET</code> </p> </li> <li> <p> <code>CISCO</code> </p> </li> </ul>"""
    credential: "capo_appfabric.types.credential.Credential"
    """<p>Contains credentials for the application, such as an API key or OAuth2 client ID and secret.</p> <p>Specify credentials that match the authorization type for your request. For example, if the authorization type for your request is OAuth2 (<code>oauth2</code>), then you should provide only the OAuth2 credentials.</p>"""
    tenant: "capo_appfabric.types.tenant.Tenant"
    """<p>Contains information about an application tenant, such as the application display name and identifier.</p>"""
    auth_type: "capo_appfabric.types.auth_type.AuthType"
    """<p>The authorization type for the app authorization.</p>"""
    client_token: NotRequired["capo_appfabric.types.uuid.UUID"]
    """<p>Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a <a href="https://wikipedia.org/wiki/Universally_unique_identifier">UUID type of value</a>.</p> <p>If you don't provide this value, then Amazon Web Services generates a random one for you.</p> <p>If you retry the operation with the same <code>ClientToken</code>, but with different parameters, the retry fails with an <code>IdempotentParameterMismatch</code> error.</p>"""
    tags: NotRequired["capo_appfabric.types.tag_list.TagList"]
    """<p>A map of the key-value pairs of the tag or tags to assign to the resource.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateAppAuthorizationRequest) -> dict:
    out: dict = {}
    out["app"] = value["app"]
    import capo_appfabric.types.credential

    out["credential"] = capo_appfabric.types.credential.serialize_json(
        value["credential"]
    )
    import capo_appfabric.types.tenant

    out["tenant"] = capo_appfabric.types.tenant.serialize_json(value["tenant"])
    import capo_appfabric.types.auth_type

    out["authType"] = capo_appfabric.types.auth_type.serialize_json(value["auth_type"])
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.serialize_json(value["tags"])
    return out


def deserialize_json(data: dict) -> CreateAppAuthorizationRequest:
    out: CreateAppAuthorizationRequest = {}  # type: ignore[typeddict-item]
    if data.get("app") is not None:
        out["app"] = data["app"]
    else:
        raise DeserializationError("CreateAppAuthorizationRequest.app required")
    if data.get("credential") is not None:
        import capo_appfabric.types.credential

        out["credential"] = capo_appfabric.types.credential.deserialize_json(
            data["credential"]
        )
    else:
        raise DeserializationError("CreateAppAuthorizationRequest.credential required")
    if data.get("tenant") is not None:
        import capo_appfabric.types.tenant

        out["tenant"] = capo_appfabric.types.tenant.deserialize_json(data["tenant"])
    else:
        raise DeserializationError("CreateAppAuthorizationRequest.tenant required")
    if data.get("authType") is not None:
        import capo_appfabric.types.auth_type

        out["auth_type"] = capo_appfabric.types.auth_type.deserialize_json(
            data["authType"]
        )
    else:
        raise DeserializationError("CreateAppAuthorizationRequest.auth_type required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_appfabric.types.tag_list

        out["tags"] = capo_appfabric.types.tag_list.deserialize_json(data["tags"])
    return out
