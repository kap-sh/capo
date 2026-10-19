"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DetectProfileObjectTypeRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_customer_profiles.types.name
    import capo_customer_profiles.types.objects


class DetectProfileObjectTypeRequest(TypedDict, closed=True):
    objects: "capo_customer_profiles.types.objects.Objects"
    """<p>A string that is serialized from a JSON object.</p>"""
    domain_name: "capo_customer_profiles.types.name.name"
    """<p>The unique name of the domain.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DetectProfileObjectTypeRequest) -> dict:
    out: dict = {}
    import capo_customer_profiles.types.objects

    out["Objects"] = capo_customer_profiles.types.objects.serialize_json(
        value["objects"]
    )
    return out


def deserialize_json(data: dict) -> DetectProfileObjectTypeRequest:
    out: DetectProfileObjectTypeRequest = {}  # type: ignore[typeddict-item]
    if data.get("Objects") is not None:
        import capo_customer_profiles.types.objects

        out["objects"] = capo_customer_profiles.types.objects.deserialize_json(
            data["Objects"]
        )
    else:
        out["objects"] = []
    return out


def redact_sensitive(value: DetectProfileObjectTypeRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "objects" in value:
        out["objects"] = "*** Sensitive Data Redacted ***"
    return out
