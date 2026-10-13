"""Generated from Smithy shape ``com.amazonaws.customerprofiles#AppflowIntegration``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.batches
    import capo_customer_profiles.types.flow_definition


class AppflowIntegration(TypedDict, closed=True):
    flow_definition: "capo_customer_profiles.types.flow_definition.FlowDefinition"
    batches: NotRequired["capo_customer_profiles.types.batches.Batches"]
    """<p>Batches in workflow of type <code>APPFLOW_INTEGRATION</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AppflowIntegration) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.flow_definition

    out["FlowDefinition"] = capo_customer_profiles.types.flow_definition.serialize_json(
        value["flow_definition"]
    )
    if "batches" in value:
        import capo_customer_profiles.types.batches

        out["Batches"] = capo_customer_profiles.types.batches.serialize_json(
            value["batches"]
        )
    return out


def deserialize_json(data: dict) -> AppflowIntegration:
    out: AppflowIntegration = {}  # type: ignore[typeddict-item]
    if data.get("FlowDefinition") is not None:
        import capo_customer_profiles.types.flow_definition

        out["flow_definition"] = (
            capo_customer_profiles.types.flow_definition.deserialize_json(
                data["FlowDefinition"]
            )
        )
    else:
        raise DeserializationError("AppflowIntegration.flow_definition required")
    if data.get("Batches") is not None:
        import capo_customer_profiles.types.batches

        out["batches"] = capo_customer_profiles.types.batches.deserialize_json(
            data["Batches"]
        )
    return out


def redact_sensitive(value: AppflowIntegration) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "flow_definition" in value:
        out["flow_definition"] = "*** Sensitive Data Redacted ***"
    return out
