"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceTemplatesOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.next_token
    import capo_proton.types.service_template_summary_list


class ListServiceTemplatesOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next service template in the array of service templates, after the current requested list of service templates.</p>"""
    templates: (
        "capo_proton.types.service_template_summary_list.ServiceTemplateSummaryList"
    )
    """<p>An array of service templates with detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceTemplatesOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.service_template_summary_list

    out["templates"] = (
        capo_proton.types.service_template_summary_list.serialize_aws_json_1_0(
            value["templates"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceTemplatesOutput:
    out: ListServiceTemplatesOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("templates") is not None:
        import capo_proton.types.service_template_summary_list

        out["templates"] = (
            capo_proton.types.service_template_summary_list.deserialize_aws_json_1_0(
                data["templates"]
            )
        )
    else:
        out["templates"] = []
    return out


def redact_sensitive(value: ListServiceTemplatesOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "templates" in value:
        import capo_proton.types.service_template_summary_list

        out["templates"] = (
            capo_proton.types.service_template_summary_list.redact_sensitive(
                value["templates"]
            )
        )
    return out
