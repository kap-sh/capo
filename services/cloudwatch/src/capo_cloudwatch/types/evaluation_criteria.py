"""Generated from Smithy shape ``com.amazonaws.cloudwatch#EvaluationCriteria``."""

from typing import TYPE_CHECKING, TypeAlias

from typing_extensions import TypedDict

from capo_cloudwatch._protocol.xml import Element
from capo_cloudwatch.errors import DeserializationError, SerializationError
from capo_cloudwatch.types._unknown import UnknownUnionMember

if TYPE_CHECKING:
    import capo_cloudwatch.types.alarm_prom_ql_criteria


class _EvaluationCriteria_PromQLCriteria(TypedDict, closed=True):
    PromQLCriteria: "capo_cloudwatch.types.alarm_prom_ql_criteria.AlarmPromQLCriteria"


EvaluationCriteria: TypeAlias = _EvaluationCriteria_PromQLCriteria | UnknownUnionMember


# --- awsQuery ser/de ---
def serialize_query(
    value: EvaluationCriteria, pairs: list[tuple[str, str]], prefix: str
) -> None:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationCriteria: cannot serialize unknown variant {value.name!r}"
        )
    elif "PromQLCriteria" in value:
        import capo_cloudwatch.types.alarm_prom_ql_criteria

        capo_cloudwatch.types.alarm_prom_ql_criteria.serialize_query(
            value["PromQLCriteria"], pairs, f"{prefix}.PromQLCriteria"
        )
    else:
        raise SerializationError("EvaluationCriteria: no variant present")


def deserialize_query(el: Element) -> EvaluationCriteria:
    for child in el:
        if child.tag == "PromQLCriteria":
            import capo_cloudwatch.types.alarm_prom_ql_criteria

            return {
                "PromQLCriteria": capo_cloudwatch.types.alarm_prom_ql_criteria.deserialize_query(
                    child
                )
            }
        else:
            return UnknownUnionMember(child.tag)
    raise DeserializationError("EvaluationCriteria: no recognized variant element")


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: EvaluationCriteria) -> dict:
    if isinstance(value, UnknownUnionMember):
        raise SerializationError(
            f"EvaluationCriteria: cannot serialize unknown variant {value.name!r}"
        )
    elif "PromQLCriteria" in value:
        import capo_cloudwatch.types.alarm_prom_ql_criteria

        return {
            "PromQLCriteria": capo_cloudwatch.types.alarm_prom_ql_criteria.serialize_aws_json_1_0(
                value["PromQLCriteria"]
            )
        }
    else:
        raise SerializationError("EvaluationCriteria: no variant present")


def deserialize_aws_json_1_0(data: dict) -> EvaluationCriteria:
    if data.get("PromQLCriteria") is not None:
        import capo_cloudwatch.types.alarm_prom_ql_criteria

        return {
            "PromQLCriteria": capo_cloudwatch.types.alarm_prom_ql_criteria.deserialize_aws_json_1_0(
                data["PromQLCriteria"]
            )
        }
    else:
        name = next(
            (k for k, v in data.items() if v is not None and k != "__type"), None
        )
        if name is not None:
            return UnknownUnionMember(name)
        raise DeserializationError("EvaluationCriteria: no recognized variant key")
