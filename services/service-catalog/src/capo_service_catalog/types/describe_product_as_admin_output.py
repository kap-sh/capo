"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProductAsAdminOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.budgets
    import capo_service_catalog.types.product_view_detail
    import capo_service_catalog.types.provisioning_artifact_summaries
    import capo_service_catalog.types.tag_option_details
    import capo_service_catalog.types.tags


class DescribeProductAsAdminOutput(TypedDict, closed=True):
    product_view_detail: NotRequired[
        "capo_service_catalog.types.product_view_detail.ProductViewDetail"
    ]
    """<p>Information about the product view.</p>"""
    provisioning_artifact_summaries: NotRequired[
        "capo_service_catalog.types.provisioning_artifact_summaries.ProvisioningArtifactSummaries"
    ]
    """<p>Information about the provisioning artifacts (also known as versions) for the specified product.</p>"""
    tags: NotRequired["capo_service_catalog.types.tags.Tags"]
    """<p>Information about the tags associated with the product.</p>"""
    tag_options: NotRequired[
        "capo_service_catalog.types.tag_option_details.TagOptionDetails"
    ]
    """<p>Information about the TagOptions associated with the product.</p>"""
    budgets: NotRequired["capo_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProductAsAdminOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import capo_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            capo_service_catalog.types.product_view_detail.serialize_aws_json_1_1(
                value["product_view_detail"]
            )
        )
    if "provisioning_artifact_summaries" in value:
        import capo_service_catalog.types.provisioning_artifact_summaries

        out["ProvisioningArtifactSummaries"] = (
            capo_service_catalog.types.provisioning_artifact_summaries.serialize_aws_json_1_1(
                value["provisioning_artifact_summaries"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_aws_json_1_1(
            value["tags"]
        )
    if "tag_options" in value:
        import capo_service_catalog.types.tag_option_details

        out["TagOptions"] = (
            capo_service_catalog.types.tag_option_details.serialize_aws_json_1_1(
                value["tag_options"]
            )
        )
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProductAsAdminOutput:
    out: DescribeProductAsAdminOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetail") is not None:
        import capo_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            capo_service_catalog.types.product_view_detail.deserialize_aws_json_1_1(
                data["ProductViewDetail"]
            )
        )
    if data.get("ProvisioningArtifactSummaries") is not None:
        import capo_service_catalog.types.provisioning_artifact_summaries

        out["provisioning_artifact_summaries"] = (
            capo_service_catalog.types.provisioning_artifact_summaries.deserialize_aws_json_1_1(
                data["ProvisioningArtifactSummaries"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_aws_json_1_1(
            data["Tags"]
        )
    if data.get("TagOptions") is not None:
        import capo_service_catalog.types.tag_option_details

        out["tag_options"] = (
            capo_service_catalog.types.tag_option_details.deserialize_aws_json_1_1(
                data["TagOptions"]
            )
        )
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProductAsAdminOutput) -> dict:
    out: dict = {}
    if "product_view_detail" in value:
        import capo_service_catalog.types.product_view_detail

        out["ProductViewDetail"] = (
            capo_service_catalog.types.product_view_detail.serialize_cbor(
                value["product_view_detail"]
            )
        )
    if "provisioning_artifact_summaries" in value:
        import capo_service_catalog.types.provisioning_artifact_summaries

        out["ProvisioningArtifactSummaries"] = (
            capo_service_catalog.types.provisioning_artifact_summaries.serialize_cbor(
                value["provisioning_artifact_summaries"]
            )
        )
    if "tags" in value:
        import capo_service_catalog.types.tags

        out["Tags"] = capo_service_catalog.types.tags.serialize_cbor(value["tags"])
    if "tag_options" in value:
        import capo_service_catalog.types.tag_option_details

        out["TagOptions"] = (
            capo_service_catalog.types.tag_option_details.serialize_cbor(
                value["tag_options"]
            )
        )
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_cbor(
            value["budgets"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProductAsAdminOutput:
    out: DescribeProductAsAdminOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewDetail") is not None:
        import capo_service_catalog.types.product_view_detail

        out["product_view_detail"] = (
            capo_service_catalog.types.product_view_detail.deserialize_cbor(
                data["ProductViewDetail"]
            )
        )
    if data.get("ProvisioningArtifactSummaries") is not None:
        import capo_service_catalog.types.provisioning_artifact_summaries

        out["provisioning_artifact_summaries"] = (
            capo_service_catalog.types.provisioning_artifact_summaries.deserialize_cbor(
                data["ProvisioningArtifactSummaries"]
            )
        )
    if data.get("Tags") is not None:
        import capo_service_catalog.types.tags

        out["tags"] = capo_service_catalog.types.tags.deserialize_cbor(data["Tags"])
    if data.get("TagOptions") is not None:
        import capo_service_catalog.types.tag_option_details

        out["tag_options"] = (
            capo_service_catalog.types.tag_option_details.deserialize_cbor(
                data["TagOptions"]
            )
        )
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_cbor(
            data["Budgets"]
        )
    return out
