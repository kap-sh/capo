"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AnalysisStatusUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhubstrategy.errors import DeserializationError, SerializationError
from capo_migrationhubstrategy.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.runtime_analysis_status
    import capo_migrationhubstrategy.types.src_code_or_db_analysis_status


class _AnalysisStatusUnion_runtimeAnalysisStatus(TypedDict, closed=True):
    runtimeAnalysisStatus: (
        "capo_migrationhubstrategy.types.runtime_analysis_status.RuntimeAnalysisStatus"
    )


class _AnalysisStatusUnion_srcCodeOrDbAnalysisStatus(TypedDict, closed=True):
    srcCodeOrDbAnalysisStatus: "capo_migrationhubstrategy.types.src_code_or_db_analysis_status.SrcCodeOrDbAnalysisStatus"


AnalysisStatusUnion: TypeAlias = (
    _AnalysisStatusUnion_runtimeAnalysisStatus
    | _AnalysisStatusUnion_srcCodeOrDbAnalysisStatus
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalysisStatusUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnalysisStatusUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "runtimeAnalysisStatus" in value:
        return {"runtimeAnalysisStatus": value["runtimeAnalysisStatus"]}
    elif "srcCodeOrDbAnalysisStatus" in value:
        return {"srcCodeOrDbAnalysisStatus": value["srcCodeOrDbAnalysisStatus"]}
    else:
        raise SerializationError("AnalysisStatusUnion: no variant present")


def deserialize_json(data: dict) -> AnalysisStatusUnion:
    if data.get("runtimeAnalysisStatus") is not None:
        return {"runtimeAnalysisStatus": data["runtimeAnalysisStatus"]}
    elif data.get("srcCodeOrDbAnalysisStatus") is not None:
        return {"srcCodeOrDbAnalysisStatus": data["srcCodeOrDbAnalysisStatus"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AnalysisStatusUnion: no recognized variant key")
