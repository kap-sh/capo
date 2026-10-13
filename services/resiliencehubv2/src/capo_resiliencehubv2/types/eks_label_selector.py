"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksLabelSelector``."""

from typing import TYPE_CHECKING, Any

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.eks_label_map
    import capo_resiliencehubv2.types.eks_label_selector_requirement_list


class EksLabelSelector(TypedDict, closed=True):
    match_labels: NotRequired["capo_resiliencehubv2.types.eks_label_map.EksLabelMap"]
    """<p>The label key-value pairs that an object must have. All pairs must match for the object to be selected.</p>"""
    match_expressions: NotRequired[
        "capo_resiliencehubv2.types.eks_label_selector_requirement_list.EksLabelSelectorRequirementList"
    ]
    """<p>The label requirements that an object must satisfy. All requirements in the list must match for the object to be selected.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksLabelSelector) -> dict:
    out: dict = {}
    if "match_labels" in value:
        import capo_resiliencehubv2.types.eks_label_map

        out["matchLabels"] = capo_resiliencehubv2.types.eks_label_map.serialize_json(
            value["match_labels"]
        )
    if "match_expressions" in value:
        import capo_resiliencehubv2.types.eks_label_selector_requirement_list

        out["matchExpressions"] = (
            capo_resiliencehubv2.types.eks_label_selector_requirement_list.serialize_json(
                value["match_expressions"]
            )
        )
    return out


def deserialize_json(data: dict) -> EksLabelSelector:
    out: EksLabelSelector = {}  # type: ignore[typeddict-item]
    if data.get("matchLabels") is not None:
        import capo_resiliencehubv2.types.eks_label_map

        out["match_labels"] = capo_resiliencehubv2.types.eks_label_map.deserialize_json(
            data["matchLabels"]
        )
    if data.get("matchExpressions") is not None:
        import capo_resiliencehubv2.types.eks_label_selector_requirement_list

        out["match_expressions"] = (
            capo_resiliencehubv2.types.eks_label_selector_requirement_list.deserialize_json(
                data["matchExpressions"]
            )
        )
    return out


def redact_sensitive(value: EksLabelSelector) -> dict[str, Any]:
    out: dict[str, Any] = dict(value)
    if "match_labels" in value:
        out["match_labels"] = "*** Sensitive Data Redacted ***"
    if "match_expressions" in value:
        out["match_expressions"] = "*** Sensitive Data Redacted ***"
    return out
