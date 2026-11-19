"""Generated from Smithy shape ``com.amazonaws.appstream#AssociateAppBlockBuilderAppBlockResult``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_appstream.types.app_block_builder_app_block_association


class AssociateAppBlockBuilderAppBlockResult(TypedDict, closed=True):
    app_block_builder_app_block_association: NotRequired[
        "capo_appstream.types.app_block_builder_app_block_association.AppBlockBuilderAppBlockAssociation"
    ]
    """<p>The list of app block builders associated with app blocks.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: AssociateAppBlockBuilderAppBlockResult) -> dict:
    out: dict = {}
    if "app_block_builder_app_block_association" in value:
        import capo_appstream.types.app_block_builder_app_block_association

        out["AppBlockBuilderAppBlockAssociation"] = (
            capo_appstream.types.app_block_builder_app_block_association.serialize_aws_json_1_1(
                value["app_block_builder_app_block_association"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> AssociateAppBlockBuilderAppBlockResult:
    out: AssociateAppBlockBuilderAppBlockResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilderAppBlockAssociation") is not None:
        import capo_appstream.types.app_block_builder_app_block_association

        out["app_block_builder_app_block_association"] = (
            capo_appstream.types.app_block_builder_app_block_association.deserialize_aws_json_1_1(
                data["AppBlockBuilderAppBlockAssociation"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: AssociateAppBlockBuilderAppBlockResult) -> dict:
    out: dict = {}
    if "app_block_builder_app_block_association" in value:
        import capo_appstream.types.app_block_builder_app_block_association

        out["AppBlockBuilderAppBlockAssociation"] = (
            capo_appstream.types.app_block_builder_app_block_association.serialize_cbor(
                value["app_block_builder_app_block_association"]
            )
        )
    return out


def deserialize_cbor(data: dict) -> AssociateAppBlockBuilderAppBlockResult:
    out: AssociateAppBlockBuilderAppBlockResult = {}  # type: ignore[typeddict-item]
    if data.get("AppBlockBuilderAppBlockAssociation") is not None:
        import capo_appstream.types.app_block_builder_app_block_association

        out["app_block_builder_app_block_association"] = (
            capo_appstream.types.app_block_builder_app_block_association.deserialize_cbor(
                data["AppBlockBuilderAppBlockAssociation"]
            )
        )
    return out
