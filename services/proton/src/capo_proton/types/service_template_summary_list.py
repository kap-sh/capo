"""Generated from Smithy shape ``com.amazonaws.proton#ServiceTemplateSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.service_template_summary

ServiceTemplateSummaryList: TypeAlias = list[
    "capo_proton.types.service_template_summary.ServiceTemplateSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceTemplateSummaryList) -> list:
    import capo_proton.types.service_template_summary

    out: list = []
    for item in value:
        out.append(
            capo_proton.types.service_template_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceTemplateSummaryList:
    import capo_proton.types.service_template_summary

    out: ServiceTemplateSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_proton.types.service_template_summary.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: ServiceTemplateSummaryList) -> list[Any]:
    import capo_proton.types.service_template_summary

    return [
        capo_proton.types.service_template_summary.redact_sensitive(item)
        for item in value
    ]
