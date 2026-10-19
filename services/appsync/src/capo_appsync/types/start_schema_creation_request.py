"""Generated from Smithy shape ``com.amazonaws.appsync#StartSchemaCreationRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_appsync.types.blob
    import capo_appsync.types.string


class StartSchemaCreationRequest(TypedDict, closed=True):
    api_id: "capo_appsync.types.string.String"
    """<p>The API ID.</p>"""
    definition: "capo_appsync.types.blob.Blob"
    """<p>The schema definition, in GraphQL schema language format.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: StartSchemaCreationRequest) -> dict:
    out: dict = {}
    import capo_appsync.types.blob

    out["definition"] = capo_appsync.types.blob.serialize_json(value["definition"])
    return out


def deserialize_json(data: dict) -> StartSchemaCreationRequest:
    out: StartSchemaCreationRequest = {}  # type: ignore[typeddict-item]
    if data.get("definition") is not None:
        import capo_appsync.types.blob

        out["definition"] = capo_appsync.types.blob.deserialize_json(data["definition"])
    else:
        out["definition"] = b""
    return out
