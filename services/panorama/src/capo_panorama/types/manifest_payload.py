"""Generated from Smithy shape ``com.amazonaws.panorama#ManifestPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError, SerializationError
from capo_panorama.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_panorama.types.manifest_payload_data


class _ManifestPayload_PayloadData(TypedDict, closed=True):
    PayloadData: "capo_panorama.types.manifest_payload_data.ManifestPayloadData"


ManifestPayload: TypeAlias = _ManifestPayload_PayloadData | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ManifestPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ManifestPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PayloadData" in value:
        return {"PayloadData": value["PayloadData"]}
    else:
        raise SerializationError("ManifestPayload: no variant present")


def deserialize_json(data: dict) -> ManifestPayload:
    if data.get("PayloadData") is not None:
        return {"PayloadData": data["PayloadData"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ManifestPayload: no recognized variant key")
