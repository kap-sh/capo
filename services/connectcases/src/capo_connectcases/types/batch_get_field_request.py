"""Generated from Smithy shape ``com.amazonaws.connectcases#BatchGetFieldRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_connectcases.types.batch_get_field_identifier_list
    import capo_connectcases.types.domain_id


class BatchGetFieldRequest(TypedDict, closed=True):
    domain_id: "capo_connectcases.types.domain_id.DomainId"
    """<p>The unique identifier of the Cases domain. </p>"""
    fields: "capo_connectcases.types.batch_get_field_identifier_list.BatchGetFieldIdentifierList"
    """<p>A list of unique field identifiers. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetFieldRequest) -> dict:
    out: dict = {}
    import capo_connectcases.types.batch_get_field_identifier_list

    out["fields"] = (
        capo_connectcases.types.batch_get_field_identifier_list.serialize_json(
            value["fields"]
        )
    )
    return out


def deserialize_json(data: dict) -> BatchGetFieldRequest:
    out: BatchGetFieldRequest = {}  # type: ignore[typeddict-item]
    if data.get("fields") is not None:
        import capo_connectcases.types.batch_get_field_identifier_list

        out["fields"] = (
            capo_connectcases.types.batch_get_field_identifier_list.deserialize_json(
                data["fields"]
            )
        )
    else:
        out["fields"] = []
    return out
