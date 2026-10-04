"""Generated from Smithy shape ``com.amazonaws.endusermessaging#ListNotifyCodeConfigurationsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_endusermessaging.errors import DeserializationError

if TYPE_CHECKING:
    import capo_endusermessaging.types.next_token
    import capo_endusermessaging.types.notify_code_configuration_list


class ListNotifyCodeConfigurationsOutput(TypedDict, closed=True):
    notify_code_configurations: "capo_endusermessaging.types.notify_code_configuration_list.NotifyCodeConfigurationList"
    """<p>The list of notify code configurations.</p>"""
    next_token: NotRequired["capo_endusermessaging.types.next_token.NextToken"]
    """<p>The token to retrieve the next page of results. This value is returned when more results are available, and is null when there are no more results to return.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ListNotifyCodeConfigurationsOutput) -> dict:
    out: dict = {}
    import capo_endusermessaging.types.notify_code_configuration_list

    out["notifyCodeConfigurations"] = (
        capo_endusermessaging.types.notify_code_configuration_list.serialize_json(
            value["notify_code_configurations"]
        )
    )
    if "next_token" in value:
        out["nextToken"] = value["next_token"]
    return out


def deserialize_json(data: dict) -> ListNotifyCodeConfigurationsOutput:
    out: ListNotifyCodeConfigurationsOutput = {}  # type: ignore[typeddict-item]
    if data.get("notifyCodeConfigurations") is not None:
        import capo_endusermessaging.types.notify_code_configuration_list

        out["notify_code_configurations"] = (
            capo_endusermessaging.types.notify_code_configuration_list.deserialize_json(
                data["notifyCodeConfigurations"]
            )
        )
    else:
        raise DeserializationError(
            "ListNotifyCodeConfigurationsOutput.notify_code_configurations required"
        )
    if data.get("nextToken") is not None:
        out["next_token"] = data["nextToken"]
    return out
