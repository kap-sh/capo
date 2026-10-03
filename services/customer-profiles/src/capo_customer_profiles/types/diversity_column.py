"""Generated from Smithy shape ``com.amazonaws.customerprofiles#DiversityColumn``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

from capo_customer_profiles.errors import DeserializationError

if TYPE_CHECKING:
    import capo_customer_profiles.types.diversity_cap_type
    import capo_customer_profiles.types.diversity_target_expression
    import capo_customer_profiles.types.text


class DiversityColumn(TypedDict, closed=True):
    name: "capo_customer_profiles.types.text.text"
    """<p>The name of the item catalog column on which to apply the diversity cap. The column must be defined in the recommender schema.</p>"""
    cap_type: "capo_customer_profiles.types.diversity_cap_type.DiversityCapType"
    """<p>The type of diversity cap to apply. Valid values are <code>PERCENTAGE</code> (interpret <code>Target</code> as a percentage of returned items) and <code>VALUE</code> (interpret <code>Target</code> as an absolute count).</p>"""
    target: "capo_customer_profiles.types.diversity_target_expression.DiversityTargetExpression"
    """<p>The diversity cap target. Either an integer literal (for example, <code>"25"</code>) or a placeholder expression of the form <code>$name</code> whose value is supplied at inference time through <code>GetProfileRecommendations</code>.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: DiversityColumn) -> dict:
    out: dict = {}
    out["Name"] = value["name"]
    import capo_customer_profiles.types.diversity_cap_type

    out["CapType"] = capo_customer_profiles.types.diversity_cap_type.serialize_json(
        value["cap_type"]
    )
    out["Target"] = value["target"]
    return out


def deserialize_json(data: dict) -> DiversityColumn:
    out: DiversityColumn = {}  # type: ignore[typeddict-item]
    if data.get("Name") is not None:
        out["name"] = data["Name"]
    else:
        raise DeserializationError("DiversityColumn.name required")
    if data.get("CapType") is not None:
        import capo_customer_profiles.types.diversity_cap_type

        out["cap_type"] = (
            capo_customer_profiles.types.diversity_cap_type.deserialize_json(
                data["CapType"]
            )
        )
    else:
        raise DeserializationError("DiversityColumn.cap_type required")
    if data.get("Target") is not None:
        out["target"] = data["Target"]
    else:
        raise DeserializationError("DiversityColumn.target required")
    return out
