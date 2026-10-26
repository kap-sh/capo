"""Generated from Smithy shape ``com.amazonaws.panorama#ManifestOverridesPayload``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_panorama.errors import DeserializationError, SerializationError
from capo_panorama.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_panorama.types.manifest_overrides_payload_data


class _ManifestOverridesPayload_PayloadData(TypedDict, closed=True):
    PayloadData: "capo_panorama.types.manifest_overrides_payload_data.ManifestOverridesPayloadData"


ManifestOverridesPayload: TypeAlias = (
    _ManifestOverridesPayload_PayloadData | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: ManifestOverridesPayload) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ManifestOverridesPayload: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "PayloadData" in value:
        return {"PayloadData": value["PayloadData"]}
    else:
        raise SerializationError("ManifestOverridesPayload: no variant present")


def deserialize_json(data: dict) -> ManifestOverridesPayload:
    if data.get("PayloadData") is not None:
        return {"PayloadData": data["PayloadData"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "ManifestOverridesPayload: no recognized variant key"
        )
