"""Generated from Smithy shape ``com.amazonaws.appfabric#AppAuthorization``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_appfabric.errors import DeserializationError

if TYPE_CHECKING:
    import capo_appfabric.types.app_authorization_status
    import capo_appfabric.types.arn
    import capo_appfabric.types.auth_type
    import capo_appfabric.types.date_time
    import capo_appfabric.types.persona
    import capo_appfabric.types.string255
    import capo_appfabric.types.tenant


class AppAuthorization(TypedDict, closed=True):
    app_authorization_arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app authorization.</p>"""
    app_bundle_arn: "capo_appfabric.types.arn.Arn"
    """<p>The Amazon Resource Name (ARN) of the app bundle for the app authorization.</p>"""
    app: "capo_appfabric.types.string255.String255"
    """<p>The name of the application.</p>"""
    tenant: "capo_appfabric.types.tenant.Tenant"
    """<p>Contains information about an application tenant, such as the application display name and identifier.</p>"""
    auth_type: "capo_appfabric.types.auth_type.AuthType"
    """<p>The authorization type.</p>"""
    status: "capo_appfabric.types.app_authorization_status.AppAuthorizationStatus"
    """<p>The state of the app authorization.</p> <p>The following states are possible:</p> <ul> <li> <p> <code>PendingConnect</code>: The initial state of the app authorization. The app authorization is created but not yet connected.</p> </li> <li> <p> <code>Connected</code>: The app authorization is connected to the application, and is ready to be used.</p> </li> <li> <p> <code>ConnectionValidationFailed</code>: The app authorization received a validation exception when trying to connect to the application. If the app authorization is in this state, you should verify the configured credentials and try to connect the app authorization again.</p> </li> <li> <p> <code>TokenAutoRotationFailed</code>: AppFabric failed to refresh the access token. If the app authorization is in this state, you should try to reconnect the app authorization.</p> </li> </ul>"""
    created_at: "capo_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the app authorization was created.</p>"""
    updated_at: "capo_appfabric.types.date_time.DateTime"
    """<p>The timestamp of when the app authorization was last updated.</p>"""
    persona: NotRequired["capo_appfabric.types.persona.Persona"]
    """<p>The user persona of the app authorization.</p> <p>This field should always be <code>admin</code>.</p>"""
    auth_url: NotRequired["str"]
    """<p>The application URL for the OAuth flow.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppAuthorization) -> dict:
    out: dict = {}
    out["appAuthorizationArn"] = value["app_authorization_arn"]
    out["appBundleArn"] = value["app_bundle_arn"]
    out["app"] = value["app"]
    import capo_appfabric.types.tenant

    out["tenant"] = capo_appfabric.types.tenant.serialize_json(value["tenant"])
    import capo_appfabric.types.auth_type

    out["authType"] = capo_appfabric.types.auth_type.serialize_json(value["auth_type"])
    import capo_appfabric.types.app_authorization_status

    out["status"] = capo_appfabric.types.app_authorization_status.serialize_json(
        value["status"]
    )
    import capo_appfabric.types.date_time

    out["createdAt"] = capo_appfabric.types.date_time.serialize_json(
        value["created_at"]
    )
    import capo_appfabric.types.date_time

    out["updatedAt"] = capo_appfabric.types.date_time.serialize_json(
        value["updated_at"]
    )
    if "persona" in value:
        import capo_appfabric.types.persona

        out["persona"] = capo_appfabric.types.persona.serialize_json(value["persona"])
    if "auth_url" in value:
        out["authUrl"] = value["auth_url"]
    return out


def deserialize_json(data: dict) -> AppAuthorization:
    out: AppAuthorization = {}  # type: ignore[typeddict-item]
    if data.get("appAuthorizationArn") is not None:
        out["app_authorization_arn"] = data["appAuthorizationArn"]
    else:
        out["app_authorization_arn"] = ""
    if data.get("appBundleArn") is not None:
        out["app_bundle_arn"] = data["appBundleArn"]
    else:
        out["app_bundle_arn"] = ""
    if data.get("app") is not None:
        out["app"] = data["app"]
    else:
        out["app"] = ""
    if data.get("tenant") is not None:
        import capo_appfabric.types.tenant

        out["tenant"] = capo_appfabric.types.tenant.deserialize_json(data["tenant"])
    else:
        raise DeserializationError("AppAuthorization.tenant required")
    if data.get("authType") is not None:
        import capo_appfabric.types.auth_type

        out["auth_type"] = capo_appfabric.types.auth_type.deserialize_json(
            data["authType"]
        )
    else:
        import typing

        out["auth_type"] = typing.cast("capo_appfabric.types.auth_type.AuthType", "")
    if data.get("status") is not None:
        import capo_appfabric.types.app_authorization_status

        out["status"] = capo_appfabric.types.app_authorization_status.deserialize_json(
            data["status"]
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_appfabric.types.app_authorization_status.AppAuthorizationStatus", ""
        )
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
    if data.get("persona") is not None:
        import capo_appfabric.types.persona

        out["persona"] = capo_appfabric.types.persona.deserialize_json(data["persona"])
    if data.get("authUrl") is not None:
        out["auth_url"] = data["authUrl"]
    return out
