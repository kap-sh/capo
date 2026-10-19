"""Generated from Smithy shape ``com.amazonaws.ivs#ListRecordingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs.types.pagination_token
    import capo_ivs.types.recording_configuration_list


class ListRecordingConfigurationsResponse(TypedDict, closed=True):
    recording_configurations: (
        "capo_ivs.types.recording_configuration_list.RecordingConfigurationList"
    )
    """<p>List of the matching recording configurations.</p>"""
    next_token: NotRequired["capo_ivs.types.pagination_token.PaginationToken"]
    """<p>If there are more recording configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListRecordingConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivs.types.recording_configuration_list

    out["recordingConfigurations"] = (
        capo_ivs.types.recording_configuration_list.serialize_json(
            value["recording_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListRecordingConfigurationsResponse:
    out: ListRecordingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("recordingConfigurations") is not None:
        import capo_ivs.types.recording_configuration_list

        out["recording_configurations"] = (
            capo_ivs.types.recording_configuration_list.deserialize_json(
                data["recordingConfigurations"]
            )
        )
    else:
        out["recording_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
