"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#GetServiceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_resiliencehubv2.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.service


class GetServiceResponse(TypedDict, closed=True):
    service: "capo_resiliencehubv2.types.service.Service"
    """<p>The requested service.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetServiceResponse) -> dict:
    out: dict = {}
    import capo_resiliencehubv2.types.service

    out["service"] = capo_resiliencehubv2.types.service.serialize_json(value["service"])
    return out


def deserialize_json(data: dict) -> GetServiceResponse:
    out: GetServiceResponse = {}  # type: ignore[typeddict-item]
    if data.get("service") is not None:
        import capo_resiliencehubv2.types.service

        out["service"] = capo_resiliencehubv2.types.service.deserialize_json(
            data["service"]
        )
    else:
        raise DeserializationError("GetServiceResponse.service required")
    return out


def redact_sensitive(value: GetServiceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "service" in value:
        import capo_resiliencehubv2.types.service

        out["service"] = capo_resiliencehubv2.types.service.redact_sensitive(
            value["service"]
        )
    return out
