"""Generated from Smithy shape ``com.amazonaws.migrationhuborchestrator#CreateTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_migrationhuborchestrator.errors import DeserializationError

if TYPE_CHECKING:
    import capo_migrationhuborchestrator.types.client_token
    import capo_migrationhuborchestrator.types.tag_map
    import capo_migrationhuborchestrator.types.template_source


class CreateTemplateRequest(TypedDict, closed=True):
    template_name: "str"
    """<p>The name of the migration workflow template.</p>"""
    template_description: NotRequired["str"]
    """<p>A description of the migration workflow template.</p>"""
    template_source: (
        "capo_migrationhuborchestrator.types.template_source.TemplateSource"
    )
    """<p>The source of the migration workflow template.</p>"""
    client_token: NotRequired[
        "capo_migrationhuborchestrator.types.client_token.ClientToken"
    ]
    """<p>A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see <a href="https://smithy.io/2.0/spec/behavior-traits.html#idempotencytoken-trait">Idempotency</a> in the Smithy documentation.</p>"""
    tags: NotRequired["capo_migrationhuborchestrator.types.tag_map.TagMap"]
    """<p>The tags to add to the migration workflow template.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateTemplateRequest) -> dict:
    out: dict = {}
    out["templateName"] = value["template_name"]
    if "template_description" in value:
        out["templateDescription"] = value["template_description"]
    import capo_migrationhuborchestrator.types.template_source

    out["templateSource"] = (
        capo_migrationhuborchestrator.types.template_source.serialize_json(
            value["template_source"]
        )
    )
    if "client_token" in value:
        out["clientToken"] = value["client_token"]
    if "tags" in value:
        import capo_migrationhuborchestrator.types.tag_map

        out["tags"] = capo_migrationhuborchestrator.types.tag_map.serialize_json(
            value["tags"]
        )
    return out


def deserialize_json(data: dict) -> CreateTemplateRequest:
    out: CreateTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("templateName") is not None:
        out["template_name"] = data["templateName"]
    else:
        raise DeserializationError("CreateTemplateRequest.template_name required")
    if data.get("templateDescription") is not None:
        out["template_description"] = data["templateDescription"]
    if data.get("templateSource") is not None:
        import capo_migrationhuborchestrator.types.template_source

        out["template_source"] = (
            capo_migrationhuborchestrator.types.template_source.deserialize_json(
                data["templateSource"]
            )
        )
    else:
        raise DeserializationError("CreateTemplateRequest.template_source required")
    if data.get("clientToken") is not None:
        out["client_token"] = data["clientToken"]
    if data.get("tags") is not None:
        import capo_migrationhuborchestrator.types.tag_map

        out["tags"] = capo_migrationhuborchestrator.types.tag_map.deserialize_json(
            data["tags"]
        )
    return out
