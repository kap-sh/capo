"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchPutFieldOptionsRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.domain_id
    import capo_connectcases.types.field_id
    import capo_connectcases.types.field_options_list


class BatchPutFieldOptionsRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    field_id: "capo_connectcases.types.field_id.FieldId"
    """<p>The unique identifier of a field.</p>"""
    options: "capo_connectcases.types.field_options_list.FieldOptionsList"
    """<p>A list of <code>FieldOption</code> objects.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchPutFieldOptionsRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.field_options_list

    out["options"] = capo_connectcases.types.field_options_list.serialize_json(
        value["options"]
    )
    return out


def deserialize_json(data: dict) -> BatchPutFieldOptionsRequest:
    out: BatchPutFieldOptionsRequest = {}  # type: ignore[typeddict-item]
    if data.get("options") is not None:
        import capo_connectcases.types.field_options_list

        out["options"] = capo_connectcases.types.field_options_list.deserialize_json(
            data["options"]
        )
    else:
        out["options"] = []
    return out
