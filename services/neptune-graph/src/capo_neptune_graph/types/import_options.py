"""Generated from Smithy shape ``com.amazonaws.neptunegraph#ImportOptions``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_neptune_graph.errors import DeserializationError, SerializationError
from capo_neptune_graph.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_neptune_graph.types.neptune_import_options


class _ImportOptions_neptune(TypedDict, closed=True):
    neptune: "capo_neptune_graph.types.neptune_import_options.NeptuneImportOptions"


ImportOptions: TypeAlias = _ImportOptions_neptune | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: ImportOptions) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"ImportOptions: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "neptune" in value:
        import capo_neptune_graph.types.neptune_import_options

        return {
            "neptune": capo_neptune_graph.types.neptune_import_options.serialize_json(
                value["neptune"]
            )
        }
    else:
        raise SerializationError("ImportOptions: no variant present")


def deserialize_json(data: dict) -> ImportOptions:
    if data.get("neptune") is not None:
        import capo_neptune_graph.types.neptune_import_options

        return {
            "neptune": capo_neptune_graph.types.neptune_import_options.deserialize_json(
                data["neptune"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("ImportOptions: no recognized variant key")
