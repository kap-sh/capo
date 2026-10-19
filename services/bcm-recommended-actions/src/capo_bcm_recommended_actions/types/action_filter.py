"""Generated from Smithy shape ``com.amazonaws.bcmrecommendedactions#ActionFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_bcm_recommended_actions.types.filter_name
    import capo_bcm_recommended_actions.types.filter_values
    import capo_bcm_recommended_actions.types.match_option


class ActionFilter(TypedDict, closed=True):
    key: "capo_bcm_recommended_actions.types.filter_name.FilterName"
    """<p>The category to filter on. Valid values are <code>FEATURE</code> for feature type, <code>SEVERITY</code> for severity level, and <code>TYPE</code> for recommendation type.</p>"""
    match_option: "capo_bcm_recommended_actions.types.match_option.MatchOption"
    """<p>Specifies how to apply the filter. Use <code>EQUALS</code> to include matching results or <code>NOT_EQUALS</code> to exclude matching results.</p>"""
    values: "capo_bcm_recommended_actions.types.filter_values.FilterValues"
    """<p>One or more values to match against the specified key.</p>"""


# --- awsJson1_0 ser/de ---
def serialize_aws_json_1_0(value: ActionFilter) -> dict:
    out: dict = {}
    import capo_bcm_recommended_actions.types.filter_name

    out["key"] = capo_bcm_recommended_actions.types.filter_name.serialize_aws_json_1_0(
        value["key"]
    )
    import capo_bcm_recommended_actions.types.match_option

    out["matchOption"] = (
        capo_bcm_recommended_actions.types.match_option.serialize_aws_json_1_0(
            value["match_option"]
        )
    )
    import capo_bcm_recommended_actions.types.filter_values

    out["values"] = (
        capo_bcm_recommended_actions.types.filter_values.serialize_aws_json_1_0(
            value["values"]
        )
    )
    return out


def deserialize_aws_json_1_0(data: dict) -> ActionFilter:
    out: ActionFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_bcm_recommended_actions.types.filter_name

        out["key"] = (
            capo_bcm_recommended_actions.types.filter_name.deserialize_aws_json_1_0(
                data["key"]
            )
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_bcm_recommended_actions.types.filter_name.FilterName", ""
        )
    if data.get("matchOption") is not None:
        import capo_bcm_recommended_actions.types.match_option

        out["match_option"] = (
            capo_bcm_recommended_actions.types.match_option.deserialize_aws_json_1_0(
                data["matchOption"]
            )
        )
    else:
        import typing

        out["match_option"] = typing.cast(
            "capo_bcm_recommended_actions.types.match_option.MatchOption", ""
        )
    if data.get("values") is not None:
        import capo_bcm_recommended_actions.types.filter_values

        out["values"] = (
            capo_bcm_recommended_actions.types.filter_values.deserialize_aws_json_1_0(
                data["values"]
            )
        )
    else:
        out["values"] = []
    return out
