"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#UpdateTemplateResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.string_map


class UpdateTemplateResponse(TypedDict, closed=True):
    template_id: NotRequired["str"]
    """<p>The ID of the migration workflow template being updated.</p>"""
    template_arn: NotRequired["str"]
    """<p>The ARN of the migration workflow template being updated. The format for an Migration Hub Orchestrator template ARN is <code>arn:aws:migrationhub-orchestrator:region:account:template/template-abcd1234</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html">Amazon Resource Names (ARNs)</a> in the <i>AWS General Reference</i>.</p>"""
    tags: NotRequired["capo_migrationhuborchestrator.types.string_map.StringMap"]
    """<p>The tags added to the migration workflow template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateTemplateResponse) -> dict:
    out: dict = {}
    if "template_id" in value:
        out["templateId"] = value["template_id"]
    if "template_arn" in value:
        out["templateArn"] = value["template_arn"]
    if "tags" in value:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> UpdateTemplateResponse:
    out: UpdateTemplateResponse = {}  # type: ignore[typeddict-item]
    if data.get("templateId") is not None:
        out["template_id"] = data["templateId"]
    if data.get("templateArn") is not None:
        out["template_arn"] = data["templateArn"]
    if data.get("tags") is not None:
        import capo_migrationhuborchestrator.types.string_map

        out["tags"] = capo_migrationhuborchestrator.types.string_map.deserialize_json(
            data["tags"]
        )
    return out
