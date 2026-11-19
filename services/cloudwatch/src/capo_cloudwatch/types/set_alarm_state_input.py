"""Generated from Smithy shape ``com.amazonaws.cloudwatch#SetAlarmStateInput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_name
    import capo_cloudwatch.types.state_reason
    import capo_cloudwatch.types.state_reason_data
    import capo_cloudwatch.types.state_value


class SetAlarmStateInput(TypedDict, closed=True):
    alarm_name: NotRequired["capo_cloudwatch.types.alarm_name.AlarmName"]
    """<p>The name of the alarm.</p>"""
    state_value: NotRequired["capo_cloudwatch.types.state_value.StateValue"]
    """<p>The value of the state.</p>"""
    state_reason: NotRequired["capo_cloudwatch.types.state_reason.StateReason"]
    """<p>The reason that this alarm is set to this specific state, in text format.</p>"""
    state_reason_data: NotRequired[
        "capo_cloudwatch.types.state_reason_data.StateReasonData"
    ]
    """<p>The reason that this alarm is set to this specific state, in JSON format.</p> <p>For SNS or EC2 alarm actions, this is just informational. But for EC2 Auto Scaling or application Auto Scaling alarm actions, the Auto Scaling policy uses the information in this field to take the correct action.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: SetAlarmStateInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        out["StateValue"] = capo_cloudwatch.types.state_value.serialize_aws_json_1_0(
            value["state_value"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_data" in value:
        out["StateReasonData"] = value["state_reason_data"]
    return out


def deserialize_aws_json_1_0(data: dict) -> SetAlarmStateInput:
    out: SetAlarmStateInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("StateValue") is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_aws_json_1_0(
            data["StateValue"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonData") is not None:
        out["state_reason_data"] = data["StateReasonData"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: SetAlarmStateInput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_name" in value:
        pairs.append((f"{key_prefix}AlarmName", str(value["alarm_name"])))
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        capo_cloudwatch.types.state_value.serialize_query(
            value["state_value"], pairs, f"{key_prefix}StateValue"
        )
    if "state_reason" in value:
        pairs.append((f"{key_prefix}StateReason", str(value["state_reason"])))
    if "state_reason_data" in value:
        pairs.append((f"{key_prefix}StateReasonData", str(value["state_reason_data"])))


def deserialize_query(el: Element) -> SetAlarmStateInput:
    out: SetAlarmStateInput = {}  # type: ignore[typeddict-item]
    child_alarm_name = el.find("AlarmName")
    if child_alarm_name is not None:
        out["alarm_name"] = str(child_alarm_name.text or "")
    child_state_value = el.find("StateValue")
    if child_state_value is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_query(
            child_state_value
        )
    child_state_reason = el.find("StateReason")
    if child_state_reason is not None:
        out["state_reason"] = str(child_state_reason.text or "")
    child_state_reason_data = el.find("StateReasonData")
    if child_state_reason_data is not None:
        out["state_reason_data"] = str(child_state_reason_data.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: SetAlarmStateInput) -> dict:
    out: dict = {}
    if "alarm_name" in value:
        out["AlarmName"] = value["alarm_name"]
    if "state_value" in value:
        import capo_cloudwatch.types.state_value

        out["StateValue"] = capo_cloudwatch.types.state_value.serialize_cbor(
            value["state_value"]
        )
    if "state_reason" in value:
        out["StateReason"] = value["state_reason"]
    if "state_reason_data" in value:
        out["StateReasonData"] = value["state_reason_data"]
    return out


def deserialize_cbor(data: dict) -> SetAlarmStateInput:
    out: SetAlarmStateInput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmName") is not None:
        out["alarm_name"] = data["AlarmName"]
    if data.get("StateValue") is not None:
        import capo_cloudwatch.types.state_value

        out["state_value"] = capo_cloudwatch.types.state_value.deserialize_cbor(
            data["StateValue"]
        )
    if data.get("StateReason") is not None:
        out["state_reason"] = data["StateReason"]
    if data.get("StateReasonData") is not None:
        out["state_reason_data"] = data["StateReasonData"]
    return out
