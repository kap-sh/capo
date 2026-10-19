"""Generated from Smithy shape ``com.amazonaws.lambda#ListCapacityProvidersResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lambda.types.capacity_providers_list
    import capo_lambda.types.string


class ListCapacityProvidersResponse(TypedDict, closed=True):
    capacity_providers: (
        "capo_lambda.types.capacity_providers_list.CapacityProvidersList"
    )
    """<p>A list of capacity providers in your account.</p>"""
    next_marker: NotRequired["capo_lambda.types.string.String"]
    """<p>The pagination token that's included if more results are available.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListCapacityProvidersResponse) -> dict:
    out: dict = {}
    import capo_lambda.types.capacity_providers_list

    out["CapacityProviders"] = capo_lambda.types.capacity_providers_list.serialize_json(
        value["capacity_providers"]
    )
    if "next_marker" in value:
        out["NextMarker"] = value["next_marker"]
    return out


def deserialize_json(data: dict) -> ListCapacityProvidersResponse:
    out: ListCapacityProvidersResponse = {}  # type: ignore[typeddict-item]
    if data.get("CapacityProviders") is not None:
        import capo_lambda.types.capacity_providers_list

        out["capacity_providers"] = (
            capo_lambda.types.capacity_providers_list.deserialize_json(
                data["CapacityProviders"]
            )
        )
    else:
        out["capacity_providers"] = []
    if data.get("NextMarker") is not None:
        out["next_marker"] = data["NextMarker"]
    return out
