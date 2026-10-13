"""Generated from Smithy shape ``com.amazonaws.proton#ListEnvironmentTemplateVersionsOutput``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

from capo_proton.errors import DeserializationError

if TYPE_CHECKING:
    import capo_proton.types.environment_template_version_summary_list
    import capo_proton.types.next_token


class ListEnvironmentTemplateVersionsOutput(TypedDict, closed=True):
    next_token: NotRequired["capo_proton.types.next_token.NextToken"]
    """<p>A token that indicates the location of the next major or minor version in the array of major or minor versions of an environment template, after the list of major or minor versions that was previously requested.</p>"""
    template_versions: "capo_proton.types.environment_template_version_summary_list.EnvironmentTemplateVersionSummaryList"
    """<p>An array of major or minor versions of an environment template detail data.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ListEnvironmentTemplateVersionsOutput) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_proton.types.environment_template_version_summary_list

    out["templateVersions"] = (
        capo_proton.types.environment_template_version_summary_list.serialize_aws_json_1_0(
            value["template_versions"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ListEnvironmentTemplateVersionsOutput:
    out: ListEnvironmentTemplateVersionsOutput = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("templateVersions") is not None:
        import capo_proton.types.environment_template_version_summary_list

        out["template_versions"] = (
            capo_proton.types.environment_template_version_summary_list.deserialize_aws_json_1_0(
                data["templateVersions"]
            )
        )
    else:
        raise DeserializationError(
            "ListEnvironmentTemplateVersionsOutput.template_versions required"
        )
    return out


def redact_sensitive(value: ListEnvironmentTemplateVersionsOutput) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "template_versions" in value:
        import capo_proton.types.environment_template_version_summary_list

        out["template_versions"] = (
            capo_proton.types.environment_template_version_summary_list.redact_sensitive(
                value["template_versions"]
            )
        )
    return out
