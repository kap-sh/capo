"""Generated from Smithy shape ``com.amazonaws.invoicing#GetProcurementPortalPreferenceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_invoicing.errors import DeserializationError

if TYPE_CHECKING:
    import capo_invoicing.types.procurement_portal_preference


class GetProcurementPortalPreferenceResponse(TypedDict, closed=True):
    procurement_portal_preference: (
        "capo_invoicing.types.procurement_portal_preference.ProcurementPortalPreference"
    )
    """<p>The detailed configuration of the requested procurement portal preference.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: GetProcurementPortalPreferenceResponse) -> dict:
    out: dict = {}
    import capo_invoicing.types.procurement_portal_preference

    out["ProcurementPortalPreference"] = (
        capo_invoicing.types.procurement_portal_preference.serialize_aws_json_1_0(
            value["procurement_portal_preference"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> GetProcurementPortalPreferenceResponse:
    out: GetProcurementPortalPreferenceResponse = {}  # type: ignore[typeddict-item]
    if data.get("ProcurementPortalPreference") is not None:
        import capo_invoicing.types.procurement_portal_preference

        out["procurement_portal_preference"] = (
            capo_invoicing.types.procurement_portal_preference.deserialize_aws_json_1_0(
                data["ProcurementPortalPreference"]
            )
        )
    else:
        raise DeserializationError(
            "GetProcurementPortalPreferenceResponse.procurement_portal_preference required"
        )
    return out


def redact_sensitive(value: GetProcurementPortalPreferenceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "procurement_portal_preference" in value:
        import capo_invoicing.types.procurement_portal_preference

        out["procurement_portal_preference"] = (
            capo_invoicing.types.procurement_portal_preference.redact_sensitive(
                value["procurement_portal_preference"]
            )
        )
    return out
