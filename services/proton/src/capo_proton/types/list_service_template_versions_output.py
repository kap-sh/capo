"""Generated from Smithy shape ``com.amazonaws.proton#ListServiceTemplateVersionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_proton.types.next_token
    import capo_proton.types.service_template_version_summary_list


class ListServiceTemplateVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next major or minor version in the array of major or minor versions of a service template, after the current requested list of service major or minor versions.</p>"""
    template_versions: "capo_proton.types.service_template_version_summary_list.ServiceTemplateVersionSummaryList"
    """<p>An array of major or minor versions of a service template with detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListServiceTemplateVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.service_template_version_summary_list

    out["templateVersions"] = (
        capo_proton.types.service_template_version_summary_list.serialize_aws_json_1_0(
            value["template_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListServiceTemplateVersionsOutput:
    out: ListServiceTemplateVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("templateVersions") is not None:
        import capo_proton.types.service_template_version_summary_list

        out["template_versions"] = (
            capo_proton.types.service_template_version_summary_list.deserialize_aws_json_1_0(
                data["templateVersions"]
            )
        )
    else:
        out["template_versions"] = []
    return out


def redact_sensitive(value: ListServiceTemplateVersionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template_versions" in value:
        import capo_proton.types.service_template_version_summary_list

        out["template_versions"] = (
            capo_proton.types.service_template_version_summary_list.redact_sensitive(
                value["template_versions"]
            )
        )
    return out
