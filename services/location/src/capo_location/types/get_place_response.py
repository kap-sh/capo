"""Generated from Smithy shape ``com.amazonaws.location#GetPlaceResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import TypedDict

from capo_location.errors import DeserializationError

if TYPE_CHECKING:
    import capo_location.types.place


class GetPlaceResponse(TypedDict, closed=True):
    place: "capo_location.types.place.Place"
    """<p>Details about the result, such as its address and position.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetPlaceResponse) -> dict:
    out: dict = {}
    import capo_location.types.place

    out["Place"] = capo_location.types.place.serialize_json(value["place"])
    return out


def deserialize_json(data: dict) -> GetPlaceResponse:
    out: GetPlaceResponse = {}  # type: ignore[typeddict-item]
    if data.get("Place") is not None:
        import capo_location.types.place

        out["place"] = capo_location.types.place.deserialize_json(data["Place"])
    else:
        raise DeserializationError("GetPlaceResponse.place required")
    return out


def redact_sensitive(value: GetPlaceResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "place" in value:
        import capo_location.types.place

        out["place"] = capo_location.types.place.redact_sensitive(value["place"])
    return out
