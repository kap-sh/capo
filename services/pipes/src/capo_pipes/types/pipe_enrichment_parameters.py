"""Generated from Smithy shape ``com.amazonaws.pipes#PipeEnrichmentParameters``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_pipes.types.input_template
    import capo_pipes.types.pipe_enrichment_http_parameters


class PipeEnrichmentParameters(TypedDict, closed=True):
    input_template: NotRequired["capo_pipes.types.input_template.InputTemplate"]
    """<p>Valid JSON text passed to the enrichment. In this case, nothing from the event itself is passed to the enrichment. For more information, see <a href="http://www.rfc-editor.org/rfc/rfc7159.txt">The JavaScript Object Notation (JSON) Data Interchange Format</a>.</p> <p>To remove an input template, specify an empty string.</p>"""
    http_parameters: NotRequired[
        "capo_pipes.types.pipe_enrichment_http_parameters.PipeEnrichmentHttpParameters"
    ]
    """<p>Contains the HTTP parameters to use when the target is a API Gateway REST endpoint or EventBridge ApiDestination.</p> <p>If you specify an API Gateway REST API or EventBridge ApiDestination as a target, you can use this parameter to specify headers, path parameters, and query string keys/values as part of your target invoking request. If you're using ApiDestinations, the corresponding Connection can also have these values configured. In case of any conflicting keys, values from the Connection take precedence.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: PipeEnrichmentParameters) -> dict:
    out: dict = {}
    if "input_template" in value:
        out["InputTemplate"] = value["input_template"]
    if "http_parameters" in value:
        import capo_pipes.types.pipe_enrichment_http_parameters

        out["HttpParameters"] = (
            capo_pipes.types.pipe_enrichment_http_parameters.serialize_json(
                value["http_parameters"]
            )
        )
    return out


def deserialize_json(data: dict) -> PipeEnrichmentParameters:
    out: PipeEnrichmentParameters = {}  # type: ignore[typeddict-item]
    if data.get("InputTemplate") is not None:
        out["input_template"] = data["InputTemplate"]
    if data.get("HttpParameters") is not None:
        import capo_pipes.types.pipe_enrichment_http_parameters

        out["http_parameters"] = (
            capo_pipes.types.pipe_enrichment_http_parameters.deserialize_json(
                data["HttpParameters"]
            )
        )
    return out
