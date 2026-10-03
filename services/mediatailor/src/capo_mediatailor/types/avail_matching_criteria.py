"""Generated from Smithy shape ``com.amazonaws.mediatailor#AvailMatchingCriteria``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_mediatailor.errors import DeserializationError

if TYPE_CHECKING:
    import capo_mediatailor.types.__string
    import capo_mediatailor.types.operator


class AvailMatchingCriteria(TypedDict, closed=True):
    dynamic_variable: "capo_mediatailor.types.__string.__string"
    """<p>The dynamic variable(s) that MediaTailor should use as avail matching criteria. MediaTailor only places the prefetched ads into the avail if the avail matches the criteria defined by the dynamic variable. For information about dynamic variables, see <a href="https://docs.aws.amazon.com/mediatailor/latest/ug/variables.html">Using dynamic ad variables</a> in the <i>MediaTailor User Guide</i>.</p> <p>You can include up to 100 dynamic variables.</p>"""
    operator: "capo_mediatailor.types.operator.Operator"
    """<p>For the <code>DynamicVariable</code> specified in <code>AvailMatchingCriteria</code>, the Operator that is used for the comparison.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: AvailMatchingCriteria) -> dict:
    out: dict = {}
    out["DynamicVariable"] = value["dynamic_variable"]
    import capo_mediatailor.types.operator

    out["Operator"] = capo_mediatailor.types.operator.serialize_json(value["operator"])
    return out


def deserialize_json(data: dict) -> AvailMatchingCriteria:
    out: AvailMatchingCriteria = {}  # type: ignore[typeddict-item]
    if data.get("DynamicVariable") is not None:
        out["dynamic_variable"] = data["DynamicVariable"]
    else:
        raise DeserializationError("AvailMatchingCriteria.dynamic_variable required")
    if data.get("Operator") is not None:
        import capo_mediatailor.types.operator

        out["operator"] = capo_mediatailor.types.operator.deserialize_json(
            data["Operator"]
        )
    else:
        raise DeserializationError("AvailMatchingCriteria.operator required")
    return out
