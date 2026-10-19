"""Generated from Smithy shape ``com.amazonaws.ivschat#ListLoggingConfigurationsResponse``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.logging_configuration_list
    import capo_ivschat.types.pagination_token


class ListLoggingConfigurationsResponse(TypedDict, closed=True):
    logging_configurations: (
        "capo_ivschat.types.logging_configuration_list.LoggingConfigurationList"
    )
    """<p>List of the matching logging configurations (summary information only). There is only one type of destination (<code>cloudWatchLogs</code>, <code>firehose</code>, or <code>s3</code>) in a <code>destinationConfiguration</code>.</p>"""
    next_token: NotRequired["capo_ivschat.types.pagination_token.PaginationToken"]
    """<p>If there are more logging configurations than <code>maxResults</code>, use <code>nextToken</code> in the request to get the next set.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListLoggingConfigurationsResponse) -> dict:
    out: dict = {}
    import capo_ivschat.types.logging_configuration_list

    out["loggingConfigurations"] = (
        capo_ivschat.types.logging_configuration_list.serialize_json(
            value["logging_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListLoggingConfigurationsResponse:
    out: ListLoggingConfigurationsResponse = {}  # type: ignore[typeddict-item]
    if data.get("loggingConfigurations") is not None:
        import capo_ivschat.types.logging_configuration_list

        out["logging_configurations"] = (
            capo_ivschat.types.logging_configuration_list.deserialize_json(
                data["loggingConfigurations"]
            )
        )
    else:
        out["logging_configurations"] = []
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
