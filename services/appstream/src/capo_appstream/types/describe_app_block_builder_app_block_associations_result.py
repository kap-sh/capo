"""Generated from Smithy shape ``com.amazonaws.appstream#DescribeAppBlockBuilderAppBlockAssociationsResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder_app_block_associations_list
    import capo_appstream.types.string


class DescribeAppBlockBuilderAppBlockAssociationsResult(TypedDict, closed=True):
    app_block_builder_app_block_associations: NotRequired[
        "capo_appstream.types.app_block_builder_app_block_associations_list.AppBlockBuilderAppBlockAssociationsList"
    ]
    """<p>This list of app block builders associated with app blocks.</p>"""
    next_token: NotRequired["capo_appstream.types.string.String"]
    """<p>The pagination token used to retrieve the next page of results for this operation.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(
    value: DescribeAppBlockBuilderAppBlockAssociationsResult,
) -> dict:
    out: dict = {}
    if "app_block_builder_app_block_associations" in value:
        import capo_appstream.types.app_block_builder_app_block_associations_list

        out["AppBlockBuilderAppBlockAssociations"] = (
            capo_appstream.types.app_block_builder_app_block_associations_list.serialize_aws_json_1_1(
                value["app_block_builder_app_block_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_aws_json_1_1(
    data: dict,
) -> DescribeAppBlockBuilderAppBlockAssociationsResult:
    out: DescribeAppBlockBuilderAppBlockAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilderAppBlockAssociations") is not None:
        import capo_appstream.types.app_block_builder_app_block_associations_list

        out["app_block_builder_app_block_associations"] = (
            capo_appstream.types.app_block_builder_app_block_associations_list.deserialize_aws_json_1_1(
                data["AppBlockBuilderAppBlockAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeAppBlockBuilderAppBlockAssociationsResult) -> dict:
    out: dict = {}
    if "app_block_builder_app_block_associations" in value:
        import capo_appstream.types.app_block_builder_app_block_associations_list

        out["AppBlockBuilderAppBlockAssociations"] = (
            capo_appstream.types.app_block_builder_app_block_associations_list.serialize_cbor(
                value["app_block_builder_app_block_associations"]
            )
        )
    if "next_token" in value:
        out["NextToken"] = value["next_token"]
    return out


def deserialize_cbor(data: dict) -> DescribeAppBlockBuilderAppBlockAssociationsResult:
    out: DescribeAppBlockBuilderAppBlockAssociationsResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilderAppBlockAssociations") is not None:
        import capo_appstream.types.app_block_builder_app_block_associations_list

        out["app_block_builder_app_block_associations"] = (
            capo_appstream.types.app_block_builder_app_block_associations_list.deserialize_cbor(
                data["AppBlockBuilderAppBlockAssociations"]
            )
        )
    if data.get("NextToken") is not None:
        out["next_token"] = data["NextToken"]
    return out
