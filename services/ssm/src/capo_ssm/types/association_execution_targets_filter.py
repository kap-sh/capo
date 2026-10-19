"""Generated from Smithy shape ``com.amazonaws.ssm#AssociationExecutionTargetsFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_ssm.types.association_execution_targets_filter_key
    import capo_ssm.types.association_execution_targets_filter_value


class AssociationExecutionTargetsFilter(TypedDict, closed=True):
    key: "capo_ssm.types.association_execution_targets_filter_key.AssociationExecutionTargetsFilterKey"
    """<p>The key value used in the request.</p>"""
    value: "capo_ssm.types.association_execution_targets_filter_value.AssociationExecutionTargetsFilterValue"
    """<p>The value specified for the key.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociationExecutionTargetsFilter) -> dict:
    out: dict = {}
    import capo_ssm.types.association_execution_targets_filter_key

    out["Key"] = (
        capo_ssm.types.association_execution_targets_filter_key.serialize_aws_json_1_1(
            value["key"]
        )
    )
    out["Value"] = value["value"]
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociationExecutionTargetsFilter:
    out: AssociationExecutionTargetsFilter = {}  # type: ignore[typeddict-item]
    if data.get("Key") is not None:
        import capo_ssm.types.association_execution_targets_filter_key

        out["key"] = (
            capo_ssm.types.association_execution_targets_filter_key.deserialize_aws_json_1_1(
                data["Key"]
            )
        )
    else:
        import typing

        out["key"] = typing.cast(
            "capo_ssm.types.association_execution_targets_filter_key.AssociationExecutionTargetsFilterKey",
            "",
        )
    if data.get("Value") is not None:
        out["value"] = data["Value"]
    else:
        out["value"] = ""
    return out
