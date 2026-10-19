"""Generated from Smithy shape ``com.amazonaws.grafana#AuthenticationSummary``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.authentication_providers
    import capo_grafana.types.saml_configuration_status


class AuthenticationSummary(TypedDict, closed=True):
    providers: "capo_grafana.types.authentication_providers.AuthenticationProviders"
    """<p>Specifies whether the workspace uses SAML, IAM Identity Center, or both methods for user authentication.</p>"""
    saml_configuration_status: NotRequired[
        "capo_grafana.types.saml_configuration_status.SamlConfigurationStatus"
    ]
    """<p>Specifies whether the workplace's user authentication method is fully configured.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AuthenticationSummary) -> dict:
    out: dict = {}
    import capo_grafana.types.authentication_providers

    out["providers"] = capo_grafana.types.authentication_providers.serialize_json(
        value["providers"]
    )
    if "saml_configuration_status" in value:
        out["samlConfigurationStatus"] = value["saml_configuration_status"]
    return out


def deserialize_json(data: dict) -> AuthenticationSummary:
    out: AuthenticationSummary = {}  # type: ignore[typeddict-item]
    if data.get("providers") is not None:
        import capo_grafana.types.authentication_providers

        out["providers"] = capo_grafana.types.authentication_providers.deserialize_json(
            data["providers"]
        )
    else:
        out["providers"] = []
    if data.get("samlConfigurationStatus") is not None:
        out["saml_configuration_status"] = data["samlConfigurationStatus"]
    return out
