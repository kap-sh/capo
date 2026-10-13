"""Generated from Smithy shape ``com.amazonaws.proton#EnvironmentTemplateSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.environment_template_summary

EnvironmentTemplateSummaryList: TypeAlias = list[
    "capo_proton.types.environment_template_summary.EnvironmentTemplateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EnvironmentTemplateSummaryList) -> list:
    import capo_proton.types.environment_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_proton.types.environment_template_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> EnvironmentTemplateSummaryList:
    import capo_proton.types.environment_template_summary

    out: EnvironmentTemplateSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_proton.types.environment_template_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: EnvironmentTemplateSummaryList) -> list[Any]:
    import capo_proton.types.environment_template_summary

    return [
        capo_proton.types.environment_template_summary.redact_sensitive(item)
        for item in value
    ]
