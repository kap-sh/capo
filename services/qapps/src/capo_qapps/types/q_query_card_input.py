"""Generated from Smithy shape ``com.amazonaws.qapps#QQueryCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_qapps.types.attribute_filter
    import capo_qapps.types.card_output_source
    import capo_qapps.types.card_type
    import capo_qapps.types.prompt
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class QQueryCardInput(TypedDict, closed=True):
    title: "capo_qapps.types.title.Title"
    """<p>The title or label of the query card.</p>"""
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the query card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    prompt: "capo_qapps.types.prompt.Prompt"
    """<p>The prompt or instructions displayed for the query card.</p>"""
    output_source: "capo_qapps.types.card_output_source.CardOutputSource"
    """<p>The source or type of output to generate for the query card.</p>"""
    attribute_filter: NotRequired["capo_qapps.types.attribute_filter.AttributeFilter"]
    """<p>Turns on filtering of responses based on document attributes or metadata fields.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QQueryCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(
        value.get("type", "q-query")
    )
    out["prompt"] = value["prompt"]
    import capo_qapps.types.card_output_source

    out["outputSource"] = capo_qapps.types.card_output_source.serialize_json(
        value.get("output_source", "approved-sources")
    )
    if "attribute_filter" in value:
        import capo_qapps.types.attribute_filter

        out["attributeFilter"] = capo_qapps.types.attribute_filter.serialize_json(
            value["attribute_filter"]
        )
    return out


def deserialize_json(data: dict) -> QQueryCardInput:
    out: QQueryCardInput = {}  # type: ignore[typeddict-item]
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        out["type"] = "q-query"
    if data.get("prompt") is not None:
        out["prompt"] = data["prompt"]
    else:
        out["prompt"] = ""
    if data.get("outputSource") is not None:
        import capo_qapps.types.card_output_source

        out["output_source"] = capo_qapps.types.card_output_source.deserialize_json(
            data["outputSource"]
        )
    else:
        out["output_source"] = "approved-sources"
    if data.get("attributeFilter") is not None:
        import capo_qapps.types.attribute_filter

        out["attribute_filter"] = capo_qapps.types.attribute_filter.deserialize_json(
            data["attributeFilter"]
        )
    return out
