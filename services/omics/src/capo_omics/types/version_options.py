"""Generated from Smithy shape ``com.amazonaws.omics#VersionOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_omics.errors import DeserializationError, SerializationError
from capo_omics.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_omics.types.tsv_version_options


class VersionOptionsTsvVersionOptionsMember(TypedDict, closed=True):
    tsvVersionOptions: "capo_omics.types.tsv_version_options.TsvVersionOptions"


VersionOptions: TypeAlias = VersionOptionsTsvVersionOptionsMember | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: VersionOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"VersionOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "tsvVersionOptions" in value:
        import capo_omics.types.tsv_version_options

        return {
            "tsvVersionOptions": capo_omics.types.tsv_version_options.serialize_json(
                value["tsvVersionOptions"]
            )
        }
    else:
        raise SerializationError("VersionOptions: no variant present")


def deserialize_json(data: dict) -> VersionOptions:
    if data.get("tsvVersionOptions") is not None:
        import capo_omics.types.tsv_version_options

        return {
            "tsvVersionOptions": capo_omics.types.tsv_version_options.deserialize_json(
                data["tsvVersionOptions"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("VersionOptions: no recognized variant key")
