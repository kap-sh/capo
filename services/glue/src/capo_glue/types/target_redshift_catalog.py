"""Generated from Smithy shape ``com.amazonaws.glue#TargetRedshiftCatalog``."""

from typing import TYPE_CHECKING

from typing_extensions import TypedDict

if TYPE_CHECKING:
    import capo_glue.types.resource_arn_string


class TargetRedshiftCatalog(TypedDict, closed=True):
    catalog_arn: "capo_glue.types.resource_arn_string.ResourceArnString"
    """<p>The Amazon Resource Name (ARN) of the catalog resource.</p>"""


# --- awsJson1_1 ser/de ---
def serialize_aws_json_1_1(value: TargetRedshiftCatalog) -> dict:
    out: dict = {}
    out["CatalogArn"] = value["catalog_arn"]
    return out


def deserialize_aws_json_1_1(data: dict) -> TargetRedshiftCatalog:
    out: TargetRedshiftCatalog = {}  # type: ignore[typeddict-item]
    if data.get("CatalogArn") is not None:
        out["catalog_arn"] = data["CatalogArn"]
    else:
        out["catalog_arn"] = ""
    return out
