"""Generated from Smithy shape ``com.amazonaws.proton#ListServicesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.next_token
    import capo_proton.types.service_summary_list


class ListServicesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service in the array of services, after the current requested list of services.</p>"""
    services: "capo_proton.types.service_summary_list.ServiceSummaryList"
    """<p>An array of services with summaries of detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServicesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.service_summary_list

    out["services"] = capo_proton.types.service_summary_list.serialize_aws_json_1_0(
        value["services"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServicesOutput:
    out: ListServicesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("services") is not None:
        import capo_proton.types.service_summary_list

        out["services"] = (
            capo_proton.types.service_summary_list.deserialize_aws_json_1_0(
                data["services"]
            )
        )
    else:
        out["services"] = []
    return out


def redact_sensitive(value: ListServicesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "services" in value:
        import capo_proton.types.service_summary_list

        out["services"] = capo_proton.types.service_summary_list.redact_sensitive(
            value["services"]
        )
    return out
