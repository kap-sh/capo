"""Generated from Smithy shape ``com.amazonaws.emrcontainers#ListJobTemplatesResponse``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_emr_containers.types.job_templates
    import capo_emr_containers.types.next_token


class ListJobTemplatesResponse(TypedDict, closed=True):
    templates: NotRequired["capo_emr_containers.types.job_templates.JobTemplates"]
    """<p>This output lists information about the specified job templates.</p>"""
    next_token: NotRequired["capo_emr_containers.types.next_token.NextToken"]
    """<p> This output displays the token for the next set of job templates.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListJobTemplatesResponse) -> dict:
    out: dict = {}
    if "templates" in value:
        import capo_emr_containers.types.job_templates

        out["templates"] = capo_emr_containers.types.job_templates.serialize_json(
            value["templates"]
        )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListJobTemplatesResponse:
    out: ListJobTemplatesResponse = {}  # type: ignore[typeddict-item]
    if data.get("templates") is not None:
        import capo_emr_containers.types.job_templates

        out["templates"] = capo_emr_containers.types.job_templates.deserialize_json(
            data["templates"]
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out


def redact_sensitive(value: ListJobTemplatesResponse) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "templates" in value:
        import capo_emr_containers.types.job_templates

        out["templates"] = capo_emr_containers.types.job_templates.redact_sensitive(
            value["templates"]
        )
    return out
