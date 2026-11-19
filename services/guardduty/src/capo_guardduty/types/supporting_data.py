"""Generated from Smithy shape ``com.amazonaws.guardduty#SupportingData``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_guardduty.errors import DeserializationError, SerializationError
from capo_guardduty.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_guardduty.types.analysis_record
    import capo_guardduty.types.fetch_record
    import capo_guardduty.types.metadata_record
    import capo_guardduty.types.observation_record


class SupportingDataFetchMember(TypedDict, closed=True):
    Fetch: "capo_guardduty.types.fetch_record.FetchRecord"


class SupportingDataAnalysisMember(TypedDict, closed=True):
    Analysis: "capo_guardduty.types.analysis_record.AnalysisRecord"


class SupportingDataObservationMember(TypedDict, closed=True):
    Observation: "capo_guardduty.types.observation_record.ObservationRecord"


class SupportingDataMetadataMember(TypedDict, closed=True):
    Metadata: "capo_guardduty.types.metadata_record.MetadataRecord"


SupportingData: TypeAlias = (
    SupportingDataFetchMember
    | SupportingDataAnalysisMember
    | SupportingDataObservationMember
    | SupportingDataMetadataMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: SupportingData) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"SupportingData: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "Fetch" in value:
        import capo_guardduty.types.fetch_record

        return {
            "fetch": capo_guardduty.types.fetch_record.serialize_json(value["Fetch"])
        }
    elif "Analysis" in value:
        import capo_guardduty.types.analysis_record

        return {
            "analysis": capo_guardduty.types.analysis_record.serialize_json(
                value["Analysis"]
            )
        }
    elif "Observation" in value:
        import capo_guardduty.types.observation_record

        return {
            "observation": capo_guardduty.types.observation_record.serialize_json(
                value["Observation"]
            )
        }
    elif "Metadata" in value:
        import capo_guardduty.types.metadata_record

        return {
            "metadata": capo_guardduty.types.metadata_record.serialize_json(
                value["Metadata"]
            )
        }
    else:
        raise SerializationError("SupportingData: no variant present")


def deserialize_json(data: dict) -> SupportingData:
    if data.get("fetch") is not None:
        import capo_guardduty.types.fetch_record

        return {
            "Fetch": capo_guardduty.types.fetch_record.deserialize_json(data["fetch"])
        }
    elif data.get("analysis") is not None:
        import capo_guardduty.types.analysis_record

        return {
            "Analysis": capo_guardduty.types.analysis_record.deserialize_json(
                data["analysis"]
            )
        }
    elif data.get("observation") is not None:
        import capo_guardduty.types.observation_record

        return {
            "Observation": capo_guardduty.types.observation_record.deserialize_json(
                data["observation"]
            )
        }
    elif data.get("metadata") is not None:
        import capo_guardduty.types.metadata_record

        return {
            "Metadata": capo_guardduty.types.metadata_record.deserialize_json(
                data["metadata"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError("SupportingData: no recognized variant key")


def redact_sensitive(value: SupportingData) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "Fetch" in value:
        import capo_guardduty.types.fetch_record

        out["Fetch"] = capo_guardduty.types.fetch_record.redact_sensitive(
            value["Fetch"]
        )
    if "Analysis" in value:
        import capo_guardduty.types.analysis_record

        out["Analysis"] = capo_guardduty.types.analysis_record.redact_sensitive(
            value["Analysis"]
        )
    if "Observation" in value:
        import capo_guardduty.types.observation_record

        out["Observation"] = capo_guardduty.types.observation_record.redact_sensitive(
            value["Observation"]
        )
    return out
