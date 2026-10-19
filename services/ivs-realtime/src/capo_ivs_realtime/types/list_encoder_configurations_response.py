"""Generated from Smithy shape ``com.amazonaws.ivsrealtime#ListEncoderConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivs_realtime.types.encoder_configuration_summary_list
    import capo_ivs_realtime.types.pagination_token


class ListEncoderConfigurationsResponse(TypedDict, closed=True):
    encoder_configurations: "capo_ivs_realtime.types.encoder_configuration_summary_list.EncoderConfigurationSummaryList"
    """<p>List of the matching EncoderConfigurations (summary information only).</p>"""
    next_token: NotRequired["capo_ivs_realtime.types.pagination_token.PaginationToken"]
    """<p>If there are more encoder configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListEncoderConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivs_realtime.types.encoder_configuration_summary_list

    out["encoderConfigurations"] = (
        capo_ivs_realtime.types.encoder_configuration_summary_list.serialize_json(
            value["encoder_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListEncoderConfigurationsResponse:
    out: ListEncoderConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("encoderConfigurations") is not None:
        import capo_ivs_realtime.types.encoder_configuration_summary_list

        out["encoder_configurations"] = (
            capo_ivs_realtime.types.encoder_configuration_summary_list.deserialize_json(
                data["encoderConfigurations"]
            )
        )
    else:
        out["encoder_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
