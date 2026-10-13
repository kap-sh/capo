"""Generated from Smithy shape ``com.amazonaws.proton#ServiceSummaryList``."""

from typing import TYPE_CHECKING, Any, TypeAlias

if TYPE_CHECKING:
    import capo_proton.types.service_summary

ServiceSummaryList: TypeAlias = list["capo_proton.types.service_summary.ServiceSummary"]


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ServiceSummaryList) -> list:
    import capo_proton.types.service_summary

    out: list = []
    for item in value:
        out.append(capo_proton.types.service_summary.serialize_aws_json_1_0(item))
    return out


def deserialize_aws_json_1_0(data: list) -> ServiceSummaryList:
    import capo_proton.types.service_summary

    out: ServiceSummaryList = []
    for item in data:
        if item is None:
            continue
        out.append(capo_proton.types.service_summary.deserialize_aws_json_1_0(item))
    return out


def redact_sensitive(value: ServiceSummaryList) -> list[Any]:
    import capo_proton.types.service_summary

    return [capo_proton.types.service_summary.redact_sensitive(item) for item in value]
