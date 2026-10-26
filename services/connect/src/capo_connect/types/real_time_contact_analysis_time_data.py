"""Generated from Smithy shape ``com.amazonaws.connect#RealTimeContactAnalysisTimeData``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError, SerializationError
from capo_connect.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_connect.types.real_time_contact_analysis_time_instant


class _RealTimeContactAnalysisTimeData_AbsoluteTime(TypedDict, closed=True):
    AbsoluteTime: "capo_connect.types.real_time_contact_analysis_time_instant.RealTimeContactAnalysisTimeInstant"


RealTimeContactAnalysisTimeData: TypeAlias = (
    _RealTimeContactAnalysisTimeData_AbsoluteTime | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RealTimeContactAnalysisTimeData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RealTimeContactAnalysisTimeData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "AbsoluteTime" in value:
        import capo_connect.types.real_time_contact_analysis_time_instant

        return {
            "AbsoluteTime": capo_connect.types.real_time_contact_analysis_time_instant.serialize_json(
                value["AbsoluteTime"]
            )
        }
    else:
        raise SerializationError("RealTimeContactAnalysisTimeData: no variant present")


def deserialize_json(data: dict) -> RealTimeContactAnalysisTimeData:
    if data.get("AbsoluteTime") is not None:
        import capo_connect.types.real_time_contact_analysis_time_instant

        return {
            "AbsoluteTime": capo_connect.types.real_time_contact_analysis_time_instant.deserialize_json(
                data["AbsoluteTime"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RealTimeContactAnalysisTimeData: no recognized variant key"
        )
