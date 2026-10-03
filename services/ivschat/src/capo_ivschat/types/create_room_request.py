"""Generated from Smithy shape ``com.amazonaws.ivschat#CreateRoomRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_ivschat.types.logging_configuration_identifier_list
    import capo_ivschat.types.message_review_handler
    import capo_ivschat.types.room_max_message_length
    import capo_ivschat.types.room_max_message_rate_per_second
    import capo_ivschat.types.room_name
    import capo_ivschat.types.tags


class CreateRoomRequest(TypedDict, closed=True):
    name: NotRequired["capo_ivschat.types.room_name.RoomName"]
    """<p>Room name. The value does not need to be unique.</p>"""
    maximum_message_rate_per_second: NotRequired[
        "capo_ivschat.types.room_max_message_rate_per_second.RoomMaxMessageRatePerSecond"
    ]
    """<p>Maximum number of messages per second that can be sent to the room (by all clients). Default: 10. </p>"""
    maximum_message_length: NotRequired[
        "capo_ivschat.types.room_max_message_length.RoomMaxMessageLength"
    ]
    """<p>Maximum number of characters in a single message. Messages are expected to be UTF-8 encoded and this limit applies specifically to rune/code-point count, not number of bytes. Default: 500.</p>"""
    message_review_handler: NotRequired[
        "capo_ivschat.types.message_review_handler.MessageReviewHandler"
    ]
    """<p>Configuration information for optional review of messages.</p>"""
    tags: NotRequired["capo_ivschat.types.tags.Tags"]
    """<p>Tags to attach to the resource. Array of maps, each of the form <code>string:string (key:value)</code>. See <a href="https://docs.aws.amazon.com/tag-editor/latest/userguide/best-practices-and-strats.html">Best practices and strategies</a> in <i>Tagging Amazon Web Services Resources and Tag Editor</i> for details, including restrictions that apply to tags and "Tag naming limits and requirements"; Amazon IVS Chat has no constraints beyond what is documented there.</p>"""
    logging_configuration_identifiers: NotRequired[
        "capo_ivschat.types.logging_configuration_identifier_list.LoggingConfigurationIdentifierList"
    ]
    """<p>Array of logging-configuration identifiers attached to the room.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateRoomRequest) -> dict:
    out: dict = {}
    if "name" in value:
        out["name"] = value["name"]
    if "maximum_message_rate_per_second" in value:
        out["maximumMessageRatePerSecond"] = value["maximum_message_rate_per_second"]
    if "maximum_message_length" in value:
        out["maximumMessageLength"] = value["maximum_message_length"]
    if "message_review_handler" in value:
        import capo_ivschat.types.message_review_handler

        out["messageReviewHandler"] = (
            capo_ivschat.types.message_review_handler.serialize_json(
                value["message_review_handler"]
            )
        )
    if "tags" in value:
        import capo_ivschat.types.tags

        out["tags"] = capo_ivschat.types.tags.serialize_json(value["tags"])
    if "logging_configuration_identifiers" in value:
        import capo_ivschat.types.logging_configuration_identifier_list

        out["loggingConfigurationIdentifiers"] = (
            capo_ivschat.types.logging_configuration_identifier_list.serialize_json(
                value["logging_configuration_identifiers"]
            )
        )
    return out


def deserialize_json(data: dict) -> CreateRoomRequest:
    out: CreateRoomRequest = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("maximumMessageRatePerSecond") is not None:
        out["maximum_message_rate_per_second"] = data["maximumMessageRatePerSecond"]
    if data.get("maximumMessageLength") is not None:
        out["maximum_message_length"] = data["maximumMessageLength"]
    if data.get("messageReviewHandler") is not None:
        import capo_ivschat.types.message_review_handler

        out["message_review_handler"] = (
            capo_ivschat.types.message_review_handler.deserialize_json(
                data["messageReviewHandler"]
            )
        )
    if data.get("tags") is not None:
        import capo_ivschat.types.tags

        out["tags"] = capo_ivschat.types.tags.deserialize_json(data["tags"])
    if data.get("loggingConfigurationIdentifiers") is not None:
        import capo_ivschat.types.logging_configuration_identifier_list

        out["logging_configuration_identifiers"] = (
            capo_ivschat.types.logging_configuration_identifier_list.deserialize_json(
                data["loggingConfigurationIdentifiers"]
            )
        )
    return out
