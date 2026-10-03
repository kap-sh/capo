"""Generated from Smithy shape ``com.amazonaws.resiliencehub#ImportResourcesToDraftAppVersionRequest``."""

from typing import TYPE_CHECKING

from typing_extensions import NotRequired, TypedDict

from capo_resiliencehub.errors import DeserializationError

if TYPE_CHECKING:
    import capo_resiliencehub.types.arn
    import capo_resiliencehub.types.arn_list
    import capo_resiliencehub.types.eks_source_list
    import capo_resiliencehub.types.resource_import_strategy_type
    import capo_resiliencehub.types.terraform_source_list


class ImportResourcesToDraftAppVersionRequest(TypedDict, closed=True):
    app_arn: "capo_resiliencehub.types.arn.Arn"
    """<p>Amazon Resource Name (ARN) of the Resilience Hub application. The format for this ARN is: arn:<code>partition</code>:resiliencehub:<code>region</code>:<code>account</code>:app/<code>app-id</code>. For more information about ARNs, see <a href="https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html"> Amazon Resource Names (ARNs)</a> in the <i>Amazon Web Services General Reference</i> guide.</p>"""
    source_arns: NotRequired["capo_resiliencehub.types.arn_list.ArnList"]
    """<p>The Amazon Resource Names (ARNs) for the resources.</p>"""
    terraform_sources: NotRequired[
        "capo_resiliencehub.types.terraform_source_list.TerraformSourceList"
    ]
    """<p> A list of terraform file s3 URLs you need to import. </p>"""
    import_strategy: NotRequired[
        "capo_resiliencehub.types.resource_import_strategy_type.ResourceImportStrategyType"
    ]
    """<p>The import strategy you would like to set to import resources into Resilience Hub application.</p>"""
    eks_sources: NotRequired["capo_resiliencehub.types.eks_source_list.EksSourceList"]
    """<p>The input sources of the Amazon Elastic Kubernetes Service resources you need to import.</p>"""


# --- restJson1 ser/de ---
def serialize_json(value: ImportResourcesToDraftAppVersionRequest) -> dict:
    out: dict = {}
    out["appArn"] = value["app_arn"]
    if "source_arns" in value:
        import capo_resiliencehub.types.arn_list

        out["sourceArns"] = capo_resiliencehub.types.arn_list.serialize_json(
            value["source_arns"]
        )
    if "terraform_sources" in value:
        import capo_resiliencehub.types.terraform_source_list

        out["terraformSources"] = (
            capo_resiliencehub.types.terraform_source_list.serialize_json(
                value["terraform_sources"]
            )
        )
    if "import_strategy" in value:
        import capo_resiliencehub.types.resource_import_strategy_type

        out["importStrategy"] = (
            capo_resiliencehub.types.resource_import_strategy_type.serialize_json(
                value["import_strategy"]
            )
        )
    if "eks_sources" in value:
        import capo_resiliencehub.types.eks_source_list

        out["eksSources"] = capo_resiliencehub.types.eks_source_list.serialize_json(
            value["eks_sources"]
        )
    return out


def deserialize_json(data: dict) -> ImportResourcesToDraftAppVersionRequest:
    out: ImportResourcesToDraftAppVersionRequest = {}  # type: ignore[typeddict-item]
    if data.get("appArn") is not None:
        out["app_arn"] = data["appArn"]
    else:
        raise DeserializationError(
            "ImportResourcesToDraftAppVersionRequest.app_arn required"
        )
    if data.get("sourceArns") is not None:
        import capo_resiliencehub.types.arn_list

        out["source_arns"] = capo_resiliencehub.types.arn_list.deserialize_json(
            data["sourceArns"]
        )
    if data.get("terraformSources") is not None:
        import capo_resiliencehub.types.terraform_source_list

        out["terraform_sources"] = (
            capo_resiliencehub.types.terraform_source_list.deserialize_json(
                data["terraformSources"]
            )
        )
    if data.get("importStrategy") is not None:
        import capo_resiliencehub.types.resource_import_strategy_type

        out["import_strategy"] = (
            capo_resiliencehub.types.resource_import_strategy_type.deserialize_json(
                data["importStrategy"]
            )
        )
    if data.get("eksSources") is not None:
        import capo_resiliencehub.types.eks_source_list

        out["eks_sources"] = capo_resiliencehub.types.eks_source_list.deserialize_json(
            data["eksSources"]
        )
    return out
