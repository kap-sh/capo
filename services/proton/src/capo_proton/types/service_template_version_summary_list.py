"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateVersionSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.service_template_version_summary

ServiceTemplateVersionSummaryList: TypeAlias = list[
    "capo_proton.types.service_template_version_summary.ServiceTemplateVersionSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateVersionSummaryList) -> list:
    import capo_proton.types.service_template_version_summary

    out: list = []
    for item in value:
        out.append(
            capo_proton.types.service_template_version_summary.serialize_aws_json_1_0(
                item
            )
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceTemplateVersionSummaryList:
    import capo_proton.types.service_template_version_summary

    out: ServiceTemplateVersionSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_proton.types.service_template_version_summary.deserialize_aws_json_1_0(
                item
            )
        )
    return out


def redact_sensitive(value: ServiceTemplateVersionSummaryList) -> list[Any]:
    import capo_proton.types.service_template_version_summary

    return [
        capo_proton.types.service_template_version_summary.redact_sensitive(item)
        for item in value
    ]
