"""Generated from Smithy shape ``com.amazonaws.datazone#JobRunDetails``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_datazone.errors import DeserializationError, SerializationError
from capo_datazone.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_datazone.types.lineage_run_details


class _JobRunDetails_lineageRunDetails(TypedDict, closed=True):
    lineageRunDetails: "capo_datazone.types.lineage_run_details.LineageRunDetails"


JobRunDetails: TypeAlias = _JobRunDetails_lineageRunDetails | UnknownUnionMember


# --- restJson1 ser/de ---
def serialize_json(value: JobRunDetails) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"JobRunDetails: cannot serialize unknown variant {value.name!r}"
        )
    elif "lineageRunDetails" in value:
        import capo_datazone.types.lineage_run_details

        return {
            "lineageRunDetails": capo_datazone.types.lineage_run_details.serialize_json(
                value["lineageRunDetails"]
            )
        }
    else:
        raise SerializationError("JobRunDetails: no variant present")


def deserialize_json(data: dict) -> JobRunDetails:
    if data.get("lineageRunDetails") is not None:
        import capo_datazone.types.lineage_run_details

        return {
            "lineageRunDetails": capo_datazone.types.lineage_run_details.deserialize_json(
                data["lineageRunDetails"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("JobRunDetails: no recognized variant key")
