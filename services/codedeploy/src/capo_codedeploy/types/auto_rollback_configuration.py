"""Generated from Smithy shape ``com.amazonaws.codedeploy#AutoRollbackConfiguration``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codedeploy.types.auto_rollback_events_list
    import capo_codedeploy.types.boolean


class AutoRollbackConfiguration(TypedDict, closed=True):
    enabled: "capo_codedeploy.types.boolean.Boolean"
    """<p>Indicates whether a defined automatic rollback configuration is currently enabled.</p>"""
    events: NotRequired[
        "capo_codedeploy.types.auto_rollback_events_list.AutoRollbackEventsList"
    ]
    """<p>The event type or types that trigger a rollback.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AutoRollbackConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "events" in value:
        import capo_codedeploy.types.auto_rollback_events_list

        out["events"] = (
            capo_codedeploy.types.auto_rollback_events_list.serialize_aws_json_1_1(
                value["events"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AutoRollbackConfiguration:
    out: AutoRollbackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("events") is not None:
        import capo_codedeploy.types.auto_rollback_events_list

        out["events"] = (
            capo_codedeploy.types.auto_rollback_events_list.deserialize_aws_json_1_1(
                data["events"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AutoRollbackConfiguration) -> dict:
    out: dict = {}
    out["enabled"] = value.get("enabled", False)
    if "events" in value:
        import capo_codedeploy.types.auto_rollback_events_list

        out["events"] = capo_codedeploy.types.auto_rollback_events_list.serialize_cbor(
            value["events"]
        )
    return out


def deserialize_cbor(data: dict) -> AutoRollbackConfiguration:
    out: AutoRollbackConfiguration = {}  # type: ignore[typeddict-item]
    if data.get("enabled") is not None:
        out["enabled"] = data["enabled"]
    else:
        out["enabled"] = False
    if data.get("events") is not None:
        import capo_codedeploy.types.auto_rollback_events_list

        out["events"] = (
            capo_codedeploy.types.auto_rollback_events_list.deserialize_cbor(
                data["events"]
            )
        )
    return out
