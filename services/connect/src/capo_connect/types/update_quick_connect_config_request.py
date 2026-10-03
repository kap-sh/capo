"""Generated from Smithy shape ``com.amazonaws.connect#UpdateQuickConnectConfigRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_connect.errors import DeserializationError

if TYPE_CHECKING:
    import capo_connect.types.instance_id
    import capo_connect.types.quick_connect_config
    import capo_connect.types.quick_connect_id


class UpdateQuickConnectConfigRequest(TypedDict, closed=True):
    instance_id: "capo_connect.types.instance_id.InstanceId"
    """<p>The identifier of the Connect Customer instance. You can <a href="https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html">find the instance ID</a> in the Amazon Resource Name (ARN) of the instance.</p>"""
    quick_connect_id: "capo_connect.types.quick_connect_id.QuickConnectId"
    """<p>The identifier for the quick connect.</p>"""
    quick_connect_config: "capo_connect.types.quick_connect_config.QuickConnectConfig"
    """<p>Information about the configuration settings for the quick connect.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: UpdateQuickConnectConfigRequest) -> dict:
    out: dict = {}
    import capo_connect.types.quick_connect_config

    out["QuickConnectConfig"] = capo_connect.types.quick_connect_config.serialize_json(
        value["quick_connect_config"]
    )
    return out


def deserialize_json(data: dict) -> UpdateQuickConnectConfigRequest:
    out: UpdateQuickConnectConfigRequest = {}  # type: ignore[typeddict-item]
    if data.get("QuickConnectConfig") is not None:
        import capo_connect.types.quick_connect_config

        out["quick_connect_config"] = (
            capo_connect.types.quick_connect_config.deserialize_json(
                data["QuickConnectConfig"]
            )
        )
    else:
        raise DeserializationError(
            "UpdateQuickConnectConfigRequest.quick_connect_config required"
        )
    return out
