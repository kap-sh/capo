"""Generated from Smithy shape ``com.amazonaws.datazone#MetadataGenerationRunTypeStat``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_datazone.types.metadata_generation_run_status
    import capo_datazone.types.metadata_generation_run_type


class MetadataGenerationRunTypeStat(TypedDict, closed=True):
    type: "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType"
    """<p>The type of the metadata generation run type statistics.</p>"""
    status: (
        "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus"
    )
    """<p>The status of the metadata generation run type statistics.</p>"""
    error_message: NotRequired["str"]
    """<p>The error message displayed if the action fails to run.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: MetadataGenerationRunTypeStat) -> dict:
    out: dict = {}
    import capo_datazone.types.metadata_generation_run_type

    out["type"] = capo_datazone.types.metadata_generation_run_type.serialize_json(
        value["type"]
    )
    import capo_datazone.types.metadata_generation_run_status

    out["status"] = capo_datazone.types.metadata_generation_run_status.serialize_json(
        value["status"]
    )
    if "error_message" in value:
        out["errorMessage"] = value["error_message"]
    return out


def deserialize_json(data: dict) -> MetadataGenerationRunTypeStat:
    out: MetadataGenerationRunTypeStat = {}  # type: ignore[typeddict-item]
    if data.get("type") is not None:
        import capo_datazone.types.metadata_generation_run_type

        out["type"] = capo_datazone.types.metadata_generation_run_type.deserialize_json(
            data["type"]
        )
    else:
        import typing

        out["type"] = typing.cast(
            "capo_datazone.types.metadata_generation_run_type.MetadataGenerationRunType",
            "",
        )
    if data.get("status") is not None:
        import capo_datazone.types.metadata_generation_run_status

        out["status"] = (
            capo_datazone.types.metadata_generation_run_status.deserialize_json(
                data["status"]
            )
        )
    else:
        import typing

        out["status"] = typing.cast(
            "capo_datazone.types.metadata_generation_run_status.MetadataGenerationRunStatus",
            "",
        )
    if data.get("errorMessage") is not None:
        out["error_message"] = data["errorMessage"]
    return out
