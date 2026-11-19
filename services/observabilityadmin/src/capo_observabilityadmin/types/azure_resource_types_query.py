"""Generated from Smithy shape ``com.amazonaws.observabilityadmin#AzureResourceTypesQuery``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_observabilityadmin.types.azure_query_scope


class AzureResourceTypesQuery(TypedDict, closed=True):
    scope: NotRequired[
        "capo_observabilityadmin.types.azure_query_scope.AzureQueryScope"
    ]
    """<p>Limits the query to a management group or to specific subscriptions.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AzureResourceTypesQuery) -> dict:
    out: dict = {}
    if "scope" in value:
        import capo_observabilityadmin.types.azure_query_scope

        out["Scope"] = capo_observabilityadmin.types.azure_query_scope.serialize_json(
            value["scope"]
        )
    return out


def deserialize_json(data: dict) -> AzureResourceTypesQuery:
    out: AzureResourceTypesQuery = {}  # type: ignore[typeddict-item]
    if data.get("Scope") is not None:
        import capo_observabilityadmin.types.azure_query_scope

        out["scope"] = capo_observabilityadmin.types.azure_query_scope.deserialize_json(
            data["Scope"]
        )
    return out
