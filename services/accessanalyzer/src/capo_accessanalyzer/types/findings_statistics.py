"""Generated from Smithy shape ``com.amazonaws.accessanalyzer#FindingsStatistics``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_accessanalyzer.errors import DeserializationError, SerializationError
from capo_accessanalyzer.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_accessanalyzer.types.external_access_findings_statistics
    import capo_accessanalyzer.types.internal_access_findings_statistics
    import capo_accessanalyzer.types.unused_access_findings_statistics


class _FindingsStatistics_externalAccessFindingsStatistics(TypedDict, closed=True):
    externalAccessFindingsStatistics: "capo_accessanalyzer.types.external_access_findings_statistics.ExternalAccessFindingsStatistics"


class _FindingsStatistics_internalAccessFindingsStatistics(TypedDict, closed=True):
    internalAccessFindingsStatistics: "capo_accessanalyzer.types.internal_access_findings_statistics.InternalAccessFindingsStatistics"


class _FindingsStatistics_unusedAccessFindingsStatistics(TypedDict, closed=True):
    unusedAccessFindingsStatistics: "capo_accessanalyzer.types.unused_access_findings_statistics.UnusedAccessFindingsStatistics"


FindingsStatistics: TypeAlias = (
    _FindingsStatistics_externalAccessFindingsStatistics
    | _FindingsStatistics_internalAccessFindingsStatistics
    | _FindingsStatistics_unusedAccessFindingsStatistics
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: FindingsStatistics) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"FindingsStatistics: cannot serialize unknown variant {value.name!r}"
        )
    elif "externalAccessFindingsStatistics" in value:
        import capo_accessanalyzer.types.external_access_findings_statistics

        return {
            "externalAccessFindingsStatistics": capo_accessanalyzer.types.external_access_findings_statistics.serialize_json(
                value["externalAccessFindingsStatistics"]
            )
        }
    elif "internalAccessFindingsStatistics" in value:
        import capo_accessanalyzer.types.internal_access_findings_statistics

        return {
            "internalAccessFindingsStatistics": capo_accessanalyzer.types.internal_access_findings_statistics.serialize_json(
                value["internalAccessFindingsStatistics"]
            )
        }
    elif "unusedAccessFindingsStatistics" in value:
        import capo_accessanalyzer.types.unused_access_findings_statistics

        return {
            "unusedAccessFindingsStatistics": capo_accessanalyzer.types.unused_access_findings_statistics.serialize_json(
                value["unusedAccessFindingsStatistics"]
            )
        }
    else:
        raise SerializationError("FindingsStatistics: no variant present")


def deserialize_json(data: dict) -> FindingsStatistics:
    if data.get("externalAccessFindingsStatistics") is not None:
        import capo_accessanalyzer.types.external_access_findings_statistics

        return {
            "externalAccessFindingsStatistics": capo_accessanalyzer.types.external_access_findings_statistics.deserialize_json(
                data["externalAccessFindingsStatistics"]
            )
        }
    elif data.get("internalAccessFindingsStatistics") is not None:
        import capo_accessanalyzer.types.internal_access_findings_statistics

        return {
            "internalAccessFindingsStatistics": capo_accessanalyzer.types.internal_access_findings_statistics.deserialize_json(
                data["internalAccessFindingsStatistics"]
            )
        }
    elif data.get("unusedAccessFindingsStatistics") is not None:
        import capo_accessanalyzer.types.unused_access_findings_statistics

        return {
            "unusedAccessFindingsStatistics": capo_accessanalyzer.types.unused_access_findings_statistics.deserialize_json(
                data["unusedAccessFindingsStatistics"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("FindingsStatistics: no recognized variant key")
