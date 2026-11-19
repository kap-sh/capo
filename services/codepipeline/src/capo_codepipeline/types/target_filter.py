"""Generated from Smithy shape ``com.amazonaws.codepipeline#TargetFilter``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_codepipeline.types.target_filter_name
    import capo_codepipeline.types.target_filter_value_list


class TargetFilter(TypedDict, closed=True):
    name: NotRequired["capo_codepipeline.types.target_filter_name.TargetFilterName"]
    """<p>The name on which to filter.</p>"""
    values: NotRequired[
        "capo_codepipeline.types.target_filter_value_list.TargetFilterValueList"
    ]
    """<p>The values on which to filter.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_codepipeline.types.target_filter_name

        out["name"] = capo_codepipeline.types.target_filter_name.serialize_aws_json_1_1(
            value["name"]
        )
    if "values" in value:
        import capo_codepipeline.types.target_filter_value_list

        out["values"] = (
            capo_codepipeline.types.target_filter_value_list.serialize_aws_json_1_1(
                value["values"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetFilter:
    out: TargetFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_codepipeline.types.target_filter_name

        out["name"] = (
            capo_codepipeline.types.target_filter_name.deserialize_aws_json_1_1(
                data["name"]
            )
        )
    if data.get("values") is not None:
        import capo_codepipeline.types.target_filter_value_list

        out["values"] = (
            capo_codepipeline.types.target_filter_value_list.deserialize_aws_json_1_1(
                data["values"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: TargetFilter) -> dict:
    out: dict = {}
    if "name" in value:
        import capo_codepipeline.types.target_filter_name

        out["name"] = capo_codepipeline.types.target_filter_name.serialize_cbor(
            value["name"]
        )
    if "values" in value:
        import capo_codepipeline.types.target_filter_value_list

        out["values"] = capo_codepipeline.types.target_filter_value_list.serialize_cbor(
            value["values"]
        )
    return out


def deserialize_cbor(data: dict) -> TargetFilter:
    out: TargetFilter = {}  # type: ignore[typeddict-item]
    if data.get("name") is not None:
        import capo_codepipeline.types.target_filter_name

        out["name"] = capo_codepipeline.types.target_filter_name.deserialize_cbor(
            data["name"]
        )
    if data.get("values") is not None:
        import capo_codepipeline.types.target_filter_value_list

        out["values"] = (
            capo_codepipeline.types.target_filter_value_list.deserialize_cbor(
                data["values"]
            )
        )
    return out
