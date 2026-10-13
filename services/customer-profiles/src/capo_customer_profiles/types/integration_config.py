"""Generated from Smithy shape ``com.amazonaws.customerprofiles#IntegrationConfig``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.appflow_integration


class IntegrationConfig(TypedDict, closed=True):
    appflow_integration: NotRequired[
        "capo_customer_profiles.types.appflow_integration.AppflowIntegration"
    ]
    """<p>Configuration data for <code>APPFLOW_INTEGRATION</code> workflow type.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: IntegrationConfig) -> dict:
    out: dict = {}
    if "appflow_integration" in value:
        import capo_customer_profiles.types.appflow_integration

        out["AppflowIntegration"] = (
            capo_customer_profiles.types.appflow_integration.serialize_json(
                value["appflow_integration"]
            )
        )
    return out


def deserialize_json(data: dict) -> IntegrationConfig:
    out: IntegrationConfig = {}  # type: ignore[typeddict-item]
    if data.get("AppflowIntegration") is not None:
        import capo_customer_profiles.types.appflow_integration

        out["appflow_integration"] = (
            capo_customer_profiles.types.appflow_integration.deserialize_json(
                data["AppflowIntegration"]
            )
        )
    return out


def redact_sensitive(value: IntegrationConfig) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "appflow_integration" in value:
        import capo_customer_profiles.types.appflow_integration

        out["appflow_integration"] = (
            capo_customer_profiles.types.appflow_integration.redact_sensitive(
                value["appflow_integration"]
            )
        )
    return out
