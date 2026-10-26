"""Generated from Smithy shape ``com.amazonaws.cleanrooms#ProtectedQueryResultConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_cleanrooms.types.protected_query_output_configuration


class ProtectedQueryResultConfiguration(TypedDict, closed=True):
    output_configuration: "capo_cleanrooms.types.protected_query_output_configuration.ProtectedQueryOutputConfiguration"
    """<p>Configuration for protected query results.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ProtectedQueryResultConfiguration) -> dict:
    out: dict = {}
    import capo_cleanrooms.types.protected_query_output_configuration

    out["outputConfiguration"] = (
        capo_cleanrooms.types.protected_query_output_configuration.serialize_json(
            value["output_configuration"]
        )
    )
    return out


def deserialize_json(data: dict) -> ProtectedQueryResultConfiguration:
    out: ProtectedQueryResultConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("outputConfiguration") is not None:
        import capo_cleanrooms.types.protected_query_output_configuration

        out["output_configuration"] = (
            capo_cleanrooms.types.protected_query_output_configuration.deserialize_json(
                data["outputConfiguration"]
            )
        )
    else:
        out["output_configuration"] = {"$unknown": {"name": ""}}
    return out
