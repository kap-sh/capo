"""Generated from Smithy shape ``com.amazonaws.connect#QuickConnectConfig``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_connect.types.flow_quick_connect_config
    import capo_connect.types.phone_number_quick_connect_config
    import capo_connect.types.queue_quick_connect_config
    import capo_connect.types.quick_connect_type
    import capo_connect.types.user_quick_connect_config


class QuickConnectConfig(TypedDict, closed=True):
    quick_connect_type: "capo_connect.types.quick_connect_type.QuickConnectType"
    """<p>The type of quick connect. In the Connect Customer admin website, when you create a quick connect, you are prompted to assign one of the following types: Agent (USER), External (PHONE_NUMBER), or Queue (QUEUE). </p>"""
    user_config: NotRequired[
        "capo_connect.types.user_quick_connect_config.UserQuickConnectConfig"
    ]
    """<p>The user configuration. This is required only if QuickConnectType is USER.</p>"""
    queue_config: NotRequired[
        "capo_connect.types.queue_quick_connect_config.QueueQuickConnectConfig"
    ]
    """<p>The queue configuration. This is required only if QuickConnectType is QUEUE.</p>"""
    phone_config: NotRequired[
        "capo_connect.types.phone_number_quick_connect_config.PhoneNumberQuickConnectConfig"
    ]
    """<p>The phone configuration. This is required only if QuickConnectType is PHONE_NUMBER.</p>"""
    flow_config: NotRequired[
        "capo_connect.types.flow_quick_connect_config.FlowQuickConnectConfig"
    ]
    """<p> Flow configuration for quick connect setup. </p>"""


# --- restJson1 ser/de ---
def serialize_json(value: QuickConnectConfig) -> dict:
    out: dict = {}
    import capo_connect.types.quick_connect_type

    out["QuickConnectType"] = capo_connect.types.quick_connect_type.serialize_json(
        value["quick_connect_type"]
    )
    if "user_config" in value:
        import capo_connect.types.user_quick_connect_config

        out["UserConfig"] = capo_connect.types.user_quick_connect_config.serialize_json(
            value["user_config"]
        )
    if "queue_config" in value:
        import capo_connect.types.queue_quick_connect_config

        out["QueueConfig"] = (
            capo_connect.types.queue_quick_connect_config.serialize_json(
                value["queue_config"]
            )
        )
    if "phone_config" in value:
        import capo_connect.types.phone_number_quick_connect_config

        out["PhoneConfig"] = (
            capo_connect.types.phone_number_quick_connect_config.serialize_json(
                value["phone_config"]
            )
        )
    if "flow_config" in value:
        import capo_connect.types.flow_quick_connect_config

        out["FlowConfig"] = capo_connect.types.flow_quick_connect_config.serialize_json(
            value["flow_config"]
        )
    return out


def deserialize_json(data: dict) -> QuickConnectConfig:
    out: QuickConnectConfig = {}  # type: ignore[typeddict-item]
    if data.get("QuickConnectType") is not None:
        import capo_connect.types.quick_connect_type

        out["quick_connect_type"] = (
            capo_connect.types.quick_connect_type.deserialize_json(
                data["QuickConnectType"]
            )
        )
    else:
        import typing

        out["quick_connect_type"] = typing.cast(
            "capo_connect.types.quick_connect_type.QuickConnectType", ""
        )
    if data.get("UserConfig") is not None:
        import capo_connect.types.user_quick_connect_config

        out["user_config"] = (
            capo_connect.types.user_quick_connect_config.deserialize_json(
                data["UserConfig"]
            )
        )
    if data.get("QueueConfig") is not None:
        import capo_connect.types.queue_quick_connect_config

        out["queue_config"] = (
            capo_connect.types.queue_quick_connect_config.deserialize_json(
                data["QueueConfig"]
            )
        )
    if data.get("PhoneConfig") is not None:
        import capo_connect.types.phone_number_quick_connect_config

        out["phone_config"] = (
            capo_connect.types.phone_number_quick_connect_config.deserialize_json(
                data["PhoneConfig"]
            )
        )
    if data.get("FlowConfig") is not None:
        import capo_connect.types.flow_quick_connect_config

        out["flow_config"] = (
            capo_connect.types.flow_quick_connect_config.deserialize_json(
                data["FlowConfig"]
            )
        )
    return out
