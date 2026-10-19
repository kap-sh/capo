"""Generated from Smithy shape ``com.amazonaws.grafana#AuthenticationDescription``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.authentication_providers
    import capo_grafana.types.aws_sso_authentication
    import capo_grafana.types.saml_authentication


class AuthenticationDescription(TypedDict, closed=True):
    providers: "capo_grafana.types.authentication_providers.AuthenticationProviders"
    """<p>Specifies whether this workspace uses IAM Identity Center, SAML, or both methods to authenticate users to use the Grafana console in the Amazon Managed Grafana workspace.</p>"""
    saml: NotRequired["capo_grafana.types.saml_authentication.SamlAuthentication"]
    """<p>A structure containing information about how this workspace works with SAML, including what attributes within the assertion are to be mapped to user information in the workspace. </p>"""
    aws_sso: NotRequired[
        "capo_grafana.types.aws_sso_authentication.AwsSsoAuthentication"
    ]
    """<p>A structure containing information about how this workspace works with IAM Identity Center. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationDescription) -> dict:
    out: dict = {}
    import capo_grafana.types.authentication_providers

    out["providers"] = capo_grafana.types.authentication_providers.serialize_json(
        value["providers"]
    )
    if "saml" in value:
        import capo_grafana.types.saml_authentication

        out["saml"] = capo_grafana.types.saml_authentication.serialize_json(
            value["saml"]
        )
    if "aws_sso" in value:
        import capo_grafana.types.aws_sso_authentication

        out["awsSso"] = capo_grafana.types.aws_sso_authentication.serialize_json(
            value["aws_sso"]
        )
    return out


def deserialize_json(data: dict) -> AuthenticationDescription:
    out: AuthenticationDescription = {}  # type: ignore[typeddict-item]
    if data.get("providers") is not None:
        import capo_grafana.types.authentication_providers

        out["providers"] = capo_grafana.types.authentication_providers.deserialize_json(
            data["providers"]
        )
    else:
        out["providers"] = []
    if data.get("saml") is not None:
        import capo_grafana.types.saml_authentication

        out["saml"] = capo_grafana.types.saml_authentication.deserialize_json(
            data["saml"]
        )
    if data.get("awsSso") is not None:
        import capo_grafana.types.aws_sso_authentication

        out["aws_sso"] = capo_grafana.types.aws_sso_authentication.deserialize_json(
            data["awsSso"]
        )
    return out


def redact_sensitive(value: AuthenticationDescription) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "saml" in value:
        import capo_grafana.types.saml_authentication

        out["saml"] = capo_grafana.types.saml_authentication.redact_sensitive(
            value["saml"]
        )
    return out
