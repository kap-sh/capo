"""Generated from Smithy shape ``com.amazonaws.cloudwatch#DescribeAlarmContributorsOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_contributors
    import capo_cloudwatch.types.next_token


class DescribeAlarmContributorsOutput(TypedDict, closed=True):
    alarm_contributors: NotRequired[
        "capo_cloudwatch.types.alarm_contributors.AlarmContributors"
    ]
    """<p>A list of alarm contributors that provide details about the individual time series contributing to the alarm's state.</p>"""
    next_token: NotRequired["capo_cloudwatch.types.next_token.NextToken"]
    """<p>The token that marks the start of the next batch of returned results.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: DescribeAlarmContributorsOutput) -> dict:
    out: dict = {}
    if "alarm_contributors" in value:
        import capo_cloudwatch.types.alarm_contributors

        out["AlarmContributors"] = (
            capo_cloudwatch.types.alarm_contributors.serialize_aws_json_1_0(
                value["alarm_contributors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_0(data: dict) -> DescribeAlarmContributorsOutput:
    out: DescribeAlarmContributorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmContributors") is not None:
        import capo_cloudwatch.types.alarm_contributors

        out["alarm_contributors"] = (
            capo_cloudwatch.types.alarm_contributors.deserialize_aws_json_1_0(
                data["AlarmContributors"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- awsQuery ser/de ---
def serialize_query(
    value: DescribeAlarmContributorsOutput, pairs: list[tuple[str, str]], prefix: str
) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "alarm_contributors" in value:
        import capo_cloudwatch.types.alarm_contributors

        capo_cloudwatch.types.alarm_contributors.serialize_query(
            value["alarm_contributors"], pairs, f"{key_prefix}AlarmContributors"
        )
    if "next_token" in value:
        pairs.append((f"{key_prefix}NextToken", str(value["next_token"])))


def deserialize_query(el: Element) -> DescribeAlarmContributorsOutput:
    out: DescribeAlarmContributorsOutput = {}  # type: ignore[typeddict-item]
    child_alarm_contributors = el.find("AlarmContributors")
    if child_alarm_contributors is not None:
        import capo_cloudwatch.types.alarm_contributors

        out["alarm_contributors"] = (
            capo_cloudwatch.types.alarm_contributors.deserialize_query(
                child_alarm_contributors
            )
        )
    child_next_token = el.find("NextToken")
    if child_next_token is not None:
        out["next_token"] = str(child_next_token.text or "")
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAlarmContributorsOutput) -> dict:
    out: dict = {}
    if "alarm_contributors" in value:
        import capo_cloudwatch.types.alarm_contributors

        out["AlarmContributors"] = (
            capo_cloudwatch.types.alarm_contributors.serialize_cbor(
                value["alarm_contributors"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAlarmContributorsOutput:
    out: DescribeAlarmContributorsOutput = {}  # type: ignore[typeddict-item]
    if data.get("AlarmContributors") is not None:
        import capo_cloudwatch.types.alarm_contributors

        out["alarm_contributors"] = (
            capo_cloudwatch.types.alarm_contributors.deserialize_cbor(
                data["AlarmContributors"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
