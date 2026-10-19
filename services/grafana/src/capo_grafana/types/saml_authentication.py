"""Generated from Smithy shape ``com.amazonaws.grafana#SamlAuthentication``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_grafana.types.saml_configuration
    import capo_grafana.types.saml_configuration_status


class SamlAuthentication(TypedDict, closed=True):
    status: "capo_grafana.types.saml_configuration_status.SamlConfigurationStatus"
    """<p>Specifies whether the workspace's SAML configuration is complete.</p>"""
    configuration: NotRequired[
        "capo_grafana.types.saml_configuration.SamlConfiguration"
    ]
    """<p>A structure containing details about how this workspace works with SAML. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: SamlAuthentication) -> dict:
    out: dict = {}
    out["status"] = value["status"]
    if "configuration" in value:
        import capo_grafana.types.saml_configuration

        out["configuration"] = capo_grafana.types.saml_configuration.serialize_json(
            value["configuration"]
        )
    return out


def deserialize_json(data: dict) -> SamlAuthentication:
    out: SamlAuthentication = {}  # type: ignore[typeddict-item]
    if data.get("status") is not None:
        out["status"] = data["status"]
    else:
        out["status"] = ""
    if data.get("configuration") is not None:
        import capo_grafana.types.saml_configuration

        out["configuration"] = capo_grafana.types.saml_configuration.deserialize_json(
            data["configuration"]
        )
    return out


def redact_sensitive(value: SamlAuthentication) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "configuration" in value:
        import capo_grafana.types.saml_configuration

        out["configuration"] = capo_grafana.types.saml_configuration.redact_sensitive(
            value["configuration"]
        )
    return out
