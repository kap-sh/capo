"""Generated from Smithy shape ``com.amazonaws.backup#GetRestoreTestingInferredMetadataOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backup.types.string_map


class GetRestoreTestingInferredMetadataOutput(TypedDict, closed=True):
    inferred_metadata: "capo_backup.types.string_map.stringMap"
    """<p>This is a string map of the metadata inferred from the request.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: GetRestoreTestingInferredMetadataOutput) -> dict:
    out: dict = {}
    import capo_backup.types.string_map

    out["InferredMetadata"] = capo_backup.types.string_map.serialize_json(
        value["inferred_metadata"]
    )
    return out


def deserialize_json(data: dict) -> GetRestoreTestingInferredMetadataOutput:
    out: GetRestoreTestingInferredMetadataOutput = {}  # type: ignore[typeddict-item]
    if data.get("InferredMetadata") is not None:
        import capo_backup.types.string_map

        out["inferred_metadata"] = capo_backup.types.string_map.deserialize_json(
            data["InferredMetadata"]
        )
    else:
        out["inferred_metadata"] = {}
    return out
