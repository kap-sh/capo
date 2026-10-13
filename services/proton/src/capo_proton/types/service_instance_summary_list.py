"""Generated from Smithy shape ``com.amazonaws.proton#ServiceInstanceSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.service_instance_summary

ServiceInstanceSummaryList: TypeAlias = list[
    "capo_proton.types.service_instance_summary.ServiceInstanceSummary"
]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceInstanceSummaryList) -> list:
    import capo_proton.types.service_instance_summary

    out: list = []
    for item in value:
        out.append(
            capo_proton.types.service_instance_summary.serialize_aws_json_1_0(item)
        )
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceInstanceSummaryList:
    import capo_proton.types.service_instance_summary

    out: ServiceInstanceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(
            capo_proton.types.service_instance_summary.deserialize_aws_json_1_0(item)
        )
    return out


def redact_sensitive(value: ServiceInstanceSummaryList) -> list[Any]:
    import capo_proton.types.service_instance_summary

    return [
        capo_proton.types.service_instance_summary.redact_sensitive(item)
        for item in value
    ]
