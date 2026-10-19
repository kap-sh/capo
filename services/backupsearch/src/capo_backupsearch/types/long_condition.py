"""Generated from Smithy shape ``com.amazonaws.backupsearch#LongCondition``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_backupsearch.types.long_condition_operator


class LongCondition(TypedDict, closed=True):
    value: "int"
    """<p>The value of an item included in one of the search item filters.</p>"""
    operator: "capo_backupsearch.types.long_condition_operator.LongConditionOperator"
    """<p>A string that defines what values will be returned.</p> <p>If this is included, avoid combinations of operators that will return all possible values. For example, including both <code>EQUALS_TO</code> and <code>NOT_EQUALS_TO</code> with a value of <code>4</code> will return all values.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: LongCondition) -> dict:
    out: dict = {}
    out["Value"] = value["value"]
    import capo_backupsearch.types.long_condition_operator

    out["Operator"] = capo_backupsearch.types.long_condition_operator.serialize_json(
        value.get("operator", "EQUALS_TO")
    )
    return out


def deserialize_json(data: dict) -> LongCondition:
    out: LongCondition = {}  # type: ignore[typeddict-item]
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = 0
    if data.get("Operator") is not None:
        import capo_backupsearch.types.long_condition_operator

        out["operator"] = (
            capo_backupsearch.types.long_condition_operator.deserialize_json(
                data["Operator"]
            )
        )
    else:
        out["operator"] = "EQUALS_TO"
    return out
