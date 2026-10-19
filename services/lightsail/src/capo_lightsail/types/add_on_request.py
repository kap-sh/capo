"""Generated from Smithy shape ``com.amazonaws.lightsail#AddOnRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_lightsail.types.add_on_type
    import capo_lightsail.types.auto_snapshot_add_on_request
    import capo_lightsail.types.stop_instance_on_idle_request


class AddOnRequest(TypedDict, closed=True):
    add_on_type: "capo_lightsail.types.add_on_type.AddOnType"
    """<p>The add-on type.</p>"""
    auto_snapshot_add_on_request: NotRequired[
        "capo_lightsail.types.auto_snapshot_add_on_request.AutoSnapshotAddOnRequest"
    ]
    """<p>An object that represents additional parameters when enabling or modifying the automatic snapshot add-on.</p>"""
    stop_instance_on_idle_request: NotRequired[
        "capo_lightsail.types.stop_instance_on_idle_request.StopInstanceOnIdleRequest"
    ]
    """<p>An object that represents additional parameters when enabling or modifying the <code>StopInstanceOnIdle</code> add-on.</p> <important> <p>This object only applies to Lightsail for Research resources.</p> </important>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AddOnRequest) -> dict:
    out: dict = {}
    import capo_lightsail.types.add_on_type

    out["addOnType"] = capo_lightsail.types.add_on_type.serialize_aws_json_1_1(
        value["add_on_type"]
    )
    if "auto_snapshot_add_on_request" in value:
        import capo_lightsail.types.auto_snapshot_add_on_request

        out["autoSnapshotAddOnRequest"] = (
            capo_lightsail.types.auto_snapshot_add_on_request.serialize_aws_json_1_1(
                value["auto_snapshot_add_on_request"]
            )
        )
    if "stop_instance_on_idle_request" in value:
        import capo_lightsail.types.stop_instance_on_idle_request

        out["stopInstanceOnIdleRequest"] = (
            capo_lightsail.types.stop_instance_on_idle_request.serialize_aws_json_1_1(
                value["stop_instance_on_idle_request"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AddOnRequest:
    out: AddOnRequest = {}  # type: ignore[typeddict-item]
    if data.get("addOnType") is not None:
        import capo_lightsail.types.add_on_type

        out["add_on_type"] = capo_lightsail.types.add_on_type.deserialize_aws_json_1_1(
            data["addOnType"]
        )
    else:
        import typing

        out["add_on_type"] = typing.cast(
            "capo_lightsail.types.add_on_type.AddOnType", ""
        )
    if data.get("autoSnapshotAddOnRequest") is not None:
        import capo_lightsail.types.auto_snapshot_add_on_request

        out["auto_snapshot_add_on_request"] = (
            capo_lightsail.types.auto_snapshot_add_on_request.deserialize_aws_json_1_1(
                data["autoSnapshotAddOnRequest"]
            )
        )
    if data.get("stopInstanceOnIdleRequest") is not None:
        import capo_lightsail.types.stop_instance_on_idle_request

        out["stop_instance_on_idle_request"] = (
            capo_lightsail.types.stop_instance_on_idle_request.deserialize_aws_json_1_1(
                data["stopInstanceOnIdleRequest"]
            )
        )
    return out
