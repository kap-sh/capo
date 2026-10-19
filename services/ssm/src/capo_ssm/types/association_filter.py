"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_filter_key
    import capo_ssm.types.association_filter_value


class AssociationFilter(TypedDict, closed=True):
    key: "capo_ssm.types.association_filter_key.AssociationFilterKey"
    """<p>The name of the filter.</p> <note> <p> <code>InstanceId</code> has been deprecated.</p> </note>"""
    value: "capo_ssm.types.association_filter_value.AssociationFilterValue"
    """<p>The filter value.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.association_filter_key

    out["key"] = capo_ssm.types.association_filter_key.serialize_aws_json_1_1(
        value["key"]
    )
    out["value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationFilter:
    out: AssociationFilter = {}  # type: ignore[typeddict-item]
    if data.get("key") is not None:
        import capo_ssm.types.association_filter_key

        out["key"] = capo_ssm.types.association_filter_key.deserialize_aws_json_1_1(
            data["key"]
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.association_filter_key.AssociationFilterKey", ""
        )
    if data.get("value") is not None:
        out["value"] = data["value"]
    else:
        out["value"] = ""
    return out
