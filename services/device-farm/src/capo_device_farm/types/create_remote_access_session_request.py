"""Generated from Smithy shape ``com.amazonaws.devicefarm#CreateRemoteAccessSessionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_device_farm.errors import DeserializationError

if TYPE_CHECKING:
    import capo_device_farm.types.amazon_resource_name
    import capo_device_farm.types.boolean
    import capo_device_farm.types.create_remote_access_session_configuration
    import capo_device_farm.types.interaction_mode
    import capo_device_farm.types.name


class CreateRemoteAccessSessionRequest(TypedDict, closed=True):
    project_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The Amazon Resource Name (ARN) of the project for which you want to create a remote access session.</p>"""
    device_arn: "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    """<p>The ARN of the device for which you want to create a remote access session.</p>"""
    app_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the app to create the remote access session.</p>"""
    instance_arn: NotRequired[
        "capo_device_farm.types.amazon_resource_name.AmazonResourceName"
    ]
    """<p>The Amazon Resource Name (ARN) of the device instance for which you want to create a remote access session.</p>"""
    name: NotRequired["capo_device_farm.types.name.Name"]
    """<p>The name of the remote access session to create.</p>"""
    configuration: NotRequired[
        "capo_device_farm.types.create_remote_access_session_configuration.CreateRemoteAccessSessionConfiguration"
    ]
    """<p>The configuration information for the remote access session request.</p>"""
    interaction_mode: NotRequired[
        "capo_device_farm.types.interaction_mode.InteractionMode"
    ]
    """<p>The interaction mode of the remote access session. Changing the interactive mode of remote access sessions is no longer available.</p>"""
    skip_app_resign: NotRequired["capo_device_farm.types.boolean.Boolean"]
    """<p>When set to <code>true</code>, for private devices, Device Farm does not sign your app again. For public devices, Device Farm always signs your apps again.</p> <p>For more information on how Device Farm modifies your uploads during tests, see <a href="http://aws.amazon.com/device-farm/faqs/">Do you modify my app?</a> </p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: CreateRemoteAccessSessionRequest) -> dict:
    out: dict = {}
    out["projectArn"] = value["project_arn"]
    out["deviceArn"] = value["device_arn"]
    if "app_arn" in value:
        out["appArn"] = value["app_arn"]
    if "instance_arn" in value:
        out["instanceArn"] = value["instance_arn"]
    if "name" in value:
        out["name"] = value["name"]
    if "configuration" in value:
        import capo_device_farm.types.create_remote_access_session_configuration

        out["configuration"] = (
            capo_device_farm.types.create_remote_access_session_configuration.serialize_aws_json_1_1(
                value["configuration"]
            )
        )
    if "interaction_mode" in value:
        import capo_device_farm.types.interaction_mode

        out["interactionMode"] = (
            capo_device_farm.types.interaction_mode.serialize_aws_json_1_1(
                value["interaction_mode"]
            )
        )
    if "skip_app_resign" in value:
        out["skipAppResign"] = value["skip_app_resign"]
    return out


def deserialize_aws_json_1_1(data: dict) -> CreateRemoteAccessSessionRequest:
    out: CreateRemoteAccessSessionRequest = {}  # type: ignore[typeddict-item]
    if data.get("projectArn") is not None:
        out["project_arn"] = data["projectArn"]
    else:
        raise DeserializationError(
            "CreateRemoteAccessSessionRequest.project_arn required"
        )
    if data.get("deviceArn") is not None:
        out["device_arn"] = data["deviceArn"]
    else:
        raise DeserializationError(
            "CreateRemoteAccessSessionRequest.device_arn required"
        )
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    if data.get("instanceArn") is not None:
        out["instance_arn"] = data["instanceArn"]
    if data.get("name") is not None:
        out["name"] = data["name"]
    if data.get("configuration") is not None:
        import capo_device_farm.types.create_remote_access_session_configuration

        out["configuration"] = (
            capo_device_farm.types.create_remote_access_session_configuration.deserialize_aws_json_1_1(
                data["configuration"]
            )
        )
    if data.get("interactionMode") is not None:
        import capo_device_farm.types.interaction_mode

        out["interaction_mode"] = (
            capo_device_farm.types.interaction_mode.deserialize_aws_json_1_1(
                data["interactionMode"]
            )
        )
    if data.get("skipAppResign") is not None:
        out["skip_app_resign"] = data["skipAppResign"]
    return out
