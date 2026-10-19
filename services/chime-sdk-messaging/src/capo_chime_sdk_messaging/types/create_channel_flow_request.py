"""Generated from Smithy shape ``com.amazonaws.chimesdkmessaging#CreateChannelFlowRequest``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_chime_sdk_messaging.types.chime_arn
    import capo_chime_sdk_messaging.types.client_request_token
    import capo_chime_sdk_messaging.types.non_empty_resource_name
    import capo_chime_sdk_messaging.types.processor_list
    import capo_chime_sdk_messaging.types.tag_list


class CreateChannelFlowRequest(TypedDict, closed=True):
    app_instance_arn: "capo_chime_sdk_messaging.types.chime_arn.ChimeArn"
    """<p>The ARN of the channel flow request.</p>"""
    processors: "capo_chime_sdk_messaging.types.processor_list.ProcessorList"
    """<p>Information about the processor Lambda functions.</p>"""
    name: "capo_chime_sdk_messaging.types.non_empty_resource_name.NonEmptyResourceName"
    """<p>The name of the channel flow.</p>"""
    tags: NotRequired["capo_chime_sdk_messaging.types.tag_list.TagList"]
    """<p>The tags for the creation request.</p>"""
    client_request_token: (
        "capo_chime_sdk_messaging.types.client_request_token.ClientRequestToken"
    )
    """<p>The client token for the request. An Idempotency token.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: CreateChannelFlowRequest) -> dict:
    out: dict = {}
    out["AppInstanceArn"] = value["app_instance_arn"]
    import capo_chime_sdk_messaging.types.processor_list

    out["Processors"] = capo_chime_sdk_messaging.types.processor_list.serialize_json(
        value["processors"]
    )
    out["Name"] = value["name"]
    if "tags" in value:
        import capo_chime_sdk_messaging.types.tag_list

        out["Tags"] = capo_chime_sdk_messaging.types.tag_list.serialize_json(
            value["tags"]
        )
    out["ClientRequestToken"] = value["client_request_token"]
    return out


def deserialize_json(data: dict) -> CreateChannelFlowRequest:
    out: CreateChannelFlowRequest = {}  # type: ignore[typeddict-item]
    if data.get("AppInstanceArn") is not None:
        out["app_instance_arn"] = data["AppInstanceArn"]
    else:
        out["app_instance_arn"] = ""
    if data.get("Processors") is not None:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.deserialize_json(
                data["Processors"]
            )
        )
    else:
        out["processors"] = []
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        out["name"] = ""
    if data.get("Tags") is not None:
        import capo_chime_sdk_messaging.types.tag_list

        out["tags"] = capo_chime_sdk_messaging.types.tag_list.deserialize_json(
            data["Tags"]
        )
    if data.get("ClientRequestToken") is not None:
        out["client_request_token"] = data["ClientRequestToken"]
    else:
        out["client_request_token"] = ""
    return out


def redact_sensitive(value: CreateChannelFlowRequest) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "processors" in value:
        import capo_chime_sdk_messaging.types.processor_list

        out["processors"] = (
            capo_chime_sdk_messaging.types.processor_list.redact_sensitive(
                value["processors"]
            )
        )
    if "name" in value:
        out["name"] = "*** Sensitive Data Redacted ***"
    if "tags" in value:
        import capo_chime_sdk_messaging.types.tag_list

        out["tags"] = capo_chime_sdk_messaging.types.tag_list.redact_sensitive(
            value["tags"]
        )
    if "client_request_token" in value:
        out["client_request_token"] = "*** Sensitive Data Redacted ***"
    return out
