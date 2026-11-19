"""Generated from Smithy shape ``com.amazonaws.cloudwatch#Rule``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_cloudwatch._protocol.xml import Element

if TYPE_CHECKING:
    import capo_cloudwatch.types.schedule


class Rule(TypedDict, closed=True):
    schedule: NotRequired["capo_cloudwatch.types.schedule.Schedule"]
    """<p>The schedule configuration that defines when the mute rule activates and how long it remains active.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: Rule) -> dict:
    out: dict = {}
    if "schedule" in value:
        import capo_cloudwatch.types.schedule

        out["Schedule"] = capo_cloudwatch.types.schedule.serialize_aws_json_1_0(
            value["schedule"]
        )
    return out


def deserialize_aws_json_1_0(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("Schedule") is not None:
        import capo_cloudwatch.types.schedule

        out["schedule"] = capo_cloudwatch.types.schedule.deserialize_aws_json_1_0(
            data["Schedule"]
        )
    return out


# --- awsQuery ser/de ---
def serialize_query(value: Rule, pairs: list[tuple[str, str]], prefix: str) -> None:
    key_prefix = f"{prefix}." if prefix else ""
    if "schedule" in value:
        import capo_cloudwatch.types.schedule

        capo_cloudwatch.types.schedule.serialize_query(
            value["schedule"], pairs, f"{key_prefix}Schedule"
        )


def deserialize_query(el: Element) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    child_schedule = el.find("Schedule")
    if child_schedule is not None:
        import capo_cloudwatch.types.schedule

        out["schedule"] = capo_cloudwatch.types.schedule.deserialize_query(
            child_schedule
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: Rule) -> dict:
    out: dict = {}
    if "schedule" in value:
        import capo_cloudwatch.types.schedule

        out["Schedule"] = capo_cloudwatch.types.schedule.serialize_cbor(
            value["schedule"]
        )
    return out


def deserialize_cbor(data: dict) -> Rule:
    out: Rule = {}  # type: ignore[typeddict-item]
    if data.get("Schedule") is not None:
        import capo_cloudwatch.types.schedule

        out["schedule"] = capo_cloudwatch.types.schedule.deserialize_cbor(
            data["Schedule"]
        )
    return out
