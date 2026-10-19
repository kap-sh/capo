"""Generated from Smithy shape ``com.amazonaws.shield#SummarizedAttackVector``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_shield.types.string
    import capo_shield.types.summarized_counter_list


class SummarizedAttackVector(TypedDict, closed=True):
    vector_type: "capo_shield.types.string.String"
    """<p>The attack type, for example, SNMP reflection or SYN flood.</p>"""
    vector_counters: NotRequired[
        "capo_shield.types.summarized_counter_list.SummarizedCounterList"
    ]
    """<p>The list of counters that describe the details of the attack.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: SummarizedAttackVector) -> dict:
    out: dict = {}
    out["VectorType"] = value["vector_type"]
    if "vector_counters" in value:
        import capo_shield.types.summarized_counter_list

        out["VectorCounters"] = (
            capo_shield.types.summarized_counter_list.serialize_aws_json_1_1(
                value["vector_counters"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> SummarizedAttackVector:
    out: SummarizedAttackVector = {}  # type: ignore[typeddict-item]
    if data.get("VectorType") is not None:
        out["vector_type"] = data["VectorType"]
    else:
        out["vector_type"] = ""
    if data.get("VectorCounters") is not None:
        import capo_shield.types.summarized_counter_list

        out["vector_counters"] = (
            capo_shield.types.summarized_counter_list.deserialize_aws_json_1_1(
                data["VectorCounters"]
            )
        )
    return out
