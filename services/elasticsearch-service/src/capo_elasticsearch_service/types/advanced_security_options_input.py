"""Generated from Smithy shape ``com.amazonaws.elasticsearchservice#AdvancedSecurityOptionsInput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_elasticsearch_service.types.boolean
    import capo_elasticsearch_service.types.master_user_options
    import capo_elasticsearch_service.types.saml_options_input


class AdvancedSecurityOptionsInput(TypedDict, closed=True):
    enabled: NotRequired["capo_elasticsearch_service.types.boolean.Boolean"]
    """<p>True if advanced security is enabled.</p>"""
    internal_user_database_enabled: NotRequired[
        "capo_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>True if the internal user database is enabled.</p>"""
    master_user_options: NotRequired[
        "capo_elasticsearch_service.types.master_user_options.MasterUserOptions"
    ]
    """<p>Credentials for the master user: username and password, ARN, or both.</p>"""
    saml_options: NotRequired[
        "capo_elasticsearch_service.types.saml_options_input.SAMLOptionsInput"
    ]
    """<p>Specifies the SAML application configuration for the domain.</p>"""
    anonymous_auth_enabled: NotRequired[
        "capo_elasticsearch_service.types.boolean.Boolean"
    ]
    """<p>True if Anonymous auth is enabled. Anonymous auth can be enabled only when AdvancedSecurity is enabled on existing domains.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AdvancedSecurityOptionsInput) -> dict:
    out: dict = {}
    if "enabled" in value:
        out["Enabled"] = value["enabled"]
    if "internal_user_database_enabled" in value:
        out["InternalUserDatabaseEnabled"] = value["internal_user_database_enabled"]
    if "master_user_options" in value:
        import capo_elasticsearch_service.types.master_user_options

        out["MasterUserOptions"] = (
            capo_elasticsearch_service.types.master_user_options.serialize_json(
                value["master_user_options"]
            )
        )
    if "saml_options" in value:
        import capo_elasticsearch_service.types.saml_options_input

        out["SAMLOptions"] = (
            capo_elasticsearch_service.types.saml_options_input.serialize_json(
                value["saml_options"]
            )
        )
    if "anonymous_auth_enabled" in value:
        out["AnonymousAuthEnabled"] = value["anonymous_auth_enabled"]
    return out


def deserialize_json(data: dict) -> AdvancedSecurityOptionsInput:
    out: AdvancedSecurityOptionsInput = {}  # type: ignore[typeddict-item]
    if data.get("Enabled") is not None:
        out["enabled"] = data["Enabled"]
    if data.get("InternalUserDatabaseEnabled") is not None:
        out["internal_user_database_enabled"] = data["InternalUserDatabaseEnabled"]
    if data.get("MasterUserOptions") is not None:
        import capo_elasticsearch_service.types.master_user_options

        out["master_user_options"] = (
            capo_elasticsearch_service.types.master_user_options.deserialize_json(
                data["MasterUserOptions"]
            )
        )
    if data.get("SAMLOptions") is not None:
        import capo_elasticsearch_service.types.saml_options_input

        out["saml_options"] = (
            capo_elasticsearch_service.types.saml_options_input.deserialize_json(
                data["SAMLOptions"]
            )
        )
    if data.get("AnonymousAuthEnabled") is not None:
        out["anonymous_auth_enabled"] = data["AnonymousAuthEnabled"]
    return out


def redact_sensitive(value: AdvancedSecurityOptionsInput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "master_user_options" in value:
        import capo_elasticsearch_service.types.master_user_options

        out["master_user_options"] = (
            capo_elasticsearch_service.types.master_user_options.redact_sensitive(
                value["master_user_options"]
            )
        )
    if "saml_options" in value:
        import capo_elasticsearch_service.types.saml_options_input

        out["saml_options"] = (
            capo_elasticsearch_service.types.saml_options_input.redact_sensitive(
                value["saml_options"]
            )
        )
    return out
