"""Generated from Smithy shape ``com.amazonaws.appsync#EvaluateMappingTemplateRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.context
    import capo_appsync.types.template


class EvaluateMappingTemplateRequest(TypedDict, closed=True):
    template: "capo_appsync.types.template.Template"
    """<p>The mapping template; this can be a request or response template. A <code>template</code> is required for this action.</p>"""
    context: "capo_appsync.types.context.Context"
    """<p>The map that holds all of the contextual information for your resolver invocation. A <code>context</code> is required for this action.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EvaluateMappingTemplateRequest) -> dict:
    out: dict = {}
    out["template"] = value["template"]
    out["context"] = value["context"]
    return out


def deserialize_json(data: dict) -> EvaluateMappingTemplateRequest:
    out: EvaluateMappingTemplateRequest = {}  # type: ignore[typeddict-item]
    if data.get("template") is not None:
        out["template"] = data["template"]
    else:
        out["template"] = ""
    if data.get("context") is not None:
        out["context"] = data["context"]
    else:
        out["context"] = ""
    return out
