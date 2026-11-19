"""Generated from Smithy shape ``com.amazonaws.servicecatalog#DescribeProductOutput``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

if TYPE_CHECKING:
    import capo_service_catalog.types.budgets
    import capo_service_catalog.types.launch_paths
    import capo_service_catalog.types.product_view_summary
    import capo_service_catalog.types.provisioning_artifacts


class DescribeProductOutput(TypedDict, closed=True):
    product_view_summary: NotRequired[
        "capo_service_catalog.types.product_view_summary.ProductViewSummary"
    ]
    """<p>Summary information about the product view.</p>"""
    provisioning_artifacts: NotRequired[
        "capo_service_catalog.types.provisioning_artifacts.ProvisioningArtifacts"
    ]
    """<p>Information about the provisioning artifacts for the specified product.</p>"""
    budgets: NotRequired["capo_service_catalog.types.budgets.Budgets"]
    """<p>Information about the associated budgets.</p>"""
    launch_paths: NotRequired["capo_service_catalog.types.launch_paths.LaunchPaths"]
    """<p>Information about the associated launch paths.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: DescribeProductOutput) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import capo_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            capo_service_catalog.types.product_view_summary.serialize_aws_json_1_1(
                value["product_view_summary"]
            )
        )
    if "provisioning_artifacts" in value:
        import capo_service_catalog.types.provisioning_artifacts

        out["ProvisioningArtifacts"] = (
            capo_service_catalog.types.provisioning_artifacts.serialize_aws_json_1_1(
                value["provisioning_artifacts"]
            )
        )
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_aws_json_1_1(
            value["budgets"]
        )
    if "launch_paths" in value:
        import capo_service_catalog.types.launch_paths

        out["LaunchPaths"] = (
            capo_service_catalog.types.launch_paths.serialize_aws_json_1_1(
                value["launch_paths"]
            )
        )
    return out


def deserialize_aws_json_1_1(data: dict) -> DescribeProductOutput:
    out: DescribeProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewSummary") is not None:
        import capo_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            capo_service_catalog.types.product_view_summary.deserialize_aws_json_1_1(
                data["ProductViewSummary"]
            )
        )
    if data.get("ProvisioningArtifacts") is not None:
        import capo_service_catalog.types.provisioning_artifacts

        out["provisioning_artifacts"] = (
            capo_service_catalog.types.provisioning_artifacts.deserialize_aws_json_1_1(
                data["ProvisioningArtifacts"]
            )
        )
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_aws_json_1_1(
            data["Budgets"]
        )
    if data.get("LaunchPaths") is not None:
        import capo_service_catalog.types.launch_paths

        out["launch_paths"] = (
            capo_service_catalog.types.launch_paths.deserialize_aws_json_1_1(
                data["LaunchPaths"]
            )
        )
    return out


# --- rpcv2Cbor ser/de ---
def serialize_cbor(value: DescribeProductOutput) -> dict:
    out: dict = {}
    if "product_view_summary" in value:
        import capo_service_catalog.types.product_view_summary

        out["ProductViewSummary"] = (
            capo_service_catalog.types.product_view_summary.serialize_cbor(
                value["product_view_summary"]
            )
        )
    if "provisioning_artifacts" in value:
        import capo_service_catalog.types.provisioning_artifacts

        out["ProvisioningArtifacts"] = (
            capo_service_catalog.types.provisioning_artifacts.serialize_cbor(
                value["provisioning_artifacts"]
            )
        )
    if "budgets" in value:
        import capo_service_catalog.types.budgets

        out["Budgets"] = capo_service_catalog.types.budgets.serialize_cbor(
            value["budgets"]
        )
    if "launch_paths" in value:
        import capo_service_catalog.types.launch_paths

        out["LaunchPaths"] = capo_service_catalog.types.launch_paths.serialize_cbor(
            value["launch_paths"]
        )
    return out


def deserialize_cbor(data: dict) -> DescribeProductOutput:
    out: DescribeProductOutput = {}  # type: ignore[typeddict-item]
    if data.get("ProductViewSummary") is not None:
        import capo_service_catalog.types.product_view_summary

        out["product_view_summary"] = (
            capo_service_catalog.types.product_view_summary.deserialize_cbor(
                data["ProductViewSummary"]
            )
        )
    if data.get("ProvisioningArtifacts") is not None:
        import capo_service_catalog.types.provisioning_artifacts

        out["provisioning_artifacts"] = (
            capo_service_catalog.types.provisioning_artifacts.deserialize_cbor(
                data["ProvisioningArtifacts"]
            )
        )
    if data.get("Budgets") is not None:
        import capo_service_catalog.types.budgets

        out["budgets"] = capo_service_catalog.types.budgets.deserialize_cbor(
            data["Budgets"]
        )
    if data.get("LaunchPaths") is not None:
        import capo_service_catalog.types.launch_paths

        out["launch_paths"] = capo_service_catalog.types.launch_paths.deserialize_cbor(
            data["LaunchPaths"]
        )
    return out
