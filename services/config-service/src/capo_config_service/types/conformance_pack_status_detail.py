"""Generated from Smithy shape ``com.amazonaws.configservice#ConformancePackStatusDetail``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_config_service.types.conformance_pack_arn
    import capo_config_service.types.conformance_pack_id
    import capo_config_service.types.conformance_pack_name
    import capo_config_service.types.conformance_pack_state
    import capo_config_service.types.conformance_pack_status_reason
    import capo_config_service.types.date
    import capo_config_service.types.stack_arn


class ConformancePackStatusDetail(TypedDict, closed=True):
    conformance_pack_name: (
        "capo_config_service.types.conformance_pack_name.ConformancePackName"
    )
    """<p>Name of the conformance pack.</p>"""
    conformance_pack_id: (
        "capo_config_service.types.conformance_pack_id.ConformancePackId"
    )
    """<p>ID of the conformance pack.</p>"""
    conformance_pack_arn: (
        "capo_config_service.types.conformance_pack_arn.ConformancePackArn"
    )
    """<p>Amazon Resource Name (ARN) of comformance pack.</p>"""
    conformance_pack_state: (
        "capo_config_service.types.conformance_pack_state.ConformancePackState"
    )
    """<p>Indicates deployment status of conformance pack.</p> <p>Config sets the state of the conformance pack to:</p> <ul> <li> <p>CREATE_IN_PROGRESS when a conformance pack creation is in progress for an account.</p> </li> <li> <p>CREATE_COMPLETE when a conformance pack has been successfully created in your account.</p> </li> <li> <p>CREATE_FAILED when a conformance pack creation failed in your account.</p> </li> <li> <p>DELETE_IN_PROGRESS when a conformance pack deletion is in progress. </p> </li> <li> <p>DELETE_FAILED when a conformance pack deletion failed in your account.</p> </li> </ul>"""
    stack_arn: "capo_config_service.types.stack_arn.StackArn"
    """<p>Amazon Resource Name (ARN) of CloudFormation stack. </p>"""
    conformance_pack_status_reason: NotRequired[
        "capo_config_service.types.conformance_pack_status_reason.ConformancePackStatusReason"
    ]
    """<p>The reason of conformance pack creation failure.</p>"""
    last_update_requested_time: "capo_config_service.types.date.Date"
    """<p>Last time when conformation pack creation and update was requested.</p>"""
    last_update_completed_time: NotRequired["capo_config_service.types.date.Date"]
    """<p>Last time when conformation pack creation and update was successful.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: ConformancePackStatusDetail) -> dict:
    out: dict = {}
    out["ConformancePackName"] = value["conformance_pack_name"]
    out["ConformancePackId"] = value["conformance_pack_id"]
    out["ConformancePackArn"] = value["conformance_pack_arn"]
    import capo_config_service.types.conformance_pack_state

    out["ConformancePackState"] = (
        capo_config_service.types.conformance_pack_state.serialize_aws_json_1_1(
            value["conformance_pack_state"]
        )
    )
    out["StackArn"] = value["stack_arn"]
    if "conformance_pack_status_reason" in value:
        out["ConformancePackStatusReason"] = value["conformance_pack_status_reason"]
    import capo_config_service.types.date

    out["LastUpdateRequestedTime"] = (
        capo_config_service.types.date.serialize_aws_json_1_1(
            value["last_update_requested_time"]
        )
    )
    if "last_update_completed_time" in value:
        import capo_config_service.types.date

        out["LastUpdateCompletedTime"] = (
            capo_config_service.types.date.serialize_aws_json_1_1(
                value["last_update_completed_time"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> ConformancePackStatusDetail:
    out: ConformancePackStatusDetail = {}  # type: ignore[typeddict-item]
    if data.get("ConformancePackName") is not None:
        out["conformance_pack_name"] = data["ConformancePackName"]
    else:
        out["conformance_pack_name"] = ""
    if data.get("ConformancePackId") is not None:
        out["conformance_pack_id"] = data["ConformancePackId"]
    else:
        out["conformance_pack_id"] = ""
    if data.get("ConformancePackArn") is not None:
        out["conformance_pack_arn"] = data["ConformancePackArn"]
    else:
        out["conformance_pack_arn"] = ""
    if data.get("ConformancePackState") is not None:
        import capo_config_service.types.conformance_pack_state

        out["conformance_pack_state"] = (
            capo_config_service.types.conformance_pack_state.deserialize_aws_json_1_1(
                data["ConformancePackState"]
            )
        )
    else:
        import typing

        out["conformance_pack_state"] = typing.cast(
            "capo_config_service.types.conformance_pack_state.ConformancePackState", ""
        )
    if data.get("StackArn") is not None:
        out["stack_arn"] = data["StackArn"]
    else:
        out["stack_arn"] = ""
    if data.get("ConformancePackStatusReason") is not None:
        out["conformance_pack_status_reason"] = data["ConformancePackStatusReason"]
    if data.get("LastUpdateRequestedTime") is not None:
        import capo_config_service.types.date

        out["last_update_requested_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateRequestedTime"]
            )
        )
    else:
        import datetime

        out["last_update_requested_time"] = datetime.datetime.fromtimestamp(
            0, tz=datetime.timezone.utc
        )
    if data.get("LastUpdateCompletedTime") is not None:
        import capo_config_service.types.date

        out["last_update_completed_time"] = (
            capo_config_service.types.date.deserialize_aws_json_1_1(
                data["LastUpdateCompletedTime"]
            )
        )
    return out
