"""Generated from Smithy shape ``com.amazonaws.arcregionswitch#AssociatedAlarm``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_arc_region_switch.types.alarm_type
    import capo_arc_region_switch.types.iam_role_arn


class AssociatedAlarm(TypedDict, closed=True):
    cross_account_role: NotRequired[
        "capo_arc_region_switch.types.iam_role_arn.IamRoleArn"
    ]
    """<p>The cross account role for the configuration.</p>"""
    external_id: NotRequired["str"]
    """<p>The external ID (secret key) for the configuration.</p>"""
    resource_identifier: "str"
    """<p>The resource identifier for alarms that you associate with a plan.</p>"""
    alarm_type: "capo_arc_region_switch.types.alarm_type.AlarmType"
    """<p>The alarm type for an associated alarm. An associated CloudWatch alarm can be an application health alarm or a trigger alarm.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: AssociatedAlarm) -> dict:
    out: dict = {}
    if "cross_account_role" in value:
        out["crossAccountRole"] = value["cross_account_role"]
    if "external_id" in value:
        out["externalId"] = value["external_id"]
    out["resourceIdentifier"] = value["resource_identifier"]
    import capo_arc_region_switch.types.alarm_type

    out["alarmType"] = capo_arc_region_switch.types.alarm_type.serialize_aws_json_1_0(
        value["alarm_type"]
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> AssociatedAlarm:
    out: AssociatedAlarm = {}  # type: ignore[typeddict-item]
    if data.get("crossAccountRole") is not None:
        out["cross_account_role"] = data["crossAccountRole"]
    if data.get("externalId") is not None:
        out["external_id"] = data["externalId"]
    if data.get("resourceIdentifier") is not None:
        out["resource_identifier"] = data["resourceIdentifier"]
    else:
        out["resource_identifier"] = ""
    if data.get("alarmType") is not None:
        import capo_arc_region_switch.types.alarm_type

        out["alarm_type"] = (
            capo_arc_region_switch.types.alarm_type.deserialize_aws_json_1_0(
                data["alarmType"]
            )
        )
    else:
        import typing

        out["alarm_type"] = typing.cast(
            "capo_arc_region_switch.types.alarm_type.AlarmType", ""
        )
    return out
