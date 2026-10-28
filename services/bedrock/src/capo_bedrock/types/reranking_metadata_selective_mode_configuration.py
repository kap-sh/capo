"""Generated from Smithy shape ``com.amazonaws.bedrock#RerankingMetadataSelectiveModeConfiguration``."""

from typing import TYPE_CHECKING, Any, TypeAlias

from typing_extensions import TypedDict

from capo_bedrock.errors import DeserializationError, SerializationError
from capo_bedrock.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_bedrock.types.fields_for_reranking


class RerankingMetadataSelectiveModeConfigurationFieldsToIncludeMember(
    TypedDict, closed=True
):
    fieldsToInclude: "capo_bedrock.types.fields_for_reranking.FieldsForReranking"


class RerankingMetadataSelectiveModeConfigurationFieldsToExcludeMember(
    TypedDict, closed=True
):
    fieldsToExclude: "capo_bedrock.types.fields_for_reranking.FieldsForReranking"


RerankingMetadataSelectiveModeConfiguration: TypeAlias = (
    RerankingMetadataSelectiveModeConfigurationFieldsToIncludeMember
    | RerankingMetadataSelectiveModeConfigurationFieldsToExcludeMember
    | UnknownUnionMember
)


# --- restJson1 ser/de ---
def serialize_json(value: RerankingMetadataSelectiveModeConfiguration) -> dict:
    if "$unknown" in value:
        raise SerializationError(
            f"RerankingMetadataSelectiveModeConfiguration: cannot serialize unknown variant {value['$unknown']['name']!r}"
        )
    elif "fieldsToInclude" in value:
        import capo_bedrock.types.fields_for_reranking

        return {
            "fieldsToInclude": capo_bedrock.types.fields_for_reranking.serialize_json(
                value["fieldsToInclude"]
            )
        }
    elif "fieldsToExclude" in value:
        import capo_bedrock.types.fields_for_reranking

        return {
            "fieldsToExclude": capo_bedrock.types.fields_for_reranking.serialize_json(
                value["fieldsToExclude"]
            )
        }
    else:
        raise SerializationError(
            "RerankingMetadataSelectiveModeConfiguration: no variant present"
        )


def deserialize_json(data: dict) -> RerankingMetadataSelectiveModeConfiguration:
    if data.get("fieldsToInclude") is not None:
        import capo_bedrock.types.fields_for_reranking

        return {
            "fieldsToInclude": capo_bedrock.types.fields_for_reranking.deserialize_json(
                data["fieldsToInclude"]
            )
        }
    elif data.get("fieldsToExclude") is not None:
        import capo_bedrock.types.fields_for_reranking

        return {
            "fieldsToExclude": capo_bedrock.types.fields_for_reranking.deserialize_json(
                data["fieldsToExclude"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return {"$unknown": {"name": name}}
        raise DeserializationError(
            "RerankingMetadataSelectiveModeConfiguration: no recognized variant key"
        )


def redact_sensitive(
    value: RerankingMetadataSelectiveModeConfiguration,
) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "fieldsToInclude" in value:
        out["fieldsToInclude"] = "*** Sensitive Data Redacted ***"
    if "fieldsToExclude" in value:
        out["fieldsToExclude"] = "*** Sensitive Data Redacted ***"
    return out
