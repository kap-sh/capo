"""Generated from Smithy shape ``com.amazonaws.cleanrooms#BatchGetSchemaInput``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.collaboration_identifier
    import capo_cleanrooms.types.table_alias_list


class BatchGetSchemaInput(TypedDict, closed=True):
    collaboration_identifier: (
        "capo_cleanrooms.types.collaboration_identifier.CollaborationIdentifier"
    )
    """<p>A unique identifier for the collaboration that the schemas belong to. Currently accepts collaboration ID.</p>"""
    names: "capo_cleanrooms.types.table_alias_list.TableAliasList"
    """<p>The names for the schema objects to retrieve.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: BatchGetSchemaInput) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.table_alias_list

    out["names"] = capo_cleanrooms.types.table_alias_list.serialize_json(value["names"])
    return out


def deserialize_json(data: dict) -> BatchGetSchemaInput:
    out: BatchGetSchemaInput = {}  # type: ignore[typeddict-item]
    if data.get("names") is not None:
        import capo_cleanrooms.types.table_alias_list

        out["names"] = capo_cleanrooms.types.table_alias_list.deserialize_json(
            data["names"]
        )
    else:
        out["names"] = []
    return out
