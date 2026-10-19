"""Generated from Smithy shape ``com.amazonaws.ecs#Ulimit``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ecs.types.integer
    import capo_ecs.types.ulimit_name


class Ulimit(TypedDict, closed=True):
    name: "capo_ecs.types.ulimit_name.UlimitName"
    """<p>The <code>type</code> of the <code>ulimit</code>.</p>"""
    soft_limit: "capo_ecs.types.integer.Integer"
    """<p>The soft limit for the <code>ulimit</code> type. The value can be specified in bytes, seconds, or as a count, depending on the <code>type</code> of the <code>ulimit</code>.</p>"""
    hard_limit: "capo_ecs.types.integer.Integer"
    """<p>The hard limit for the <code>ulimit</code> type. The value can be specified in bytes, seconds, or as a count, depending on the <code>type</code> of the <code>ulimit</code>.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: Ulimit) -> dict:
    out: dict = {}
    import capo_ecs.types.ulimit_name

    out["name"] = capo_ecs.types.ulimit_name.serialize_aws_json_1_1(value["name"])
    out["softLimit"] = value.get("soft_limit", 0)
    out["hardLimit"] = value.get("hard_limit", 0)
    return out


def deserialize_aws_json_1_1(data: dict) -> Ulimit:
    out: Ulimit = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_ecs.types.ulimit_name

        out["name"] = capo_ecs.types.ulimit_name.deserialize_aws_json_1_1(data["name"])
    else:
        import typing

        out["name"] = typing.cast("capo_ecs.types.ulimit_name.UlimitName", "")
    if data.get("softLimit") is not None:
        out["soft_limit"] = data["softLimit"]
    else:
        out["soft_limit"] = 0
    if data.get("hardLimit") is not None:
        out["hard_limit"] = data["hardLimit"]
    else:
        out["hard_limit"] = 0
    return out
