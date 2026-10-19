"""Generated from Smithy shape ``com.amazonaws.resiliencehubv2#EksLabelSelectorRequirement``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_resiliencehubv2.types.eks_label_key
    import capo_resiliencehubv2.types.eks_label_selector_operator
    import capo_resiliencehubv2.types.eks_label_value_list


class EksLabelSelectorRequirement(TypedDict, closed=True):
    key: "capo_resiliencehubv2.types.eks_label_key.EksLabelKey"
    """<p>The label key that the requirement applies to.</p>"""
    operator: "capo_resiliencehubv2.types.eks_label_selector_operator.EksLabelSelectorOperator"
    """<p>The operator that relates the label key to the values.</p>"""
    values: NotRequired[
        "capo_resiliencehubv2.types.eks_label_value_list.EksLabelValueList"
    ]
    """<p>The label values to compare against. Specify values when the operator is IN or NOT_IN. Leave this empty when the operator is EXISTS or DOES_NOT_EXIST.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: EksLabelSelectorRequirement) -> dict:
    out: dict = {}
    out["key"] = value["key"]
    import capo_resiliencehubv2.types.eks_label_selector_operator

    out["operator"] = (
        capo_resiliencehubv2.types.eks_label_selector_operator.serialize_json(
            value["operator"]
        )
    )
    if "values" in value:
        import capo_resiliencehubv2.types.eks_label_value_list

        out["values"] = capo_resiliencehubv2.types.eks_label_value_list.serialize_json(
            value["values"]
        )
    return out


def deserialize_json(data: dict) -> EksLabelSelectorRequirement:
    out: EksLabelSelectorRequirement = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        out["key"] = data["key"]
    else:
        out["key"] = ""
    if data.get("operator") is not None:
        import capo_resiliencehubv2.types.eks_label_selector_operator

        out["operator"] = (
            capo_resiliencehubv2.types.eks_label_selector_operator.deserialize_json(
                data["operator"]
            )
        )
    else:
        import typing

        out["operator"] = typing.cast(
            "capo_resiliencehubv2.types.eks_label_selector_operator.EksLabelSelectorOperator",
            "",
        )
    if data.get("values") is not None:
        import capo_resiliencehubv2.types.eks_label_value_list

        out["values"] = (
            capo_resiliencehubv2.types.eks_label_value_list.deserialize_json(
                data["values"]
            )
        )
    return out
