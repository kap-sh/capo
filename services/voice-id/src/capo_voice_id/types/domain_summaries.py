"""Generated from Smithy shape ``com.amazonaws.voiceid#DomainSummaries``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_voice_id.types.domain_summary

DomainSummaries: TypeAlias = list["capo_voice_id.types.domain_summary.DomainSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DomainSummaries) -> list:
    import capo_voice_id.types.domain_summary

    out: list = []
    for item in value:
        out.append(capo_voice_id.types.domain_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> DomainSummaries:
    import capo_voice_id.types.domain_summary

    out: DomainSummaries = []
    for item in data:
        if item is None:
            continue
        out.append(capo_voice_id.types.domain_summary.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: DomainSummaries) -> list[Any]:
    import capo_voice_id.types.domain_summary

    return [capo_voice_id.types.domain_summary.redact_sensitive(item) for item in value]
