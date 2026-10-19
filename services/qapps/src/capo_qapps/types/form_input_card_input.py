"""Generated from Smithy shape ``com.amazonaws.qapps#FormInputCardInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.card_type
    import capo_qapps.types.form_input_card_metadata
    import capo_qapps.types.input_card_compute_mode
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class FormInputCardInput(TypedDict, closed=True):
    title: "capo_qapps.types.title.Title"
    """<p>The title or label of the form input card.</p>"""
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the form input card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    metadata: "capo_qapps.types.form_input_card_metadata.FormInputCardMetadata"
    """<p>The metadata that defines the form input card data.</p>"""
    compute_mode: NotRequired[
        "capo_qapps.types.input_card_compute_mode.InputCardComputeMode"
    ]
    """<p>The compute mode of the form input card. This property determines whether individual participants of a data collection session can submit multiple response or one response. A compute mode of <code>append</code> shall allow participants to submit the same form multiple times with different values. A compute mode of <code>replace</code>code&gt; shall overwrite the current value for each participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputCardInput) -> dict:
    out: dict = {}
    out["title"] = value["title"]
    out["id"] = value["id"]
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(
        value.get("type", "form-input")
    )
    import capo_qapps.types.form_input_card_metadata

    out["metadata"] = capo_qapps.types.form_input_card_metadata.serialize_json(
        value["metadata"]
    )
    if "compute_mode" in value:
        import capo_qapps.types.input_card_compute_mode

        out["computeMode"] = capo_qapps.types.input_card_compute_mode.serialize_json(
            value["compute_mode"]
        )
    return out


def deserialize_json(data: dict) -> FormInputCardInput:
    out: FormInputCardInput = {}  # type: ignore[typeddict-item]
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
        out["type"] = "form-input"
    if data.get("metadata") is not None:
        import capo_qapps.types.form_input_card_metadata

        out["metadata"] = capo_qapps.types.form_input_card_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("FormInputCardInput.metadata required")
    if data.get("computeMode") is not None:
        import capo_qapps.types.input_card_compute_mode

        out["compute_mode"] = capo_qapps.types.input_card_compute_mode.deserialize_json(
            data["computeMode"]
        )
    return out
