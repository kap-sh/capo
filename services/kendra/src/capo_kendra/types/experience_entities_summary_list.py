"""Generated from Smithy shape ``com.amazonaws.kendra#ExperienceEntitiesSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_kendra.types.experience_entities_summary

ExperienceEntitiesSummaryList: TypeAlias = list[
    "capo_kendra.types.experience_entities_summary.ExperienceEntitiesSummary"
]


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ExperienceEntitiesSummaryList) -> list:
    import capo_kendra.types.experience_entities_summary

    out: list = []
    for item in value:
        out.append(
            capo_kendra.types.experience_entities_summary.serialize_aws_json_1_1(item)
        )
    return out


def deserialize_aws_json_1_1(data: list) -> ExperienceEntitiesSummaryList:
    import capo_kendra.types.experience_entities_summary

    out: ExperienceEntitiesSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_kendra.types.experience_entities_summary.deserialize_aws_json_1_1(item)
        )
    return out


def redact_sensitive(value: ExperienceEntitiesSummaryList) -> list[Any]:
    import capo_kendra.types.experience_entities_summary

    return [
        capo_kendra.types.experience_entities_summary.redact_sensitive(item)
        for item in value
    ]
