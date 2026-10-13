"""Generated from Smithy shape ``com.amazonaws.grafana#SamlConfiguration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_grafana.errors import DeserializationError

if TYPE_CHECKING:
    import capo_grafana.types.allowed_organizations
    import capo_grafana.types.assertion_attributes
    import capo_grafana.types.idp_metadata
    import capo_grafana.types.login_validity_duration
    import capo_grafana.types.role_values


class SamlConfiguration(TypedDict, closed=True):
    idp_metadata: "capo_grafana.types.idp_metadata.IdpMetadata"
    """<p>A structure containing the identity provider (IdP) metadata used to integrate the identity provider with this workspace.</p>"""
    assertion_attributes: NotRequired[
        "capo_grafana.types.assertion_attributes.AssertionAttributes"
    ]
    """<p>A structure that defines which attributes in the SAML assertion are to be used to define information about the users authenticated by that IdP to use the workspace.</p>"""
    role_values: NotRequired["capo_grafana.types.role_values.RoleValues"]
    """<p>A structure containing arrays that map group names in the SAML assertion to the Grafana <code>Admin</code> and <code>Editor</code> roles in the workspace.</p>"""
    allowed_organizations: NotRequired[
        "capo_grafana.types.allowed_organizations.AllowedOrganizations"
    ]
    """<p>Lists which organizations defined in the SAML assertion are allowed to use the Amazon Managed Grafana workspace. If this is empty, all organizations in the assertion attribute have access.</p>"""
    login_validity_duration: (
        "capo_grafana.types.login_validity_duration.LoginValidityDuration"
    )
    """<p>How long a sign-on session by a SAML user is valid, before the user has to sign on again.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamlConfiguration) -> dict:
    out: dict = {}
    import capo_grafana.types.idp_metadata

    out["idpMetadata"] = capo_grafana.types.idp_metadata.serialize_json(
        value["idp_metadata"]
    )
    if "assertion_attributes" in value:
        import capo_grafana.types.assertion_attributes

        out["assertionAttributes"] = (
            capo_grafana.types.assertion_attributes.serialize_json(
                value["assertion_attributes"]
            )
        )
    if "role_values" in value:
        import capo_grafana.types.role_values

        out["roleValues"] = capo_grafana.types.role_values.serialize_json(
            value["role_values"]
        )
    if "allowed_organizations" in value:
        import capo_grafana.types.allowed_organizations

        out["allowedOrganizations"] = (
            capo_grafana.types.allowed_organizations.serialize_json(
                value["allowed_organizations"]
            )
        )
    out["loginValidityDuration"] = value.get("login_validity_duration", 0)
    return out


def deserialize_json(data: dict) -> SamlConfiguration:
    out: SamlConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("idpMetadata") is not None:
        import capo_grafana.types.idp_metadata

        out["idp_metadata"] = capo_grafana.types.idp_metadata.deserialize_json(
            data["idpMetadata"]
        )
    else:
        raise DeserializationError("SamlConfiguration.idp_metadata required")
    if data.get("assertionAttributes") is not None:
        import capo_grafana.types.assertion_attributes

        out["assertion_attributes"] = (
            capo_grafana.types.assertion_attributes.deserialize_json(
                data["assertionAttributes"]
            )
        )
    if data.get("roleValues") is not None:
        import capo_grafana.types.role_values

        out["role_values"] = capo_grafana.types.role_values.deserialize_json(
            data["roleValues"]
        )
    if data.get("allowedOrganizations") is not None:
        import capo_grafana.types.allowed_organizations

        out["allowed_organizations"] = (
            capo_grafana.types.allowed_organizations.deserialize_json(
                data["allowedOrganizations"]
            )
        )
    if data.get("loginValidityDuration") is not None:
        out["login_validity_duration"] = data["loginValidityDuration"]
    else:
        out["login_validity_duration"] = 0
    return out


def redact_sensitive(value: SamlConfiguration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "role_values" in value:
        import capo_grafana.types.role_values

        out["role_values"] = capo_grafana.types.role_values.redact_sensitive(
            value["role_values"]
        )
    return out
