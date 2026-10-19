"""Generated from Smithy shape ``com.amazonaws.cleanroomsml#ListConfiguredAudienceModelsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_cleanroomsml.types.configured_audience_model_list
    import capo_cleanroomsml.types.next_token


class ListConfiguredAudienceModelsResponse(TypedDict, closed=True):
    next_token: NotRequired["capo_cleanroomsml.types.next_token.NextToken"]
    """<p>The token value used to access the next page of results.</p>"""
    configured_audience_models: "capo_cleanroomsml.types.configured_audience_model_list.ConfiguredAudienceModelList"
    """<p>The configured audience models.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListConfiguredAudienceModelsResponse) -> dict:
    out: dict = {}
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    import capo_cleanroomsml.types.configured_audience_model_list

    out["configuredAudienceModels"] = (
        capo_cleanroomsml.types.configured_audience_model_list.serialize_json(
            value["configured_audience_models"]
        )
    )
    return out


def deserialize_json(data: dict) -> ListConfiguredAudienceModelsResponse:
    out: ListConfiguredAudienceModelsResponse = {}  # type: ignore[typeddict-item]
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    if data.get("configuredAudienceModels") is not None:
        import capo_cleanroomsml.types.configured_audience_model_list

        out["configured_audience_models"] = (
            capo_cleanroomsml.types.configured_audience_model_list.deserialize_json(
                data["configuredAudienceModels"]
            )
        )
    else:
        out["configured_audience_models"] = []
    return out
