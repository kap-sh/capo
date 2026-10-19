"""Generated from Smithy shape ``com.amazonaws.qapps#FormInputCard``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_qapps.errors import DeserializationError

if TYPE_CHECKING:
    import capo_qapps.types.card_type
    import capo_qapps.types.dependency_list
    import capo_qapps.types.form_input_card_metadata
    import capo_qapps.types.input_card_compute_mode
    import capo_qapps.types.title
    import capo_qapps.types.uuid


class FormInputCard(TypedDict, closed=True):
    id: "capo_qapps.types.uuid.UUID"
    """<p>The unique identifier of the form input card.</p>"""
    title: "capo_qapps.types.title.Title"
    """<p>The title of the form input card.</p>"""
    dependencies: "capo_qapps.types.dependency_list.DependencyList"
    """<p>Any dependencies or requirements for the form input card.</p>"""
    type: "capo_qapps.types.card_type.CardType"
    """<p>The type of the card.</p>"""
    metadata: "capo_qapps.types.form_input_card_metadata.FormInputCardMetadata"
    """<p>The metadata that defines the form input card data.</p>"""
    compute_mode: NotRequired[
        "capo_qapps.types.input_card_compute_mode.InputCardComputeMode"
    ]
    """<p>The compute mode of the form input card. This property determines whether individual participants of a data collection session can submit multiple response or one response. A compute mode of <code>append</code> shall allow participants to submit the same form multiple times with different values. A compute mode of <code>replace</code>code&gt; shall overwrite the current value for each participant.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: FormInputCard) -> dict:
    out: dict = {}
    out["id"] = value["id"]
    out["title"] = value["title"]
    import capo_qapps.types.dependency_list

    out["dependencies"] = capo_qapps.types.dependency_list.serialize_json(
        value["dependencies"]
    )
    import capo_qapps.types.card_type

    out["type"] = capo_qapps.types.card_type.serialize_json(value["type"])
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


def deserialize_json(data: dict) -> FormInputCard:
    out: FormInputCard = {}  # type: ignore[typeddict-item]
    if data.get("id") is not None:
        out["id"] = data["id"]
    else:
        out["id"] = ""
    if data.get("title") is not None:
        out["title"] = data["title"]
    else:
        out["title"] = ""
    if data.get("dependencies") is not None:
        import capo_qapps.types.dependency_list

        out["dependencies"] = capo_qapps.types.dependency_list.deserialize_json(
            data["dependencies"]
        )
    else:
        out["dependencies"] = []
    if data.get("type") is not None:
        import capo_qapps.types.card_type

        out["type"] = capo_qapps.types.card_type.deserialize_json(data["type"])
    else:
        import typing

        out["type"] = typing.cast("capo_qapps.types.card_type.CardType", "")
    if data.get("metadata") is not None:
        import capo_qapps.types.form_input_card_metadata

        out["metadata"] = capo_qapps.types.form_input_card_metadata.deserialize_json(
            data["metadata"]
        )
    else:
        raise DeserializationError("FormInputCard.metadata required")
    if data.get("computeMode") is not None:
        import capo_qapps.types.input_card_compute_mode

        out["compute_mode"] = capo_qapps.types.input_card_compute_mode.deserialize_json(
            data["computeMode"]
        )
    return out
