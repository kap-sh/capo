"""Generated from Smithy shape ``com.amazonaws.migrationhubstrategy#AnalyzerNameUnion``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_migrationhubstrategy.errors import DeserializationError, SerializationError
from capo_migrationhubstrategy.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_migrationhubstrategy.types.binary_analyzer_name
    import capo_migrationhubstrategy.types.run_time_analyzer_name
    import capo_migrationhubstrategy.types.source_code_analyzer_name


class AnalyzerNameUnionBinaryAnalyzerNameMember(TypedDict, closed=True):
    binaryAnalyzerName: (
        "capo_migrationhubstrategy.types.binary_analyzer_name.BinaryAnalyzerName"
    )


class AnalyzerNameUnionRunTimeAnalyzerNameMember(TypedDict, closed=True):
    runTimeAnalyzerName: (
        "capo_migrationhubstrategy.types.run_time_analyzer_name.RunTimeAnalyzerName"
    )


class AnalyzerNameUnionSourceCodeAnalyzerNameMember(TypedDict, closed=True):
    sourceCodeAnalyzerName: "capo_migrationhubstrategy.types.source_code_analyzer_name.SourceCodeAnalyzerName"


AnalyzerNameUnion: TypeAlias = (
    AnalyzerNameUnionBinaryAnalyzerNameMember
    | AnalyzerNameUnionRunTimeAnalyzerNameMember
    | AnalyzerNameUnionSourceCodeAnalyzerNameMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: AnalyzerNameUnion) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"AnalyzerNameUnion: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "binaryAnalyzerName" in value:
        return {"binaryAnalyzerName": value["binaryAnalyzerName"]}
    elif "runTimeAnalyzerName" in value:
        return {"runTimeAnalyzerName": value["runTimeAnalyzerName"]}
    elif "sourceCodeAnalyzerName" in value:
        return {"sourceCodeAnalyzerName": value["sourceCodeAnalyzerName"]}
    else:
        raise SerializationError("AnalyzerNameUnion: no variant present")


def deserialize_json(data: dict) -> AnalyzerNameUnion:
    if data.get("binaryAnalyzerName") is not None:
        return {"binaryAnalyzerName": data["binaryAnalyzerName"]}
    elif data.get("runTimeAnalyzerName") is not None:
        return {"runTimeAnalyzerName": data["runTimeAnalyzerName"]}
    elif data.get("sourceCodeAnalyzerName") is not None:
        return {"sourceCodeAnalyzerName": data["sourceCodeAnalyzerName"]}
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("AnalyzerNameUnion: no recognized variant key")
