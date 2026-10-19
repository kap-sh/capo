"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListConfiguredModelAlgorithmsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_model_algorithm_list
    import capo_cleanroomsml.types.next_token


class ListConfiguredModelAlgorithmsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    configured_model_algorithms: "capo_cleanroomsml.types.configured_model_algorithm_list.ConfiguredModelAlgorithmList"
    """<p>The list of configured model algorithms.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredModelAlgorithmsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.configured_model_algorithm_list

    out["configuredModelAlgorithms"] = (
        capo_cleanroomsml.types.configured_model_algorithm_list.serialize_json(
            value["configured_model_algorithms"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListConfiguredModelAlgorithmsResponse:
    out: ListConfiguredModelAlgorithmsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("configuredModelAlgorithms") is not None:
        import capo_cleanroomsml.types.configured_model_algorithm_list

        out["configured_model_algorithms"] = (
            capo_cleanroomsml.types.configured_model_algorithm_list.deserialize_json(
                data["configuredModelAlgorithms"]
            )
        )
    else:
        out["configured_model_algorithms"] = []
    return out
